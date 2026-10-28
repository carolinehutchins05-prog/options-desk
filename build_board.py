#!/usr/bin/env python3
"""Render data/board.json into best-options.html (the Best Options tab).
Usage: build_board.py [data/board.json] [best-options.html]"""
import html, json, sys
from datetime import datetime

src = sys.argv[1] if len(sys.argv) > 1 else "data/board.json"
dst = sys.argv[2] if len(sys.argv) > 2 else "best-options.html"
b = json.load(open(src))
e = html.escape

NAV = [("Best Options", "/options-desk/best-options/"), ("Week Ahead", "/options-desk/week-ahead/"), ("Daily log", "/options-desk/archive/"),
       ("Research", "/options-desk/research/"), ("Methodology", "/options-desk/methodology")]

def usd(x):
    x = round(x)
    return f"${x:,}" if x >= 0 else f"(${-x:,})"

def cls(x):
    return "up" if round(x) > 0 else ("dn" if round(x) < 0 else "")

def money_pct(p):
    return f"+{p}%" if p >= 0 else f"({-p}%)"

def card(r, rank):
    call = r["side"] == "call"
    side = "CALL" if call else "PUT"
    fav = "up" if call else "down"
    earn = {"after": "Earnings after expiry", "unknown": "Earnings date not found, check before buying",
            "before_expiry": f"Earnings {r['earnings']}, before expiry. Sell before it."}.get(r["earnings_flag"], "")
    if r["earnings"].startswith("ETF"):
        earn = "ETF, no earnings report"
    warn = '<span class="tag warn">Earnings before expiry</span>' if r["earnings_flag"] == "before_expiry" else ""
    warn += '<span class="tag warn">Check earnings date</span>' if r["earnings_flag"] == "unknown" else ""
    rows = "".join(
        f'<tr><th scope="row">{"stock " + fav + " " + str(m["move"]) + "%" if m["move"] >= 0 else "stock " + ("down" if call else "up") + " " + str(-m["move"]) + "%"}</th><td>${m["stock"]:,.2f}</td>'
        f'<td class="{cls(m["d1"])}">{usd(m["d1"])}</td><td class="{cls(m["d5"])}">{usd(m["d5"])}</td></tr>' for m in r["table"])
    return f'''<article class="opt {"call" if call else "put"}">
  <div class="opt-top">
    <span class="rank">{rank}</span>
    <div class="who"><b>{e(r["ticker"])}</b><span>{e(r["name"])}</span></div>
    <span class="side {"call" if call else "put"}">{side}</span>
    <div class="contract">{e(r["expiry"])} ${r["strike"]:g} {side.lower()}<small>{r["dte"]} days to expiry</small></div>
  </div>
  <div class="big">
    <div class="ret"><span>If it makes a normal move</span><b>{money_pct(r["ret_sigma_pct"])}</b><em>about {usd(r["usd_sigma"])} per contract, stock {fav} {r["sigma_move_pct"]}% in a week</em></div>
    <div class="facts">
      <div><span>Costs</span><b>${r["cost"]:,}</b></div>
      <div><span>Open interest</span><b>{r["oi"]:,}</b></div>
      <div><span>Volume today</span><b>{r["volume"]:,}</b></div>
      <div><span>Spread</span><b>{r["spread_pct"]}%</b></div>
      <div><span>Delta</span><b>{abs(r["delta"]):.2f}</b></div>
      <div><span>Break even</span><b>{abs(r["breakeven_pct"])}% {"above" if call else "below"}</b></div>
    </div>
  </div>
  <p class="plan"><b>Plan</b> Expiry {e(r["expiry"])}, but sell within about 3 to 5 trading days, or at +50% (${r["target_price"]:.2f}). Stop at ${r["stop_price"]:.2f}, 50% down.</p>
  <div class="tags"><span class="tag">{e(r["trend"])}, RSI {r["rsi"]}</span><span class="tag">IV {r["iv_pct"]}% vs {r["rv_pct"]}% realized</span><span class="tag">{e(earn)}</span>{warn}</div>
  <details><summary>View dollar outcomes</summary>
    <table class="oc-t"><thead><tr><th>Stock moves</th><th>Stock price</th><th>In 1 day</th><th>In 5 days</th></tr></thead><tbody>{rows}</tbody></table>
    <p class="fine">Profit or loss for one contract (100 shares) from an options pricing model with implied volatility held flat, after the spread. Parentheses mean a loss. An estimate, not a prediction.</p>
  </details>
</article>'''

