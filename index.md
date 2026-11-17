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

<div class="latest-head"><span class="eyebrow">Latest daily run</span><span class="meta">Live Verdict, 2026-11-17</span></div>

<div class="report" markdown="1">

# Calls and Puts Verdict, November 17, 2026
Live chain grading at 11:45 AM ET. Read only research, no trades placed.

## Market Gate
- **SPY** $730.16, down 1.3%, below its 200 day ($732.16). **No call clears today.**
- Puts graded as Tactical only. The backtest shows trend puts lose about 6% a trade on average, so keep them small and short.

## SPY PUT: Best Available, Tactical
- Why: SPY broke its 200 day; NVDA reports tonight after its CEO exit
- Trend: 4.4% below the 50 day ($763.82)
- Contract: Dec 18 $730 put, mark $17.54, delta 0.47, IV 22.0%
- Liquidity: Spread 0.7%, open interest 36,355, volume today 7,177, volume to OI 0.20
- Plan: Dec 18 expiry, enter Wednesday only if SPY stays below $740, sell within about 3 to 5 trading days, or at +50%, stop at 50% down.

<aside class="oc" aria-label="SPY contract detail"><div class="oc-title">SPY $730 put, Dec 18, 31 days left, stock $730.16</div><div class="oc-facts"><div><span>Cost to buy</span><b>$1,754</b></div><div><span>Most you can lose</span><b>$1,754</b></div><div><span>Each $1 the stock moves</span><b>about $47</b></div><div><span>Breakeven at expiry</span><b>$712.46 (down 2.4%)</b></div></div><table class="oc-table"><thead><tr><th>Stock moves</th><th>Stock price</th><th>In 1 day</th><th>In 5 days</th></tr></thead><tbody><tr><th scope="row">down 5%</th><td>$693.65</td><td class="up">$2,235</td><td class="up">$2,168</td></tr><tr><th scope="row">down 3%</th><td>$708.26</td><td class="up">$1,199</td><td class="up">$1,106</td></tr><tr><th scope="row">down 1%</th><td>$722.86</td><td class="up">$336</td><td class="up">$227</td></tr><tr><th scope="row">up 1%</th><td>$737.46</td><td class="dn">($344)</td><td class="dn">($456)</td></tr><tr><th scope="row">up 3%</th><td>$752.06</td><td class="dn">($849)</td><td class="dn">($952)</td></tr><tr><th scope="row">up 5%</th><td>$766.67</td><td class="dn">($1,203)</td><td class="dn">($1,288)</td></tr><tr><th scope="row">up 10%</th><td>$803.18</td><td class="dn">($1,627)</td><td class="dn">($1,662)</td></tr></tbody></table><p class="oc-plan"><b>Plan per contract</b> Stop at $8.77 costs about ($877). Target at $26.31 makes about $877.</p><p class="oc-foot">Profit or loss for one contract (100 shares), from an options pricing model that holds implied volatility flat and includes time decay. An estimate, not a prediction. Parentheses mean a loss.</p></aside>

## QQQ PUT: Best Available, Tactical
- Why: Nasdaq 9.0% below its 50 day into the NVDA print and new chip export limits
- Trend: $652.28, falling 50 day $716.72, RSI 38
- Contract: Dec 18 $650 put, mark $22.07, delta 0.45, IV 31.9%
- Liquidity: Spread 0.7%, open interest 52,000, volume today 2,585, volume to OI 0.05
- Plan: Dec 18 expiry, enter Wednesday only if QQQ stays below $662, sell within about 3 to 5 trading days, or at +50%, stop at 50% down.

<aside class="oc" aria-label="QQQ contract detail"><div class="oc-title">QQQ $650 put, Dec 18, 31 days left, stock $652.28</div><div class="oc-facts"><div><span>Cost to buy</span><b>$2,207</b></div><div><span>Most you can lose</span><b>$2,207</b></div><div><span>Each $1 the stock moves</span><b>about $45</b></div><div><span>Breakeven at expiry</span><b>$627.93 (down 3.7%)</b></div></div><table class="oc-table"><thead><tr><th>Stock moves</th><th>Stock price</th><th>In 1 day</th><th>In 5 days</th></tr></thead><tbody><tr><th scope="row">down 5%</th><td>$619.67</td><td class="up">$1,795</td><td class="up">$1,674</td></tr><tr><th scope="row">down 3%</th><td>$632.71</td><td class="up">$977</td><td class="up">$839</td></tr><tr><th scope="row">down 1%</th><td>$645.76</td><td class="up">$273</td><td class="up">$125</td></tr><tr><th scope="row">up 1%</th><td>$658.80</td><td class="dn">($317)</td><td class="dn">($467)</td></tr><tr><th scope="row">up 3%</th><td>$671.85</td><td class="dn">($798)</td><td class="dn">($942)</td></tr><tr><th scope="row">up 5%</th><td>$684.89</td><td class="dn">($1,181)</td><td class="dn">($1,311)</td></tr><tr><th scope="row">up 10%</th><td>$717.51</td><td class="dn">($1,785)</td><td class="dn">($1,871)</td></tr></tbody></table><p class="oc-plan"><b>Plan per contract</b> Stop at $11.04 costs about ($1,103). Target at $33.11 makes about $1,104.</p><p class="oc-foot">Profit or loss for one contract (100 shares), from an options pricing model that holds implied volatility flat and includes time decay. An estimate, not a prediction. Parentheses mean a loss.</p></aside>

## Third put: none passes
- Closest: **NOW** Dec 18 $95 put, break even 5.1% away (limit 5%). Also down 6.9% today, a chase

## Calls: none passes
- Gate: SPY below its 200 day. **AAPL** and **JNJ** pass trend but cannot clear

## Dropped for spread
- XLK $161P 6.0%, KRE $71P 10.6%

## Rejected, and why
- **IWM** Dec 18 $269P: volume today 50
- **META** Dec 18 $615P: open interest 1,207, volume 14
- **SMH** Dec 18 $455P: open interest 911
- **AMZN**: sitting on a flat 50 day
- **NVDA**: reports tonight, inside the holding window
- **SKYD**, **CAT**: below the 50 day despite insider buys

### Corporate
- **SKYD** Gerald Cardinale bought about $500K twice, Nov 11 and Nov 13
- **BRKB** general counsel $250K Nov 12; **WY** director $307K Nov 11
- Standing: **INTC** CEO $9.71M Nov 2, **KMI** Kinder $15M Nov 6, **ROK** CEO $1.55M

SPY broke its 200 day, so the desk is puts only. Wait for the NVDA reaction Wednesday before any entry.

</div>
