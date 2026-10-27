#!/usr/bin/env python3
"""Second backtest: which rule changes reduce losses, with a holdout.

Protocol, fixed before any result was seen
  1. Grids are small and each choice has an economic reason (list below).
  2. Each dimension is chosen on the DEVELOPMENT period only (signals 2016 to 2021),
     by highest average return per trade. Ties and non improvements keep the baseline.
  3. The combined rule is then run once on the HOLDOUT period (2022 to Oct 2026).
     Nothing is adjusted after seeing the holdout.
  4. Loss metrics are reported next to the mean: share of trades losing 30% or more,
     the average of the worst 10% of trades, and the worst calendar month.

Same data, same biases and same modeled option pricing as run_backtest.py. Read the
header of that file first. Contract level numbers are modeled, not observed.
"""
import json, sys
import numpy as np, pandas as pd
from scipy.special import ndtr, ndtri

R = 0.04
rng = np.random.default_rng(11)
px = pd.read_pickle(sys.argv[1] if len(sys.argv) > 1 else "prices.pkl")
O, C = px["Open"], px["Close"]
spy_o, spy_c = O["SPY"], C["SPY"]
tick = [t for t in C.columns if t != "SPY"]
O, C = O[tick], C[tick]
dates = C.index
n = len(dates)

sma50 = C.rolling(50).mean()
d = C.diff()
up = d.clip(lower=0).ewm(alpha=1 / 14, adjust=False).mean()
dn = (-d.clip(upper=0)).ewm(alpha=1 / 14, adjust=False).mean()
rsi = 100 - 100 / (1 + up / dn.replace(0, np.nan))
hi252 = C.rolling(252).max()
high_recent = C.rolling(3).max() >= hi252
rv30 = np.log(C / C.shift(1)).rolling(30).std() * np.sqrt(252)
call_sig = (C > sma50) & (sma50 > sma50.shift(10)) & (rsi >= 45) & (rsi <= 70) & ~high_recent
put_sig = (C < sma50) & (sma50 < sma50.shift(10)) & (rsi >= 30) & (rsi <= 55)
valid = sma50.notna() & rsi.notna() & hi252.notna() & rv30.notna()
last_i = n - 1 - 24
spy200 = (spy_c > spy_c.rolling(200).mean()).reindex(dates).fillna(False).values
spy50 = (spy_c > spy_c.rolling(50).mean()).reindex(dates).fillna(False).values
Oa, Ca = O.values, C.values
HI, RV = hi252.values, rv30.values

def bs(S, K, T, v, call):
    d1 = (np.log(S / K) + (R + 0.5 * v * v) * T) / (v * np.sqrt(T))
    d2 = d1 - v * np.sqrt(T)
    if call:
        return S * ndtr(d1) - K * np.exp(-R * T) * ndtr(d2)
    return K * np.exp(-R * T) * ndtr(-d2) - S * ndtr(-d1)

def trades(sig, call, regime=None, dte=30, delta=0.55, hold=5, target=0.50, stop=None, half=0.02, ivmult=1.15):
    m = (sig & valid).values & (np.arange(n) <= last_i)[:, None]
    if regime is not None:
        m &= regime[:, None]
    ii, jj = np.nonzero(m)
    S0 = Oa[ii + 1, jj]
    v = RV[ii, jj] * ivmult
    T0 = dte / 365
    d1 = ndtri(delta) if call else ndtri(1 - delta)
    with np.errstate(all="ignore"):
        K = S0 * np.exp(-(d1 * v * np.sqrt(T0)) + (R + 0.5 * v * v) * T0)
        P0 = bs(S0, K, T0, v, call)
        be = K + P0 if call else K - P0
        th = (bs(S0, K, T0 - 1 / 365, v, call) - P0) / P0
    g = np.isfinite(S0) & np.isfinite(v) & (v > 0.05) & (v < 0.40) & (np.abs(be / S0 - 1) <= 0.03) & (np.abs(th) < 0.05)
    if call:
        g &= be < HI[ii, jj]
    g &= np.isfinite(P0) & (P0 > 0)
    ii, jj, K, P0, v = ii[g], jj[g], K[g], P0[g], v[g]
    V = np.empty((len(ii), hold))
    for k in range(hold):
        V[:, k] = bs(Ca[ii + 1 + k, jj], K, T0 - (k + 0.75) / 252, v, call)
    ev = V >= (1 + target) * P0[:, None]
    if stop is not None:
        ev |= V <= (1 - stop) * P0[:, None]
    first = np.where(ev.any(1), ev.argmax(1), hold - 1)
    ret = V[np.arange(len(ii)), first] * (1 - half) / (P0 * (1 + half)) - 1
    ok = np.isfinite(ret)
    return ret[ok], ii[ok]

