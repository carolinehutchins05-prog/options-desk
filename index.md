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

<div class="latest-head"><span class="eyebrow">Latest daily run</span><span class="meta">Live Verdict, 2026-11-13</span></div>

<div class="report" markdown="1">

# Calls and Puts Verdict, November 13, 2026
Live chain grading at 10:23 ET. Read only research, no trades placed.

## Status
- Unusual Whales logged in. Flow feed not checked; insider pages read.
- SPY $748.35, down 1.2%, still above its 200 day $731.62, so calls are allowed.
- No contract cleared the Core gates. The Dec 18 monthly is 35 DTE and the Dec 31 chains are dead.
- Chips broke hard at the open: SMH down 4.8%, QQQ down 2.1%. Energy and staples are green.

## Best Available
Tactical tier only.

## CVX CALL: Best Available, Tactical
- Why: Houthi attacks on Saudi energy sites; oil up 2.6% Thursday.
- Trend: $218.06, up 0.8%, above a rising 50 day $215.31, RSI 47.
- Contract: Dec 18 $220 call, mark $5.88, delta 0.49, IV 23.6%
- Liquidity: Spread 2.6%, open interest 5,537, volume today 216, volume to OI 0.04
- Plan: Dec 18 expiry, sell within about 3 to 5 trading days, or at +50% ($8.82), stop at 50% down ($2.94). Void on a close under $215.31.

<aside class="oc" aria-label="CVX contract detail"><div class="oc-title">CVX $220 call, Dec 18, 35 days left, stock $218.06</div><div class="oc-facts"><div><span>Cost to buy</span><b>$588</b></div><div><span>Most you can lose</span><b>$588</b></div><div><span>Each $1 the stock moves</span><b>about $49</b></div><div><span>Breakeven at expiry</span><b>$225.88 (up 3.6%)</b></div></div><table class="oc-table"><thead><tr><th>Stock moves</th><th>Stock price</th><th>In 1 day</th><th>In 5 days</th></tr></thead><tbody><tr><th scope="row">down 5%</th><td>$207.16</td><td class="dn">($395)</td><td class="dn">($424)</td></tr><tr><th scope="row">down 3%</th><td>$211.52</td><td class="dn">($275)</td><td class="dn">($311)</td></tr><tr><th scope="row">down 1%</th><td>$215.88</td><td class="dn">($110)</td><td class="dn">($151)</td></tr><tr><th scope="row">up 1%</th><td>$220.24</td><td class="up">$102</td><td class="up">$58</td></tr><tr><th scope="row">up 3%</th><td>$224.60</td><td class="up">$361</td><td class="up">$318</td></tr><tr><th scope="row">up 5%</th><td>$228.96</td><td class="up">$663</td><td class="up">$624</td></tr><tr><th scope="row">up 10%</th><td>$239.87</td><td class="up">$1,566</td><td class="up">$1,539</td></tr></tbody></table><p class="oc-plan"><b>Plan per contract</b> Stop at $2.94 costs about ($294). Target at $8.82 makes about $294.</p><p class="oc-foot">Profit or loss for one contract (100 shares), from an options pricing model that holds implied volatility flat and includes time decay. An estimate, not a prediction. Parentheses mean a loss.</p></aside>

## IWM PUT: Best Available, Tactical
- Why: 10 year yield at 5.10% and Fed hike pricing hit small caps hardest.
- Trend: $274.84, down 1.3%, 2.2% below its 50 day $281.12.
- Contract: Dec 18 $275 put, mark $6.79, delta 0.47, IV 21.5%
- Liquidity: Spread 1.3%, open interest 89,680, volume today 365, volume to OI 0.004
- Plan: sell within about 3 to 5 trading days, or at +50% ($10.19), stop at 50% down ($3.40). Trend puts lose on average in the backtest, keep it small.

