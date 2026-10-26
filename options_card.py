#!/usr/bin/env python3
"""Stdin to stdout. Turn each hidden contract comment into a "view more" card with
per contract dollar outcomes for stock moves.

Usage: options_card.py YYYY-MM-DD < note.md > note_with_cards.md

A candidate carries one line under its heading:
<!--opt {"t":"MSFT","side":"call","K":430,"exp":"2026-11-20","mark":6.95,"S":418.2,"iv":28.8,"delta":0.58,"entry":6.95,"stop":4.50,"target":10.40}-->
mark, entry, stop, target are option prices per share. S is the stock price, iv is a percent.
entry, stop and target are optional. A malformed or incomplete comment is dropped, never fatal.
Everything is for ONE contract (100 shares). No position or sizing data is ever used."""
import json, math, re, sys
from datetime import date, datetime

R = 0.04  # risk free rate, near the Fed funds target
MOVES = [-5, -3, -1, 1, 3, 5, 10]
RUN = datetime.strptime(sys.argv[1], "%Y-%m-%d").date() if len(sys.argv) > 1 else date.today()

def N(x):
    return 0.5 * (1 + math.erf(x / math.sqrt(2)))

def bs(S, K, T, v, call):
    if T <= 0 or v <= 0:
        return max(S - K, 0) if call else max(K - S, 0)
    d1 = (math.log(S / K) + (R + v * v / 2) * T) / (v * math.sqrt(T))
    d2 = d1 - v * math.sqrt(T)
    if call:
        return S * N(d1) - K * math.exp(-R * T) * N(d2)
    return K * math.exp(-R * T) * N(-d2) - S * N(-d1)

def delta(S, K, T, v, call):
    d1 = (math.log(S / K) + (R + v * v / 2) * T) / (v * math.sqrt(T))
    return N(d1) if call else N(d1) - 1

def solve_iv(S, K, T, mark, call, fallback):
    """Implied vol that reproduces the quoted mark, so the table starts at zero."""
    lo, hi = 0.01, 5.0
    if not (bs(S, K, T, lo, call) <= mark <= bs(S, K, T, hi, call)):
        return fallback
    for _ in range(80):
        mid = (lo + hi) / 2
        if bs(S, K, T, mid, call) < mark:
            lo = mid
        else:
            hi = mid
    return (lo + hi) / 2

def usd(x):
    x = round(x)
    return f"${x:,}" if x >= 0 else f"(${-x:,})"

def cls(x):
    return "up" if round(x) > 0 else ("dn" if round(x) < 0 else "")

def card(c):
    t = str(c["t"]).upper()
    side = str(c["side"]).lower()
    if not re.fullmatch(r"[A-Z.]{1,6}", t) or side not in ("call", "put"):
        return ""
    call = side == "call"
    K, mark, S = float(c["K"]), float(c["mark"]), float(c["S"])
    expd = datetime.strptime(c["exp"], "%Y-%m-%d").date()
    dte = (expd - RUN).days
    if min(K, mark, S) <= 0 or dte < 1:
        return ""
    T = dte / 365
    v = solve_iv(S, K, T, mark, call, float(c.get("iv", 40)) / 100)
    cost = mark * 100
    d = float(c["delta"]) if c.get("delta") else delta(S, K, T, v, call)
    be = K + mark if call else K - mark
    be_pct = (be / S - 1) * 100
    horizons = [(1, "In 1 day")] + ([(5, "In 5 days")] if dte > 5 else [])

    rows = ""
    for m in MOVES:
        s2 = S * (1 + m / 100)
        cells = ""
        for h, _ in horizons:
            pl = (bs(s2, K, max(T - h / 365, 1e-9), v, call) - mark) * 100
            cells += f'<td class="{cls(pl)}">{usd(pl)}</td>'
        label = f"down {-m}%" if m < 0 else f"up {m}%"
        rows += f'<tr><th scope="row">{label}</th><td>${s2:,.2f}</td>{cells}</tr>'
    head = "".join(f"<th>{lbl}</th>" for _, lbl in horizons)

    plan = ""
    if all(k in c for k in ("entry", "stop", "target")):
        e, st, tg = float(c["entry"]), float(c["stop"]), float(c["target"])
        plan = (f'<p class="oc-plan"><b>Plan per contract</b> Stop at ${st:.2f} costs about {usd((st - e) * 100)}. '
                f'Target at ${tg:.2f} makes about {usd((tg - e) * 100)}.</p>')

    facts = (
        f'<div class="oc-facts">'
        f'<div><span>Cost to buy</span><b>{usd(cost)}</b></div>'
        f'<div><span>Most you can lose</span><b>{usd(cost)}</b></div>'
        f'<div><span>Each $1 the stock moves</span><b>about {usd(abs(d) * 100)}</b></div>'
        f'<div><span>Breakeven at expiry</span><b>${be:,.2f} ({"up" if be_pct >= 0 else "down"} {abs(be_pct):.1f}%)</b></div>'
        f'</div>')

    return (f'<aside class="oc" aria-label="{t} contract detail">'
            f'<div class="oc-title">{t} ${K:g} {side}, {expd.strftime("%b %-d")}, {dte} days left, stock ${S:,.2f}</div>'
            f'{facts}'
            f'<table class="oc-table"><thead><tr><th>Stock moves</th><th>Stock price</th>{head}</tr></thead><tbody>{rows}</tbody></table>'
            f'{plan}'
            f'<p class="oc-foot">Profit or loss for one contract (100 shares), from an options pricing model that holds implied volatility flat and includes time decay. An estimate, not a prediction. Parentheses mean a loss.</p>'
            f'</aside>')

def repl(m):
    try:
        html = card(json.loads(m.group(1)))
    except Exception:
        html = ""
    return f"\n{html}\n" if html else ""

text = re.sub(r"<!--\s*opt\s+(\{.*?\})\s*-->", repl, sys.stdin.read())
sys.stdout.write(re.sub(r"\n{3,}", "\n\n", text))
