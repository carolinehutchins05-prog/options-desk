---
layout: default
title: Options Desk
---

<section class="hero">
<p class="eyebrow">Quantitative options research</p>
<h1 class="hero-title">Options Desk</h1>
<p class="hero-sub">A rules based daily screen for single leg calls and puts. Every rule was tested on ten years of S&amp;P 500 data, and every result, pass or fail, is published.</p>
<p class="hero-links"><a href="best-options/">Best options today</a><span>&middot;</span><a href="week-ahead/">Week ahead</a><span>&middot;</span><a href="methodology">Methodology</a><span>&middot;</span><a href="research/">Research</a></p>
<div class="figures">
<div><b>14</b><span>gates every contract must clear</span></div>
<div><b>503</b><span>S&amp;P 500 stocks in the backtest</span></div>
<div><b>10 years</b><span>of price history, 2016 to 2026</span></div>
<div><b>2 runs</b><span>every trading day, 8:30 and 10:00 ET</span></div>
</div>
</section>

<section class="block">
<h2>How it works</h2>
<p class="sub">Three steps, the same every day.</p>
<div class="steps">
<div class="step"><i>1</i><h3>Screen</h3><p>Scan the S&amp;P 500 for stocks with a clear trend, a named catalyst, and no earnings report inside the holding window.</p></div>
<div class="step"><i>2</i><h3>Verify</h3><p>Re grade each idea on live option chains against fourteen gates: spread, open interest, volume, delta, volatility and more.</p></div>
<div class="step"><i>3</i><h3>Publish</h3><p>Post the result with the reason, including every rejection. Most days nothing clears, and the log says so.</p></div>
</div>
</section>

<section class="block">
<h2>What the research found</h2>
<p class="sub">Tested on 503 stocks. The results did not all flatter the idea, and they changed the rules.</p>
<div class="finds">
<div class="find"><b>No edge</b><p><strong>A trend filter alone does not beat the index.</strong>Stocks passing the call trend gate returned 1.02% over 21 days against 1.03% for SPY.</p></div>
<div class="find"><b>3.6%</b><p><strong>The spread decides the outcome.</strong>Modeled calls broke even at a quoted spread near 3.6%, so the rule is 3% or less.</p></div>
<div class="find"><b>Puts lose</b><p><strong>The put side lost in every setting tested.</strong>Puts are tactical only, held for days and never the core idea.</p></div>
</div>
<p class="meta" style="margin-top:14px">Full write up in <a href="research/backtest.html">the backtest</a>. Option prices are modeled, not historical quotes, so treat results as an approximation.</p>
</section>

<section class="block">
<h2>Built with</h2>
<div class="stack"><span>Python</span><span>pandas</span><span>Black Scholes modeling</span><span>Live option chains</span><span>Jekyll</span><span>GitHub Pages</span></div>
</section>

<div class="latest-head"><span class="eyebrow">Latest daily run</span><span class="meta">Premarket Plan, 2026-11-17</span></div>

<div class="report" markdown="1">

# Premarket Calls and Puts, November 17, 2026
Late run, priced on live midday quotes (about 11:58 AM ET). Provisional.

## Today's Catalysts
- **NVDA** reports Q3 after the close tonight. Sector binary for every chip name.
- New Commerce rule on remote access to advanced chips, plus SE Asia export limits (Nov 16).
- **DIS** beat, EPS $1.77 vs $1.68, new 52 week high today.
- **SPY** $730.26 vs its 200 day $732.16. No Core call today.

## TSM PUT: Best Available, Tactical
- Why: remote access chip rule and SE Asia export limits, Nov 16.
- Trend: $357.55, below a falling 50 day ($429), RSI 39.
- Contract: Dec 18 $370 put, mark $28.13, delta 0.55, IV 52.2%
- Liquidity: Spread 3.0%, open interest 7,246, volume today 635, volume to OI 0.09
- Plan: Dec 18 expiry, sell within about 3 to 5 trading days, or at +50%, stop at 50% down. Wait for the NVDA reaction first.
- Verdict: **tactical only**. Trend puts lost on average in our backtest, keep it small.

<aside class="oc" aria-label="TSM contract detail"><div class="oc-title">TSM $370 put, Dec 18, 31 days left, stock $357.55</div><div class="oc-facts"><div><span>Cost to buy</span><b>$2,813</b></div><div><span>Most you can lose</span><b>$2,813</b></div><div><span>Each $1 the stock moves</span><b>about $55</b></div><div><span>Breakeven at expiry</span><b>$341.87 (down 4.4%)</b></div></div><table class="oc-table"><thead><tr><th>Stock moves</th><th>Stock price</th><th>In 1 day</th><th>In 5 days</th></tr></thead><tbody><tr><th scope="row">down 5%</th><td>$339.67</td><td class="up">$1,071</td><td class="up">$959</td></tr><tr><th scope="row">down 3%</th><td>$346.82</td><td class="up">$602</td><td class="up">$478</td></tr><tr><th scope="row">down 1%</th><td>$353.97</td><td class="up">$169</td><td class="up">$37</td></tr><tr><th scope="row">up 1%</th><td>$361.13</td><td class="dn">($225)</td><td class="dn">($365)</td></tr><tr><th scope="row">up 3%</th><td>$368.28</td><td class="dn">($583)</td><td class="dn">($726)</td></tr><tr><th scope="row">up 5%</th><td>$375.43</td><td class="dn">($903)</td><td class="dn">($1,048)</td></tr><tr><th scope="row">up 10%</th><td>$393.31</td><td class="dn">($1,553)</td><td class="dn">($1,690)</td></tr></tbody></table><p class="oc-plan"><b>Plan per contract</b> Stop at $14.06 costs about ($1,407). Target at $42.19 makes about $1,406.</p><p class="oc-foot">Profit or loss for one contract (100 shares), from an options pricing model that holds implied volatility flat and includes time decay. An estimate, not a prediction. Parentheses mean a loss.</p></aside>

## Best Available
- Calls: none passes. Closest is **CVX** Dec 18 $220 call, blocked by a 6.2% spread.
- Puts: **TSM** above. **NOW** Dec 18 $95 put missed on spread (4.2%). **META** Dec 18 $640 put missed on volume (36 today).

## Dropped for spread
- CVX $220C 6.2%, AS $30C 25.5%, NOW $95P 4.2%

## Rejected
- **DIS** call: new 52 week high today.
- **HUM** call: 52 week high Nov 16.
- **AAPL** call: 52 week high Nov 13.
- **XOM** call: below its 50 day.
- **AMD** put: IV 79%.
- **MU** put: IV 81%, size 1 quotes.
- **NVDA**: reports tonight.

Chips are weak into tonight's NVDA print and SPY sits just under its 200 day. A strong NVDA beat would undo the put case overnight.

</div>
