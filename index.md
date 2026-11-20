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

<div class="latest-head"><span class="eyebrow">Latest daily run</span><span class="meta">Live Verdict, 2026-11-20</span></div>

<div class="report" markdown="1">

# Calls and Puts Verdict, November 20, 2026
Live chain grading at 3:34 PM ET, a late run. Read only research, no trades placed.

## Market
- **SPY** 692.97, down 3.2%, 5.1% under its 200 day. No core call clears today.
- **QQQ** down 5.1%, **XLK** down 6.8%. Chips led lower after NVDA earnings.

## Best Available

## QQQ PUT: Best Available, Tactical
- Why: chip led flush, QQQ 14.1% under a falling 50 day.
- Contract: Dec 18 $610 put, mark $26.78, delta 0.47, IV 41.0%
- Liquidity: Spread 0.9%, open interest 53,963, volume today 14,058, volume to OI 0.26
- Plan: Dec 18 expiry, enter only on a failed bounce near 625, sell within about 3 to 5 trading days, or at +50%, stop at 50% down.
- Verdict: **wait for the bounce**. Trend puts lose on average in the backtest, keep it small.

<aside class="oc" aria-label="QQQ contract detail"><div class="oc-title">QQQ $610 put, Dec 18, 28 days left, stock $612.22</div><div class="oc-facts"><div><span>Cost to buy</span><b>$2,678</b></div><div><span>Most you can lose</span><b>$2,678</b></div><div><span>Each $1 the stock moves</span><b>about $47</b></div><div><span>Breakeven at expiry</span><b>$583.22 (down 4.7%)</b></div></div><table class="oc-table"><thead><tr><th>Stock moves</th><th>Stock price</th><th>In 1 day</th><th>In 5 days</th></tr></thead><tbody><tr><th scope="row">down 5%</th><td>$581.61</td><td class="up">$1,608</td><td class="up">$1,431</td></tr><tr><th scope="row">down 3%</th><td>$593.85</td><td class="up">$881</td><td class="up">$688</td></tr><tr><th scope="row">down 1%</th><td>$606.10</td><td class="up">$240</td><td class="up">$38</td></tr><tr><th scope="row">up 1%</th><td>$618.34</td><td class="dn">($316)</td><td class="dn">($520)</td></tr><tr><th scope="row">up 3%</th><td>$630.59</td><td class="dn">($791)</td><td class="dn">($990)</td></tr><tr><th scope="row">up 5%</th><td>$642.83</td><td class="dn">($1,190)</td><td class="dn">($1,378)</td></tr><tr><th scope="row">up 10%</th><td>$673.44</td><td class="dn">($1,901)</td><td class="dn">($2,046)</td></tr></tbody></table><p class="oc-plan"><b>Plan per contract</b> Stop at $13.39 costs about ($1,339). Target at $40.17 makes about $1,339.</p><p class="oc-foot">Profit or loss for one contract (100 shares), from an options pricing model that holds implied volatility flat and includes time decay. An estimate, not a prediction. Parentheses mean a loss.</p></aside>

## MSFT PUT: Best Available, Tactical
- Why: megacap software sold with AI capex names, no earnings until late January.
- Trend: 484.88, 6.8% under its 50 day, RSI 39.
- Contract: Dec 18 $485 put, mark $22.15, delta 0.48, IV 41.1%
- Liquidity: Spread 2.3%, open interest 4,609, volume today 1,563, volume to OI 0.34
- Plan: Dec 18 expiry, enter on a failed bounce under 498, sell within about 3 to 5 trading days, or at +50%, stop at 50% down.

