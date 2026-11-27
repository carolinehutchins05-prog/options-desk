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

<div class="latest-head"><span class="eyebrow">Latest daily run</span><span class="meta">Live Verdict, 2026-11-27</span></div>

<div class="report" markdown="1">

# Calls and Puts Verdict, November 27, 2026
> Live chain grading at about 12:10 PM ET. Read only research, no trades placed.

- No Core calls. The S&P 500 is below its 200 day and its 50 day.
- Half day session, closes at 1:00 PM ET, so these are Monday entries.
- Tactical puts only. Trend puts lose on average in the backtest, so keep them small.

## Best Available

## NOW PUT: Best Available, Tactical
- Why: software selloff on AI capex doubts, Nov 25. Up only 0.6% while the Nasdaq 100 rose 1.9%.
- Trend: $92.71, 25.8% below a falling 50 day, RSI 31.
- Contract: Dec 18 $94 put, mark $5.43, delta 0.51, IV 54.9%
- Liquidity: Spread 0.9%, open interest 2,176, volume today 567, volume to OI 0.26
- Plan: Dec 18 expiry, enter Monday on a failed bounce under $92, sell within about 3 to 5 trading days, or at +50%, stop at 50% down. Cost $543.

<aside class="oc" aria-label="NOW contract detail"><div class="oc-title">NOW $94 put, Dec 18, 21 days left, stock $92.71</div><div class="oc-facts"><div><span>Cost to buy</span><b>$543</b></div><div><span>Most you can lose</span><b>$543</b></div><div><span>Each $1 the stock moves</span><b>about $51</b></div><div><span>Breakeven at expiry</span><b>$88.57 (down 4.5%)</b></div></div><table class="oc-table"><thead><tr><th>Stock moves</th><th>Stock price</th><th>In 1 day</th><th>In 5 days</th></tr></thead><tbody><tr><th scope="row">down 5%</th><td>$88.07</td><td class="up">$262</td><td class="up">$222</td></tr><tr><th scope="row">down 3%</th><td>$89.93</td><td class="up">$144</td><td class="up">$100</td></tr><tr><th scope="row">down 1%</th><td>$91.78</td><td class="up">$38</td><td class="dn">($9)</td></tr><tr><th scope="row">up 1%</th><td>$93.64</td><td class="dn">($57)</td><td class="dn">($105)</td></tr><tr><th scope="row">up 3%</th><td>$95.49</td><td class="dn">($140)</td><td class="dn">($189)</td></tr><tr><th scope="row">up 5%</th><td>$97.35</td><td class="dn">($213)</td><td class="dn">($260)</td></tr><tr><th scope="row">up 10%</th><td>$101.98</td><td class="dn">($350)</td><td class="dn">($390)</td></tr></tbody></table><p class="oc-plan"><b>Plan per contract</b> Stop at $2.72 costs about ($271). Target at $8.15 makes about $272.</p><p class="oc-foot">Profit or loss for one contract (100 shares), from an options pricing model that holds implied volatility flat and includes time decay. An estimate, not a prediction. Parentheses mean a loss.</p></aside>

## MSFT PUT: Best Available, Tactical
- Why: AI capex doubts, Nov 25. Up only 0.3% today and faded from $500.47.
- Trend: $491.18, 5.5% below a flat 50 day, RSI 39.
- Contract: Dec 18 $490 put, mark $15.30, delta 0.46, IV 35.0%
- Liquidity: Spread 3.3%, open interest 10,846, volume today 676, volume to OI 0.06
- Plan: Dec 18 expiry, enter Monday under $489, sell within about 3 to 5 trading days, or at +50%, stop at 50% down. Cost $1,530.

