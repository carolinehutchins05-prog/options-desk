#!/usr/bin/env python3
"""Backtest of the Options Desk screen against the S&P 500.

Everything below is fixed BEFORE any result is seen. Nothing is tuned.

What is real and what is modeled
  Real:    daily prices for every current S&P 500 name, and the SPY benchmark.
           The trend gate, the RSI band and the recent high gate are tested on those.
  Modeled: option prices. No free source has historical option chains, so contracts
           are priced with Black Scholes from each stock's trailing 30 day realized
           volatility. Spread, open interest, volume, bid size and earnings gates
           cannot be tested and are not.

Rules as published on the methodology page
  Call: close above a rising 50 day average, RSI(14) 45 to 70, no 52 week high in
        the last 3 sessions.
  Put:  close below a falling 50 day average, RSI(14) 30 to 55.
  Contract: delta 0.55, 30 calendar days to expiry (45 as a sensitivity), implied vol
        proxy under 40%, break even within 3% of spot, calls: break even below the
        52 week high, theta under 5% of premium per day.
  Entry: next session open. Exit: first close at +50% on the contract, else the
        close of the 5th session. Round trip cost: 2% half spread each way.

Known biases, stated up front
  Survivorship: only names in the index today are tested. This flatters long trend
  signals and understates losers that were later dropped.
  Constant IV: no vol crush or vol expansion is modeled.
  Not independent: signals on the same stock on adjacent days overlap, so results
  are resampled by calendar month to get honest confidence intervals.
"""
import json, sys
import numpy as np, pandas as pd
from scipy.special import ndtr, ndtri

R = 0.04
DELTA = 0.55
HALF_SPREAD = 0.02
TARGET = 0.50
HOLD = 5
rng = np.random.default_rng(7)

px = pd.read_pickle(sys.argv[1] if len(sys.argv) > 1 else "prices.pkl")
O, H, C = px["Open"], px["High"], px["Close"]
spy_o, spy_c = O["SPY"], C["SPY"]
tick = [t for t in C.columns if t != "SPY"]
O, C = O[tick], C[tick]
dates = C.index
n = len(dates)

# ---------- indicators (all use data through the close of day i) ----------
sma50 = C.rolling(50).mean()
rising = sma50 > sma50.shift(10)
falling = sma50 < sma50.shift(10)
d = C.diff()
up = d.clip(lower=0).ewm(alpha=1 / 14, adjust=False).mean()
dn = (-d.clip(upper=0)).ewm(alpha=1 / 14, adjust=False).mean()
rsi = 100 - 100 / (1 + up / dn.replace(0, np.nan))
hi252 = C.rolling(252).max()
high_recent = C.rolling(3).max() >= hi252
rv30 = np.log(C / C.shift(1)).rolling(30).std() * np.sqrt(252)
spy_regime = (spy_c > spy_c.rolling(200).mean()).reindex(dates)

call_sig = (C > sma50) & rising & (rsi >= 45) & (rsi <= 70) & ~high_recent
put_sig = (C < sma50) & falling & (rsi >= 30) & (rsi <= 55)
valid = sma50.notna() & rsi.notna() & hi252.notna() & rv30.notna()
any_day = valid.copy()

# need entry at i+1 and exit by i+HOLD+1 ... plus 21 day underlying look ahead
last_i = n - 1 - 22
lastmask = pd.Series(np.arange(n) <= last_i, index=dates)

def bs(S, K, T, v, call):
    d1 = (np.log(S / K) + (R + 0.5 * v * v) * T) / (v * np.sqrt(T))
    d2 = d1 - v * np.sqrt(T)
    if call:
        return S * ndtr(d1) - K * np.exp(-R * T) * ndtr(d2)
    return K * np.exp(-R * T) * ndtr(-d2) - S * ndtr(-d1)

def idx(mask):
    m = mask & valid & lastmask.values[:, None]
    return np.nonzero(m.values)

