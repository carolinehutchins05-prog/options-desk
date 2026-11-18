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

<div class="latest-head"><span class="eyebrow">Latest daily run</span><span class="meta">Premarket Plan, 2026-11-18</span></div>

<div class="report" markdown="1">

# Premarket Calls and Puts, November 18, 2026
Provisional plan on opening minute quotes. The 10:00 AM run confirms on live chains.

## Market
- SPY closed $732.44 against its 200 day of $732.34, above by 0.01%.
- Core calls are allowed, but only just.

## META PUT: Best Available, Tactical
- Why: trades under its 50 day. No dated catalyst, and trend puts lost money on average in the backtest.
- Trend: $620 vs 50 day $680, RSI 42.
- Contract: Dec 18 $620 put, mark $30.78, delta 0.48, IV 43.4%
- Liquidity: Spread 2.1%, open interest 2,421, volume today 0 in the first minute, volume to OI 0.00
- Plan: Dec 18 expiry, sell within about 3 to 5 trading days, or at +50%, stop at 50% down.

<aside class="oc" aria-label="META contract detail"><div class="oc-title">META $620 put, Dec 18, 30 days left, stock $620.00</div><div class="oc-facts"><div><span>Cost to buy</span><b>$3,078</b></div><div><span>Most you can lose</span><b>$3,078</b></div><div><span>Each $1 the stock moves</span><b>about $48</b></div><div><span>Breakeven at expiry</span><b>$589.22 (down 5.0%)</b></div></div><table class="oc-table"><thead><tr><th>Stock moves</th><th>Stock price</th><th>In 1 day</th><th>In 5 days</th></tr></thead><tbody><tr><th scope="row">down 5%</th><td>$589.00</td><td class="up">$1,638</td><td class="up">$1,455</td></tr><tr><th scope="row">down 3%</th><td>$601.40</td><td class="up">$903</td><td class="up">$705</td></tr><tr><th scope="row">down 1%</th><td>$613.80</td><td class="up">$248</td><td class="up">$41</td></tr><tr><th scope="row">up 1%</th><td>$626.20</td><td class="dn">($328)</td><td class="dn">($538)</td></tr><tr><th scope="row">up 3%</th><td>$638.60</td><td class="dn">($829)</td><td class="dn">($1,036)</td></tr><tr><th scope="row">up 5%</th><td>$651.00</td><td class="dn">($1,257)</td><td class="dn">($1,456)</td></tr><tr><th scope="row">up 10%</th><td>$682.00</td><td class="dn">($2,051)</td><td class="dn">($2,214)</td></tr></tbody></table><p class="oc-plan"><b>Plan per contract</b> Stop at $15.39 costs about ($1,539). Target at $46.17 makes about $1,539.</p><p class="oc-foot">Profit or loss for one contract (100 shares), from an options pricing model that holds implied volatility flat and includes time decay. An estimate, not a prediction. Parentheses mean a loss.</p></aside>

## Calls
- None pass. Closest was LOW Jan $210 call, open interest 1,159 below the 2,000 floor.

## Dropped for spread
- LOW $210C 16%, JD $25P 18%, NOW $95P 5.3%, JNJ $280C 15%

## Rejected
- DIS call: 52 week high on Nov 17.
- AAPL call: 52 week high on Nov 13.
- NVDA: under a falling 50 day, RSI 22 after a beat.
- TGT call: 50 day rolling over.
- CVX, XOM, UNH, WFC calls: below the 50 day.
- SQM put: open interest under 100.

SPY is sitting on its 200 day. A close below $732 turns off calls.

</div>