<aside class="oc" aria-label="IWM contract detail"><div class="oc-title">IWM $275 put, Dec 18, 35 days left, stock $274.84</div><div class="oc-facts"><div><span>Cost to buy</span><b>$679</b></div><div><span>Most you can lose</span><b>$679</b></div><div><span>Each $1 the stock moves</span><b>about $47</b></div><div><span>Breakeven at expiry</span><b>$268.21 (down 2.4%)</b></div></div><table class="oc-table"><thead><tr><th>Stock moves</th><th>Stock price</th><th>In 1 day</th><th>In 5 days</th></tr></thead><tbody><tr><th scope="row">down 5%</th><td>$261.10</td><td class="up">$841</td><td class="up">$819</td></tr><tr><th scope="row">down 3%</th><td>$266.59</td><td class="up">$453</td><td class="up">$422</td></tr><tr><th scope="row">down 1%</th><td>$272.09</td><td class="up">$128</td><td class="up">$92</td></tr><tr><th scope="row">up 1%</th><td>$277.59</td><td class="dn">($129)</td><td class="dn">($166)</td></tr><tr><th scope="row">up 3%</th><td>$283.09</td><td class="dn">($322)</td><td class="dn">($357)</td></tr><tr><th scope="row">up 5%</th><td>$288.58</td><td class="dn">($458)</td><td class="dn">($487)</td></tr><tr><th scope="row">up 10%</th><td>$302.32</td><td class="dn">($626)</td><td class="dn">($638)</td></tr></tbody></table><p class="oc-plan"><b>Plan per contract</b> Stop at $3.40 costs about ($339). Target at $10.19 makes about $340.</p><p class="oc-foot">Profit or loss for one contract (100 shares), from an options pricing model that holds implied volatility flat and includes time decay. An estimate, not a prediction. Parentheses mean a loss.</p></aside>

## QQQ PUT: Best Available, Tactical
- Why: Nvidia CEO exit, Nvidia earnings Nov 17, and 5.10% yields.
- Trend: $673.38, down 2.1%, 6.3% below its 50 day $718.62.
- Contract: Dec 18 $675 put, mark $21.66, delta 0.48, IV 26.6%
- Liquidity: Spread 1.3%, open interest 27,715, volume today 415, volume to OI 0.01
- Plan: enter only on a bounce toward $680, not into a 2% down day. Sell within about 3 days, or at +50% ($32.49), stop at 50% down ($10.83).

<aside class="oc" aria-label="QQQ contract detail"><div class="oc-title">QQQ $675 put, Dec 18, 35 days left, stock $673.38</div><div class="oc-facts"><div><span>Cost to buy</span><b>$2,166</b></div><div><span>Most you can lose</span><b>$2,166</b></div><div><span>Each $1 the stock moves</span><b>about $48</b></div><div><span>Breakeven at expiry</span><b>$653.34 (down 3.0%)</b></div></div><table class="oc-table"><thead><tr><th>Stock moves</th><th>Stock price</th><th>In 1 day</th><th>In 5 days</th></tr></thead><tbody><tr><th scope="row">down 5%</th><td>$639.71</td><td class="up">$1,990</td><td class="up">$1,907</td></tr><tr><th scope="row">down 3%</th><td>$653.18</td><td class="up">$1,085</td><td class="up">$983</td></tr><tr><th scope="row">down 1%</th><td>$666.65</td><td class="up">$310</td><td class="up">$196</td></tr><tr><th scope="row">up 1%</th><td>$680.11</td><td class="dn">($333)</td><td class="dn">($451)</td></tr><tr><th scope="row">up 3%</th><td>$693.58</td><td class="dn">($848)</td><td class="dn">($962)</td></tr><tr><th scope="row">up 5%</th><td>$707.05</td><td class="dn">($1,246)</td><td class="dn">($1,348)</td></tr><tr><th scope="row">up 10%</th><td>$740.72</td><td class="dn">($1,837)</td><td class="dn">($1,899)</td></tr></tbody></table><p class="oc-plan"><b>Plan per contract</b> Stop at $10.83 costs about ($1,083). Target at $32.49 makes about $1,083.</p><p class="oc-foot">Profit or loss for one contract (100 shares), from an options pricing model that holds implied volatility flat and includes time decay. An estimate, not a prediction. Parentheses mean a loss.</p></aside>

## Gapped Past Entry
- None gapped. Premarket names XOM and NOW lost their liquidity instead, see below.

## Rejected, and why
- **NFLX** put: volume 81, under 100. Closest miss.
- **PLTR** put: breakeven 6.2% away.
- **AMAT** put: volume 5, IV 59%.
- **XLE**, **GLD**, **XLC** calls: below their 50 day.
- Third call: none passes. Closest blocked was XOM, on spread.

## Dropped for spread
- XOM $170C 5.2%, NOW $100P 4.4%, XLK $170P 8.0%, SMH $475P 4.9%, CSCO $95P 6.8%


</div>