def option_trades(mask, call, dte=30, ivmult=1.15, half=HALF_SPREAD, gates=True, bench=None):
    """Return per trade contract returns for every day/stock in mask, plus metadata."""
    ii, jj = idx(mask) if bench is None else bench
    Oa, Ca = O.values, C.values
    S0 = Oa[ii + 1, jj]
    v = rv30.values[ii, jj] * ivmult
    ok = np.isfinite(S0) & np.isfinite(v) & (v > 0.05)
    T0 = dte / 365
    d1 = ndtri(DELTA) if call else ndtri(1 - DELTA)
    with np.errstate(all="ignore"):
        K = S0 * np.exp(-(d1 * v * np.sqrt(T0)) + (R + 0.5 * v * v) * T0)
        P0 = bs(S0, K, T0, v, call)
        be = K + P0 if call else K - P0
        theta = (bs(S0, K, T0 - 1 / 365, v, call) - P0) / P0
    gate = np.ones(len(ii), bool)
    stats_funnel = {"signals": int(ok.sum())}
    if gates:
        g_iv = v < 0.40
        g_be = np.abs(be / S0 - 1) <= 0.03
        g_ceil = (be < hi252.values[ii, jj]) if call else np.ones(len(ii), bool)
        g_th = np.abs(theta) < 0.05
        gate = g_iv & g_be & g_ceil & g_th
        stats_funnel.update({"iv_under_40": int((ok & g_iv).sum()),
                             "plus_break_even_3pct": int((ok & g_iv & g_be).sum()),
                             "plus_below_52w_high": int((ok & g_iv & g_be & g_ceil).sum()),
                             "plus_theta_under_5pct": int((ok & gate).sum())})
    keep = ok & gate & np.isfinite(P0) & (P0 > 0)
    ii, jj, S0, K, P0, v = ii[keep], jj[keep], S0[keep], K[keep], P0[keep], v[keep]
    V = np.empty((len(ii), HOLD))
    for k in range(HOLD):
        Tk = T0 - (k + 0.75) / 252
        V[:, k] = bs(Ca[ii + 1 + k, jj], K, Tk, v, call)
    hit = V >= (1 + TARGET) * P0[:, None]
    first = np.where(hit.any(1), hit.argmax(1), HOLD - 1)
    exitv = V[np.arange(len(ii)), first]
    ret = exitv * (1 - half) / (P0 * (1 + half)) - 1
    ok2 = np.isfinite(ret)
    return ret[ok2], ii[ok2], jj[ok2], hit.any(1)[ok2], stats_funnel

def month_id(ii):
    ds = dates[ii]
    return (ds.year * 12 + ds.month).values

def boot_mean(vals, months, reps=2000):
    u, inv = np.unique(months, return_inverse=True)
    s = np.bincount(inv, weights=vals)
    c = np.bincount(inv).astype(float)
    out = np.empty(reps)
    for r in range(reps):
        pick = rng.integers(0, len(u), len(u))
        out[r] = s[pick].sum() / c[pick].sum()
    return float(np.percentile(out, 2.5)), float(np.percentile(out, 97.5))

def summarize(ret, ii, hit):
    if len(ret) == 0:
        return {"n": 0}
    lo, hi = boot_mean(ret, month_id(ii))
    return {"n": int(len(ret)), "mean": float(ret.mean()), "median": float(np.median(ret)),
            "win_rate": float((ret > 0).mean()), "target_hit": float(hit.mean()),
            "avg_win": float(ret[ret > 0].mean()) if (ret > 0).any() else None,
            "avg_loss": float(ret[ret <= 0].mean()) if (ret <= 0).any() else None,
            "ci95": [lo, hi]}

def diff_ci(a, ia, b, ib, reps=2000):
    """Mean(a) minus mean(b), resampled by calendar month."""
    ma, mb = month_id(ia), month_id(ib)
    u = np.unique(np.concatenate([ma, mb]))
    sa = np.array([a[ma == m].sum() for m in u]); ca = np.array([(ma == m).sum() for m in u], float)
    sb = np.array([b[mb == m].sum() for m in u]); cb = np.array([(mb == m).sum() for m in u], float)
    out = []
    for _ in range(reps):
        p = rng.integers(0, len(u), len(u))
        if ca[p].sum() == 0 or cb[p].sum() == 0: continue
        out.append(sa[p].sum() / ca[p].sum() - sb[p].sum() / cb[p].sum())
    return float(a.mean() - b.mean()), float(np.percentile(out, 2.5)), float(np.percentile(out, 97.5))

results = {"universe": len(tick), "start": str(dates[0].date()), "end": str(dates[-1].date())}

# ---------- Part 1: the underlying, all real data ----------
Oa, Ca = O.values, C.values
spo, spc = spy_o.reindex(dates).values, spy_c.reindex(dates).values

def fwd(ii, jj, h):
    return Ca[ii + h, jj] / Oa[ii + 1, jj] - 1, spc[ii + h] / spo[ii + 1] - 1