def section(title, sub, items, empty):
    body = "".join(card(r, i + 1) for i, r in enumerate(items)) if items else f'<p class="empty">{e(empty)}</p>'
    return f'<section class="blk"><div class="blk-h"><h2>{e(title)}</h2><p>{e(sub)}</p></div><div class="list">{body}</div></section>'

spy = b["spy"]
regime = (f'S&amp;P 500 (SPY) is <b>above</b> its 200 day average ({spy["spy"]:,} vs {spy["sma200"]:,}), so core calls are on.' if spy["above"]
          else f'S&amp;P 500 (SPY) is <b>below</b> its 200 day average ({spy["spy"]:,} vs {spy["sma200"]:,}), so core calls are off. Tactical ideas only.')
core = section("Core calls", "The strictest list: 45 to 75 days, spread 3% or less, break even within 3%, implied vol under 40%, S&P 500 above its 200 day average.", b["calls_core"],
               "Nothing passes the core rules right now." if spy["above"] else "Core calls are off while the S&P 500 is below its 200 day average.")
tact_c = section("Tactical calls", "Looser on timing and price: 21 to 75 days, spread 4% or less, break even within 5%. For a quick trade.", b["calls_tactical"], "No tactical calls pass right now.")
tact_p = section("Tactical puts", "Stocks below their 50 day average. Puts are tactical only: in the backtest, trend puts lost money on average, so keep them short and small.", b["puts_tactical"], "No puts pass right now.")
nav = "".join(f'<a href="{u}"{" class=on" if t == "Best Options" else ""}>{t}</a>' for t, u in NAV)

page = f'''---
layout: none
permalink: /best-options/
title: Best Options
---
<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1">
<title>Best Options &middot; Options Desk</title>
<meta name="description" content="The most liquid calls and puts ranked by estimated return on a normal move, refreshed each trading day.">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700&display=swap" rel="stylesheet">
<link rel="stylesheet" href="/options-desk/assets/week.css?v={datetime.now().strftime("%Y%m%d%H%M%S")}">
<link rel="stylesheet" href="/options-desk/assets/board.css?v={datetime.now().strftime("%Y%m%d%H%M%S")}">
</head>
<body>
<header class="top"><div class="bar">
  <a class="brand" href="/options-desk/"><span class="logo">OD</span>Options Desk</a>
  <nav>{nav}</nav>
</div></header>
<main class="shell">
  <section class="hero">
    <p class="eyebrow">Best options</p>
    <h1>The best liquid options right now</h1>
    <p class="lede">These are the calls and puts with the most open interest that give the best estimated return for a normal week of movement, after paying the spread. Each one is a longer dated contract with a short plan: buy it, then sell within a few days, or at a 50% gain, or at a 50% loss. Sorted best first.</p>
    <p class="stamp">Built from {b["contracts_scanned"]:,} contracts across {b["tickers_scanned"]} stocks, snapshot {e(b["snapshot_date"])}, updated {e(b["as_of"])}</p>
  </section>
  <div class="regime">{regime}</div>
  {core}{tact_c}{tact_p}
  <section class="how"><h2>How to read this</h2>
    <p><b>Return on a normal move.</b> We take each stock's own recent volatility, scale it to one week, and estimate what the option would be worth if the stock moved that much in the contract's favor, minus the spread you pay going in and out. Options priced cheaply compared with how the stock really moves rank higher.</p>
    <p><b>Open interest</b> is how many contracts are open. Every contract here has at least 2,000 open and 100 traded today, so you can get in and out.</p>
    <p><b>Earnings.</b> Anything reporting inside the next eight days is removed, because the price drop after a report can erase the gain. If a report falls after that but before expiry it is flagged: sell before it.</p>
    <p class="fine"><strong>Not investment advice.</strong> A personal research log. Estimates come from a model, not real fills. Free, delayed quotes can be stale, so check the live chain before any trade.</p>
  </section>
</main>
</body>
</html>
'''
open(dst, "w").write(page)
print("wrote", dst, len(page))