<aside class="oc" aria-label="MSFT contract detail"><div class="oc-title">MSFT $490 put, Dec 18, 21 days left, stock $491.18</div><div class="oc-facts"><div><span>Cost to buy</span><b>$1,530</b></div><div><span>Most you can lose</span><b>$1,530</b></div><div><span>Each $1 the stock moves</span><b>about $46</b></div><div><span>Breakeven at expiry</span><b>$474.70 (down 3.4%)</b></div></div><table class="oc-table"><thead><tr><th>Stock moves</th><th>Stock price</th><th>In 1 day</th><th>In 5 days</th></tr></thead><tbody><tr><th scope="row">down 5%</th><td>$466.62</td><td class="up">$1,395</td><td class="up">$1,273</td></tr><tr><th scope="row">down 3%</th><td>$476.44</td><td class="up">$751</td><td class="up">$607</td></tr><tr><th scope="row">down 1%</th><td>$486.27</td><td class="up">$202</td><td class="up">$45</td></tr><tr><th scope="row">up 1%</th><td>$496.09</td><td class="dn">($252)</td><td class="dn">($409)</td></tr><tr><th scope="row">up 3%</th><td>$505.92</td><td class="dn">($613)</td><td class="dn">($762)</td></tr><tr><th scope="row">up 5%</th><td>$515.74</td><td class="dn">($891)</td><td class="dn">($1,023)</td></tr><tr><th scope="row">up 10%</th><td>$540.30</td><td class="dn">($1,302)</td><td class="dn">($1,378)</td></tr></tbody></table><p class="oc-plan"><b>Plan per contract</b> Stop at $7.65 costs about ($765). Target at $22.95 makes about $765.</p><p class="oc-foot">Profit or loss for one contract (100 shares), from an options pricing model that holds implied volatility flat and includes time decay. An estimate, not a prediction. Parentheses mean a loss.</p></aside>

## AMZN PUT: Best Available, Tactical
- Why: AI capex doubts, Nov 25. Bounced 3.9% today right into its 50 day.
- Trend: $253.96, 0.5% below its 50 day, RSI 42. Black Friday is a live bull catalyst, so it ranks third.
- Contract: Dec 18 $250 put, mark $7.60, delta 0.41, IV 40.3%
- Liquidity: Spread 2.6%, open interest 14,916, volume today 529, volume to OI 0.04
- Plan: Dec 18 expiry, enter only if it fails at the 50 day near $255, sell within about 3 to 5 trading days, or at +50%, stop at 50% down. Cost $760.

<aside class="oc" aria-label="AMZN contract detail"><div class="oc-title">AMZN $250 put, Dec 18, 21 days left, stock $253.96</div><div class="oc-facts"><div><span>Cost to buy</span><b>$760</b></div><div><span>Most you can lose</span><b>$760</b></div><div><span>Each $1 the stock moves</span><b>about $41</b></div><div><span>Breakeven at expiry</span><b>$242.40 (down 4.6%)</b></div></div><table class="oc-table"><thead><tr><th>Stock moves</th><th>Stock price</th><th>In 1 day</th><th>In 5 days</th></tr></thead><tbody><tr><th scope="row">down 5%</th><td>$241.26</td><td class="up">$629</td><td class="up">$546</td></tr><tr><th scope="row">down 3%</th><td>$246.34</td><td class="up">$336</td><td class="up">$245</td></tr><tr><th scope="row">down 1%</th><td>$251.42</td><td class="up">$87</td><td class="dn">($7)</td></tr><tr><th scope="row">up 1%</th><td>$256.50</td><td class="dn">($120)</td><td class="dn">($211)</td></tr><tr><th scope="row">up 3%</th><td>$261.58</td><td class="dn">($286)</td><td class="dn">($371)</td></tr><tr><th scope="row">up 5%</th><td>$266.66</td><td class="dn">($417)</td><td class="dn">($492)</td></tr><tr><th scope="row">up 10%</th><td>$279.36</td><td class="dn">($621)</td><td class="dn">($666)</td></tr></tbody></table><p class="oc-plan"><b>Plan per contract</b> Stop at $3.80 costs about ($380). Target at $11.40 makes about $380.</p><p class="oc-foot">Profit or loss for one contract (100 shares), from an options pricing model that holds implied volatility flat and includes time decay. An estimate, not a prediction. Parentheses mean a loss.</p></aside>

## Calls
- No call passes the Tactical tier on this page. Closest: TSLA Dec 18 $400 call, break even 5.3% away against a 5% bar, and the contract was already up 53% on the day.

## Rejected, and why
- TSLA Jan 15 $400 call: break even 7.5% away.
- XLY Jan 15 $120 call: spread 13%, volume today 0.
- PATK Jan 15 $85 call: open interest 0.
- GLXY: insider cluster, but the stock is far below its 50 day, so no call.
- Semiconductor, tech, energy and communication ETF calls: all below their 50 day despite the rally.

### Corporate
- GLXY: CEO bought $955K and CFO $269K on Nov 25. Strongest read on the page, broken trend.
- PATK: $417K buy on Nov 25. Uptrend, but the option chain is dead.
- BORR: $3.94M buy on Nov 24, no officer title shown, weak.

Thin holiday rally inside a broken tape, with software laggards barely joining in. A close back above the 50 day in MSFT, or the S&P 500 reclaiming its 200 day on real volume, kills the puts.

</div>