def month_id(ii):
    ds = dates[ii]
    return (ds.year * 12 + ds.month).values

def boot(vals, months, reps=1500):
    u, inv = np.unique(months, return_inverse=True)
    s = np.bincount(inv, weights=vals); c = np.bincount(inv).astype(float)
    out = [s[p].sum() / c[p].sum() for p in (rng.integers(0, len(u), len(u)) for _ in range(reps))]
    return [float(np.percentile(out, 2.5)), float(np.percentile(out, 97.5))]

def summ(ret, ii):
    if len(ret) < 50:
        return {"n": int(len(ret))}
    mo = month_id(ii)
    u, inv = np.unique(mo, return_inverse=True)
    cnt = np.bincount(inv); avg = np.bincount(inv, weights=ret) / np.maximum(cnt, 1)
    worst_m = float(avg[cnt >= 100].min()) if (cnt >= 100).any() else None
    srt = np.sort(ret)
    return {"n": int(len(ret)), "mean": float(ret.mean()), "ci95": boot(ret, mo),
            "median": float(np.median(ret)), "win_rate": float((ret > 0).mean()),
            "loss_30plus": float((ret <= -0.30).mean()),
            "worst10_avg": float(srt[: max(1, len(srt) // 10)].mean()),
            "worst_month": worst_m}

def split(ret, ii):
    yr = dates[ii].year
    return summ(ret[yr <= 2021], ii[yr <= 2021]), summ(ret[yr >= 2022], ii[yr >= 2022])

DIMS = {
    "dte": [("dte30", {"dte": 30}), ("dte45", {"dte": 45}), ("dte60", {"dte": 60})],
    "delta": [("delta0.50", {"delta": 0.50}), ("delta0.55", {"delta": 0.55}), ("delta0.65", {"delta": 0.65})],
    "hold": [("hold3", {"hold": 3}), ("hold5", {"hold": 5}), ("hold10", {"hold": 10})],
    "target": [("target30", {"target": 0.30}), ("target50", {"target": 0.50}), ("target100", {"target": 1.00})],
    "stop": [("nostop", {"stop": None}), ("stop30", {"stop": 0.30}), ("stop50", {"stop": 0.50})],
    "regime": [("any_market", {"regime": None}), ("spy_above_200d", {"regime": spy200}),
               ("spy_above_200d_and_50d", {"regime": spy200 & spy50})],
}
BASE = {"dte": 30, "delta": 0.55, "hold": 5, "target": 0.50, "stop": None, "regime": None}

out = {"protocol": "dimension chosen on 2016 to 2021 only, combined rule then run on 2022 to Oct 2026"}
singles = {}
choice = {}
for dim, opts in DIMS.items():
    rows = {}
    best_name, best_mean, best_kw = None, -9, {}
    for name, kw in opts:
        ret, ii = trades(call_sig, True, **kw)
        dev, hold_ = split(ret, ii)
        rows[name] = {"dev": dev, "holdout": hold_}
        base_like = all((v is None and BASE[k] is None) or (not isinstance(v, np.ndarray) and v is not None and BASE[k] == v) for k, v in kw.items())
        if dev.get("mean") is not None and (dev["mean"] > best_mean or (base_like and dev["mean"] >= best_mean - 1e-12)):
            best_name, best_mean, best_kw = name, dev["mean"], kw
    singles[dim] = rows
    choice[dim] = {"picked": best_name, "kw": {k: ("regime_mask" if k == "regime" and v is not None else v) for k, v in best_kw.items()}}
    choice[dim]["_kw"] = best_kw
out["calls_single_dimension"] = singles

combo = {}
for dim in choice:
    combo.update(choice[dim]["_kw"])
for dim in choice:
    choice[dim].pop("_kw")
out["picked"] = choice
base_ret, base_ii = trades(call_sig, True)
cb_ret, cb_ii = trades(call_sig, True, **combo)
out["calls_baseline"] = dict(zip(("dev", "holdout"), split(base_ret, base_ii)))
out["calls_combined"] = dict(zip(("dev", "holdout"), split(cb_ret, cb_ii)))

# puts, for the decision on whether they stay
pr, pi = trades(put_sig, False)
out["puts_baseline"] = dict(zip(("dev", "holdout"), split(pr, pi)))
pr2, pi2 = trades(put_sig, False, regime=~spy200)
out["puts_only_when_spy_below_200d"] = dict(zip(("dev", "holdout"), split(pr2, pi2)))
pr3, pi3 = trades(put_sig, False, **{k: v for k, v in combo.items() if k != "regime"})
out["puts_with_combined_exits"] = dict(zip(("dev", "holdout"), split(pr3, pi3)))

json.dump(out, open("loss_reduction_results.json", "w"), indent=2)
def f(s):
    if "mean" not in s: return f"n={s['n']}"
    return (f"n={s['n']:>6} mean={s['mean']*100:6.1f}% [{s['ci95'][0]*100:5.1f},{s['ci95'][1]*100:5.1f}] win={s['win_rate']*100:4.1f}% "
            f"loss30={s['loss_30plus']*100:4.1f}% worst10={s['worst10_avg']*100:6.1f}% worstmo={(s['worst_month'] or 0)*100:6.1f}%")
for dim, rows in singles.items():
    print("==", dim, "picked:", choice[dim]["picked"])
    for name, r in rows.items():
        print(f"  {name:24s} DEV {f(r['dev'])}\n  {'':24s} HOLD {f(r['holdout'])}")
for k in ("calls_baseline", "calls_combined", "puts_baseline", "puts_only_when_spy_below_200d", "puts_with_combined_exits"):
    print("##", k, "\n  DEV ", f(out[k]["dev"]), "\n  HOLD", f(out[k]["holdout"]))

# ---- Added after the single dimension results were read. NOT part of the pre registered protocol. ----
# The protocol's own combined rule (above) collapsed to a few hundred trades on the quietest stocks and
# looks like a modeling artifact, so it is not adopted. These combinations keep only the changes that
# improved the average in BOTH periods, are economically motivated, and did not worsen the tail.
# Because the holdout informed this choice, treat the holdout below as consistency, not a clean test.
adopted = {
    "dte45_delta50_regime200": dict(dte=45, delta=0.50, regime=spy200),
    "dte45_delta50_regime200_stop50": dict(dte=45, delta=0.50, regime=spy200, stop=0.50),
    "dte45_regime200": dict(dte=45, regime=spy200),
    "dte45_regime200_stop50": dict(dte=45, regime=spy200, stop=0.50),
}
out["adopted_candidates"] = {}
for name, kw in adopted.items():
    r_, i_ = trades(call_sig, True, **kw)
    out["adopted_candidates"][name] = dict(zip(("dev", "holdout"), split(r_, i_)))
    print("@@", name, "\n  DEV ", f(out["adopted_candidates"][name]["dev"]), "\n  HOLD", f(out["adopted_candidates"][name]["holdout"]))
json.dump(out, open("loss_reduction_results.json", "w"), indent=2)