und = {}
base_i, base_j = idx(any_day)
for name, mask in (("call_signal", call_sig), ("put_signal", put_sig)):
    ii, jj = idx(mask)
    row = {"n": int(len(ii))}
    for h in (5, 21):
        r, s = fwd(ii, jj, h)
        rb, sb = fwd(base_i, base_j, h)
        ok = np.isfinite(r) & np.isfinite(s); okb = np.isfinite(rb)
        ex = (r - s)[ok]; exb = (rb - sb)[okb]
        diff = diff_ci(ex, ii[ok], exb, base_i[okb])
        row[f"h{h}"] = {"mean_return": float(r[ok].mean()), "spy_same_window": float(s[ok].mean()),
                        "excess_vs_spy": float(ex.mean()),
                        "all_stocks_excess_vs_spy": float(exb.mean()),
                        "edge_over_all_stocks": diff[0], "edge_ci95": [diff[1], diff[2]]}
    und[name] = row
results["underlying"] = und

# ---------- Part 2: modeled option P&L ----------
opt = {}
for name, mask, call in (("calls", call_sig, True), ("puts", put_sig, False)):
    ret, ii, jj, hit, fun = option_trades(mask, call)
    opt[name] = {"screen": summarize(ret, ii, hit), "funnel": fun}
    # baseline: same contract rules and same modeled gates on EVERY stock day, no trend gate
    rb, ib, jb, hb, funb = option_trades(any_day, call)
    opt[name]["all_stock_days"] = summarize(rb, ib, hb)
    opt[name]["edge_vs_all_stock_days"] = list(diff_ci(ret, ii, rb, ib))
    # S&P 500 itself: the same contract on SPY every day
    # periods and regimes
    yr = dates[ii].year
    per = {}
    for lab, lo_, hi_ in (("2016 to 2019", 2016, 2019), ("2020 to 2022", 2020, 2022), ("2023 to 2026", 2023, 2026)):
        m = (yr >= lo_) & (yr <= hi_)
        per[lab] = summarize(ret[m], ii[m], hit[m])
    opt[name]["by_period"] = per
    reg = spy_regime.values[ii]
    opt[name]["by_regime"] = {"spy_above_200d": summarize(ret[reg], ii[reg], hit[reg]),
                              "spy_below_200d": summarize(ret[~reg], ii[~reg], hit[~reg])}
    # sensitivities, fixed in advance
    sens = {}
    for lab, kw in (("dte45", {"dte": 45}), ("iv_premium_1.00", {"ivmult": 1.0}), ("iv_premium_1.30", {"ivmult": 1.30}),
                    ("no_cost", {"half": 0.0}), ("cost_4pct_each_way", {"half": 0.04}), ("no_modeled_gates", {"gates": False})):
        r2, i2, j2, h2, _ = option_trades(mask, call, **kw)
        sens[lab] = summarize(r2, i2, h2)
    opt[name]["sensitivity"] = sens

# SPY benchmark: the same contract on SPY every day (SPY is the S&P 500)
def spy_trades(call):
    global O, C, rv30, hi252
    keepO, keepC, keepR, keepH = O, C, rv30, hi252
    spyrv = np.log(spy_c / spy_c.shift(1)).rolling(30).std() * np.sqrt(252)
    O = pd.DataFrame({"SPY": spy_o}); C = pd.DataFrame({"SPY": spy_c})
    rv30 = pd.DataFrame({"SPY": spyrv}); hi252 = pd.DataFrame({"SPY": spy_c.rolling(252).max()})
    v_ok = spyrv.notna() & hi252["SPY"].notna()
    ii = np.nonzero((v_ok.values) & (np.arange(n) <= last_i))[0]
    jj = np.zeros(len(ii), int)
    out = option_trades(None, call, bench=(ii, jj))
    O, C, rv30, hi252 = keepO, keepC, keepR, keepH
    return out

for name, call in (("calls", True), ("puts", False)):
    r, i, j, h, f = spy_trades(call)
    opt[name]["spy_every_day"] = summarize(r, i, h)
results["options"] = opt

# SPY buy and hold over the whole sample for context
results["spy_buy_and_hold"] = {"total_return": float(spy_c.dropna().iloc[-1] / spy_c.dropna().loc["2016-01-04":].iloc[0] - 1)}

json.dump(results, open("results.json", "w"), indent=2)
print(json.dumps(results, indent=2))
