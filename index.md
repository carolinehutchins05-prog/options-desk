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

<div class="latest-head"><span class="eyebrow">Latest daily run</span><span class="meta">Live Verdict, 2026-11-12</span></div>

<div class="report" markdown="1">

# Calls and Puts Verdict, November 12, 2026
Live chain grading at 10:25 ET. Read only research, no trades placed.

## Status
- Unusual Whales logged in. Flow feed not checked; insider pages read.
- SPY $756.52, above its 200 day $728.65, so calls are allowed.
- No contract cleared the Core gates. The Dec 18 monthly is 36 DTE and the Dec 31 chains are dead.

## Best Available
Tactical tier only.

## MSFT CALL: Best Available, Tactical
- Why: holding above its 50 day while chips sell.
- Trend: $524.78, up 0.7%, above a rising 50 day $518.20, RSI 48.
- Contract: Dec 18 $525 call, mark $18.78, delta 0.54, IV 26.9%
- Liquidity: Spread 2.4%, open interest 69,171, volume today 212, volume to OI 0.003
- Plan: Dec 18 expiry, sell within about 3 to 5 trading days, or at +50% ($28.17), stop at 50% down ($9.39).

<aside class="oc" aria-label="MSFT contract detail"><div class="oc-title">MSFT $525 call, Dec 18, 36 days left, stock $524.78</div><div class="oc-facts"><div><span>Cost to buy</span><b>$1,878</b></div><div><span>Most you can lose</span><b>$1,878</b></div><div><span>Each $1 the stock moves</span><b>about $54</b></div><div><span>Breakeven at expiry</span><b>$543.78 (up 3.6%)</b></div></div><table class="oc-table"><thead><tr><th>Stock moves</th><th>Stock price</th><th>In 1 day</th><th>In 5 days</th></tr></thead><tbody><tr><th scope="row">down 5%</th><td>$498.54</td><td class="dn">($1,115)</td><td class="dn">($1,206)</td></tr><tr><th scope="row">down 3%</th><td>$509.04</td><td class="dn">($754)</td><td class="dn">($859)</td></tr><tr><th scope="row">down 1%</th><td>$519.53</td><td class="dn">($295)</td><td class="dn">($408)</td></tr><tr><th scope="row">up 1%</th><td>$530.03</td><td class="up">$264</td><td class="up">$149</td></tr><tr><th scope="row">up 3%</th><td>$540.52</td><td class="up">$919</td><td class="up">$808</td></tr><tr><th scope="row">up 5%</th><td>$551.02</td><td class="up">$1,662</td><td class="up">$1,559</td></tr><tr><th scope="row">up 10%</th><td>$577.26</td><td class="up">$3,823</td><td class="up">$3,751</td></tr></tbody></table><p class="oc-plan"><b>Plan per contract</b> Stop at $9.39 costs about ($939). Target at $28.17 makes about $939.</p><p class="oc-foot">Profit or loss for one contract (100 shares), from an options pricing model that holds implied volatility flat and includes time decay. An estimate, not a prediction. Parentheses mean a loss.</p></aside>

## QQQ PUT: Best Available, Tactical
- Why: Nvidia CEO ouster report and December hike fear; liquid stand in for the chip short.
- Trend: $685.53, down 0.7%, 4.7% below its 50 day $719.04.
- Contract: Dec 18 $685 put, mark $18.88, delta 0.46, IV 24.2%
- Liquidity: Spread 0.8%, open interest 9,469, volume today 248, volume to OI 0.03
- Plan: sell within about 3 trading days, or at +50% ($28.31), stop at 50% down ($9.44). Trend puts lose on average in the backtest, keep it small.

<aside class="oc" aria-label="QQQ contract detail"><div class="oc-title">QQQ $685 put, Dec 18, 36 days left, stock $685.53</div><div class="oc-facts"><div><span>Cost to buy</span><b>$1,888</b></div><div><span>Most you can lose</span><b>$1,888</b></div><div><span>Each $1 the stock moves</span><b>about $46</b></div><div><span>Breakeven at expiry</span><b>$666.12 (down 2.8%)</b></div></div><table class="oc-table"><thead><tr><th>Stock moves</th><th>Stock price</th><th>In 1 day</th><th>In 5 days</th></tr></thead><tbody><tr><th scope="row">down 5%</th><td>$651.25</td><td class="up">$2,014</td><td class="up">$1,943</td></tr><tr><th scope="row">down 3%</th><td>$664.96</td><td class="up">$1,089</td><td class="up">$999</td></tr><tr><th scope="row">down 1%</th><td>$678.67</td><td class="up">$309</td><td class="up">$208</td></tr><tr><th scope="row">up 1%</th><td>$692.39</td><td class="dn">($322)</td><td class="dn">($426)</td></tr><tr><th scope="row">up 3%</th><td>$706.10</td><td class="dn">($812)</td><td class="dn">($910)</td></tr><tr><th scope="row">up 5%</th><td>$719.81</td><td class="dn">($1,175)</td><td class="dn">($1,261)</td></tr><tr><th scope="row">up 10%</th><td>$754.08</td><td class="dn">($1,672)</td><td class="dn">($1,717)</td></tr></tbody></table><p class="oc-plan"><b>Plan per contract</b> Stop at $9.44 costs about ($944). Target at $28.31 makes about $943.</p><p class="oc-foot">Profit or loss for one contract (100 shares), from an options pricing model that holds implied volatility flat and includes time decay. An estimate, not a prediction. Parentheses mean a loss.</p></aside>

## Gapped Past Entry
- **AMD**: up 1.5%, Dec 18 $560 call breakeven 8.1% away at IV 63%.

## Rejected, and why
- **TSLA** call: breakeven 5.6% away.
- **UNH** call: volume 12.
- **NOW** put: breakeven 6.4% away.
- **PLTR** put: breakeven 5.8% away, volume 21.
- **NFLX** put: volume 21.
- **IWM** put: volume 43.
- **NVDA** put: earnings Nov 17 inside the holding window.
- **COHR**, **ROK**, **INTC** calls: below a falling 50 day.

## Dropped for spread
- SMH $500P 4.5%, UNH $400C 4.3%, JNJ $280C 5.5%


</div>
