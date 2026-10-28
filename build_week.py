#!/usr/bin/env python3
"""Render data/week.json into week-ahead.html, the dark dashboard page.
Usage: build_week.py [data/week.json] [week-ahead.html]"""
import html, json, sys
from datetime import datetime
from zoneinfo import ZoneInfo

src = sys.argv[1] if len(sys.argv) > 1 else "data/week.json"
dst = sys.argv[2] if len(sys.argv) > 2 else "week-ahead.html"
d = json.load(open(src))
e = html.escape
stamp = datetime.now(ZoneInfo("America/New_York")).strftime("%a %b %-d, %-I:%M %p ET")

NAV = [("Best Options", "/options-desk/best-options/"), ("Week Ahead", "/options-desk/week-ahead/"), ("Daily log", "/options-desk/archive/"),
       ("Research", "/options-desk/research/"), ("Methodology", "/options-desk/methodology")]

def chip(label, val):
    return f'<span class="chip"><b>{e(label)}</b>{e(val)}</span>' if val else ""

def macro(m):
    chips = chip("Consensus", m.get("cons", "")) + chip("Prior", m.get("prior", ""))
    return f'''<article class="item imp-{e(m["imp"])}">
  <div class="item-head"><span class="time">{e(m["time"])}</span><span class="imp-tag">{ {"high":"High impact","med":"Medium","low":"Low"}[m["imp"]] }</span></div>
  <h4>{e(m["name"])}</h4>
  <div class="chips">{chips}</div>
  <p class="note">{e(m["note"])}</p>
  <div class="react"><span class="react-k">How markets could react</span><p>{e(m["react"])}</p></div>
</article>'''

def tile(x):
    cls = "tile star" if x.get("star") else "tile"
    if x.get("actual"):
        try:
            beat = float(x["actual"]) >= float(x["eps"])
        except ValueError:
            beat = False
        sub = f'<span class="eps {"beat" if beat else "miss"}">Reported {e(x["actual"])} vs {e(x["eps"])} est</span>'
    else:
        sub = f'<span class="eps">Est {e(x["eps"])}</span>'
    return f'<div class="{cls}"><b>{e(x["t"])}</b><span class="co">{e(x["n"])}</span>{sub}</div>'

def group(title, items):
    if not items:
        return ""
    return f'<h5>{title} <i>{len(items)}</i></h5><div class="tiles">{"".join(tile(x) for x in items)}</div>'

days = []
for day in d["days"]:
    n_e = len(day.get("am", [])) + len(day.get("pm", []))
    n_m = len(day["macro"])
    earn = group("Before the open", day.get("am", [])) + group("After the close", day.get("pm", [])) or '<p class="empty">No notable reports.</p>'
    days.append(f'''<section class="day" id="{e(day["key"])}" data-day="{e(day["key"])}">
  <header class="day-head"><h3>{e(day["label"])}<span>{e(day["date"])}</span></h3>
    <div class="counts"><em>{n_m} macro</em><em>{n_e} earnings</em></div></header>
  <div class="day-grid">
    <div class="col"><h2 class="col-t">Economic news</h2>{"".join(macro(m) for m in day["macro"])}</div>
    <div class="col"><h2 class="col-t">Earnings</h2>{earn}</div>
  </div>
</section>''')

stats = "".join(f'<div class="stat"><span>{e(s["label"])}</span><b>{e(s["value"])}</b><em>{e(s["sub"])}</em></div>' for s in d["stats"])
spot = "".join(f'''<div class="spot"><div class="spot-top"><b>{e(s["ticker"])}</b><span>{e(s["name"])}</span></div>
  <p class="when">{e(s["when"])}</p>
  <div class="chips">{chip("EPS est", s["eps"])}{chip("Revenue est", s["rev"])}</div>
  <p class="note">{e(s["watch"])}</p></div>''' for s in d["spotlight"])
tabs = '<button class="tab on" data-f="all" aria-pressed="true">Full week</button>' + "".join(
    f'<button class="tab" data-f="{e(x["key"])}" aria-pressed="false">{e(x["short"])}<small>{e(x["date"])}</small></button>' for x in d["days"])
nav = "".join(f'<a href="{u}"{" class=on" if t == "Week Ahead" else ""}>{t}</a>' for t, u in NAV)
notes = "".join(f"<p>{e(n)}</p>" for n in d["notes"])
h = d["headline"]

page = f'''---
layout: none
permalink: /week-ahead/
title: Week Ahead
---
<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1">
<title>Week Ahead &middot; Options Desk</title>
<meta name="description" content="This week's economic releases, earnings reports and how the market could react.">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700&display=swap" rel="stylesheet">
<link rel="stylesheet" href="/options-desk/assets/week.css?v={datetime.now().strftime("%Y%m%d%H%M%S")}">
</head>
<body>
<header class="top"><div class="bar">
  <a class="brand" href="/options-desk/"><span class="logo">OD</span>Options Desk</a>
  <nav>{nav}</nav>
</div></header>
<main class="shell">
  <section class="hero">
    <p class="eyebrow">Week ahead</p>
    <h1>{e(d["week_label"])}</h1>
    <p class="lede">{e(d["summary"])}</p>
    <p class="stamp">Updated {e(stamp)}</p>
  </section>
  <section class="stats">{stats}</section>
  <section class="headline"><span class="kick">{e(h["kicker"])}</span><h2>{e(h["title"])}</h2><p>{e(h["body"])}</p></section>
  <section><h2 class="sec">Megacap reports to watch</h2><div class="spots">{spot}</div></section>
  <div class="tabs" role="group" aria-label="Filter by day">{tabs}</div>
  <div class="days">{"".join(days)}</div>
  <footer class="foot">{notes}<p><strong>Not investment advice.</strong> A personal research log. No position, account or portfolio data is published here.</p></footer>
</main>
<script>
(function(){{
  var tabs=[].slice.call(document.querySelectorAll('.tab')), days=[].slice.call(document.querySelectorAll('.day'));
  function show(f){{
    tabs.forEach(function(t){{var on=t.dataset.f===f;t.classList.toggle('on',on);t.setAttribute('aria-pressed',on)}});
    days.forEach(function(s){{s.hidden=!(f==='all'||s.dataset.day===f)}});
  }}
  tabs.forEach(function(t){{t.addEventListener('click',function(){{show(t.dataset.f)}})}});
  try{{
    var k=['sun','mon','tue','wed','thu','fri','sat'][new Date(new Date().toLocaleString('en-US',{{timeZone:'America/New_York'}})).getDay()];
    var t=tabs.filter(function(x){{return x.dataset.f===k}})[0]; if(t) t.classList.add('today');
  }}catch(e){{}}
}})();
</script>
</body>
</html>
'''
open(dst, "w").write(page)
print("wrote", dst, len(page), "bytes")