<aside class="oc" aria-label="MSFT contract detail"><div class="oc-title">MSFT $485 put, Dec 18, 28 days left, stock $484.88</div><div class="oc-facts"><div><span>Cost to buy</span><b>$2,215</b></div><div><span>Most you can lose</span><b>$2,215</b></div><div><span>Each $1 the stock moves</span><b>about $48</b></div><div><span>Breakeven at expiry</span><b>$462.85 (down 4.5%)</b></div></div><table class="oc-table"><thead><tr><th>Stock moves</th><th>Stock price</th><th>In 1 day</th><th>In 5 days</th></tr></thead><tbody><tr><th scope="row">down 5%</th><td>$460.64</td><td class="up">$1,305</td><td class="up">$1,167</td></tr><tr><th scope="row">down 3%</th><td>$470.33</td><td class="up">$717</td><td class="up">$566</td></tr><tr><th scope="row">down 1%</th><td>$480.03</td><td class="up">$197</td><td class="up">$37</td></tr><tr><th scope="row">up 1%</th><td>$489.73</td><td class="dn">($257)</td><td class="dn">($419)</td></tr><tr><th scope="row">up 3%</th><td>$499.43</td><td class="dn">($645)</td><td class="dn">($805)</td></tr><tr><th scope="row">up 5%</th><td>$509.12</td><td class="dn">($973)</td><td class="dn">($1,125)</td></tr><tr><th scope="row">up 10%</th><td>$533.37</td><td class="dn">($1,560)</td><td class="dn">($1,679)</td></tr></tbody></table><p class="oc-plan"><b>Plan per contract</b> Stop at $11.08 costs about ($1,107). Target at $33.23 makes about $1,108.</p><p class="oc-foot">Profit or loss for one contract (100 shares), from an options pricing model that holds implied volatility flat and includes time decay. An estimate, not a prediction. Parentheses mean a loss.</p></aside>

## AAPL CALL: Best Available, Tactical
- Why: holding far better than chips, no earnings until late January.
- Trend: 343.54, 0.6% above a rising 50 day, RSI 53, down 1.6% today.
- Contract: Dec 18 $345 call, mark $10.58, delta 0.49, IV 29.9%
- Liquidity: Spread 2.4%, open interest 8,671, volume today 3,286, volume to OI 0.38
- Plan: Dec 18 expiry, enter only if it holds 341.60 and reclaims 345, sell within about 3 to 5 trading days, or at +50%, stop at 50% down.

<aside class="oc" aria-label="AAPL contract detail"><div class="oc-title">AAPL $345 call, Dec 18, 28 days left, stock $343.54</div><div class="oc-facts"><div><span>Cost to buy</span><b>$1,058</b></div><div><span>Most you can lose</span><b>$1,058</b></div><div><span>Each $1 the stock moves</span><b>about $49</b></div><div><span>Breakeven at expiry</span><b>$355.58 (up 3.5%)</b></div></div><table class="oc-table"><thead><tr><th>Stock moves</th><th>Stock price</th><th>In 1 day</th><th>In 5 days</th></tr></thead><tbody><tr><th scope="row">down 5%</th><td>$326.36</td><td class="dn">($676)</td><td class="dn">($742)</td></tr><tr><th scope="row">down 3%</th><td>$333.23</td><td class="dn">($466)</td><td class="dn">($544)</td></tr><tr><th scope="row">down 1%</th><td>$340.10</td><td class="dn">($187)</td><td class="dn">($274)</td></tr><tr><th scope="row">up 1%</th><td>$346.98</td><td class="up">$162</td><td class="up">$73</td></tr><tr><th scope="row">up 3%</th><td>$353.85</td><td class="up">$581</td><td class="up">$494</td></tr><tr><th scope="row">up 5%</th><td>$360.72</td><td class="up">$1,063</td><td class="up">$984</td></tr><tr><th scope="row">up 10%</th><td>$377.89</td><td class="up">$2,484</td><td class="up">$2,432</td></tr></tbody></table><p class="oc-plan"><b>Plan per contract</b> Stop at $5.29 costs about ($529). Target at $15.86 makes about $528.</p><p class="oc-foot">Profit or loss for one contract (100 shares), from an options pricing model that holds implied volatility flat and includes time decay. An estimate, not a prediction. Parentheses mean a loss.</p></aside>

## Other calls
- No second or third call passes. Closest was **V** Dec 18 $405 call, blocked by open interest 915.
- **XOM** and **XLE** are below their 50 day.

## Third put
- **META** Dec 18 $560 put: breakeven 5.8% away, ask size 1.
- **TSLA** Dec 18 $345 put: IV 61.6%.

## Dropped for spread
- V $405C 10.6%, XLK $150P 5.0%


</div>
