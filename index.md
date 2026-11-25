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

<div class="latest-head"><span class="eyebrow">Latest daily run</span><span class="meta">Live Verdict, 2026-11-25</span></div>

<div class="report" markdown="1">

# Calls and Puts Verdict, November 25, 2026
> Live chain grading at about 11:00 AM ET. Read only research, no trades placed.

- No Core calls today. The S&P 500 is well below its 200 day and down 2.6%.
- Tactical puts only. Trend puts lose on average in the backtest, so keep them small.
- Chase warning: only enter on a failed bounce, never into the flush. Wait for October PCE if it has not printed.

## Best Available

## QQQ PUT: Best Available, Tactical
- Why: AI capex and valuation selloff, Nasdaq 100 down 4.3% on Nov 25.
- Trend: $611.18, 13.7% below its 50 day.
- Contract: Dec 18 $610 put, mark $23.87, delta 0.46, IV 40.9%
- Liquidity: Spread 1.0%, open interest 56,295, volume today 11,052, volume to OI 0.20
- Plan: Dec 18 expiry, sell within about 3 to 5 trading days, or at +50%, stop at 50% down. Cost $2,387.

<aside class="oc" aria-label="QQQ contract detail"><div class="oc-title">QQQ $610 put, Dec 18, 23 days left, stock $611.18</div><div class="oc-facts"><div><span>Cost to buy</span><b>$2,387</b></div><div><span>Most you can lose</span><b>$2,387</b></div><div><span>Each $1 the stock moves</span><b>about $46</b></div><div><span>Breakeven at expiry</span><b>$586.13 (down 4.1%)</b></div></div><table class="oc-table"><thead><tr><th>Stock moves</th><th>Stock price</th><th>In 1 day</th><th>In 5 days</th></tr></thead><tbody><tr><th scope="row">down 5%</th><td>$580.62</td><td class="up">$1,665</td><td class="up">$1,480</td></tr><tr><th scope="row">down 3%</th><td>$592.84</td><td class="up">$906</td><td class="up">$699</td></tr><tr><th scope="row">down 1%</th><td>$605.07</td><td class="up">$243</td><td class="up">$24</td></tr><tr><th scope="row">up 1%</th><td>$617.29</td><td class="dn">($323)</td><td class="dn">($544)</td></tr><tr><th scope="row">up 3%</th><td>$629.52</td><td class="dn">($795)</td><td class="dn">($1,010)</td></tr><tr><th scope="row">up 5%</th><td>$641.74</td><td class="dn">($1,181)</td><td class="dn">($1,380)</td></tr><tr><th scope="row">up 10%</th><td>$672.30</td><td class="dn">($1,830)</td><td class="dn">($1,970)</td></tr></tbody></table><p class="oc-plan"><b>Plan per contract</b> Stop at $11.93 costs about ($1,194). Target at $35.80 makes about $1,193.</p><p class="oc-foot">Profit or loss for one contract (100 shares), from an options pricing model that holds implied volatility flat and includes time decay. An estimate, not a prediction. Parentheses mean a loss.</p></aside>

## AMZN PUT: Best Available, Tactical
- Why: AI capex doubts and tariff reports, down 6.2% on Nov 25.
- Trend: $236.60, 7.3% below its 50 day. Earnings late January, clear.
- Contract: Dec 18 $240 put, mark $12.55, delta 0.52, IV 46.2%
- Liquidity: Spread 2.4%, open interest 23,064, volume today 1,951, volume to OI 0.08
- Plan: Dec 18 expiry, enter on a failed bounce near $242 to $245, sell within 3 to 5 trading days, or at +50%, stop at 50% down. Cost $1,255.

<aside class="oc" aria-label="AMZN contract detail"><div class="oc-title">AMZN $240 put, Dec 18, 23 days left, stock $236.60</div><div class="oc-facts"><div><span>Cost to buy</span><b>$1,255</b></div><div><span>Most you can lose</span><b>$1,255</b></div><div><span>Each $1 the stock moves</span><b>about $52</b></div><div><span>Breakeven at expiry</span><b>$227.45 (down 3.9%)</b></div></div><table class="oc-table"><thead><tr><th>Stock moves</th><th>Stock price</th><th>In 1 day</th><th>In 5 days</th></tr></thead><tbody><tr><th scope="row">down 5%</th><td>$224.77</td><td class="up">$693</td><td class="up">$616</td></tr><tr><th scope="row">down 3%</th><td>$229.50</td><td class="up">$382</td><td class="up">$295</td></tr><tr><th scope="row">down 1%</th><td>$234.23</td><td class="up">$104</td><td class="up">$9</td></tr><tr><th scope="row">up 1%</th><td>$238.97</td><td class="dn">($141)</td><td class="dn">($240)</td></tr><tr><th scope="row">up 3%</th><td>$243.70</td><td class="dn">($354)</td><td class="dn">($453)</td></tr><tr><th scope="row">up 5%</th><td>$248.43</td><td class="dn">($536)</td><td class="dn">($632)</td></tr><tr><th scope="row">up 10%</th><td>$260.26</td><td class="dn">($868)</td><td class="dn">($946)</td></tr></tbody></table><p class="oc-plan"><b>Plan per contract</b> Stop at $6.28 costs about ($627). Target at $18.83 makes about $628.</p><p class="oc-foot">Profit or loss for one contract (100 shares), from an options pricing model that holds implied volatility flat and includes time decay. An estimate, not a prediction. Parentheses mean a loss.</p></aside>

## IWM PUT: Best Available, Tactical
- Why: small caps are the rate sensitive leg as a December hike gets priced.
- Trend: $263.37, 5.1% below its 50 day. Least extended of the set.
- Contract: Jan 15 $265 put, mark $11.09, delta 0.49, IV 27.5%
- Liquidity: Spread 1.2%, open interest 37,078, volume today 225, volume to OI 0.01
- Plan: Jan 15 expiry, sell within about 3 to 5 trading days, or at +50%, stop at 50% down. Cost $1,109.

<aside class="oc" aria-label="IWM contract detail"><div class="oc-title">IWM $265 put, Jan 15, 51 days left, stock $263.37</div><div class="oc-facts"><div><span>Cost to buy</span><b>$1,109</b></div><div><span>Most you can lose</span><b>$1,109</b></div><div><span>Each $1 the stock moves</span><b>about $49</b></div><div><span>Breakeven at expiry</span><b>$253.91 (down 3.6%)</b></div></div><table class="oc-table"><thead><tr><th>Stock moves</th><th>Stock price</th><th>In 1 day</th><th>In 5 days</th></tr></thead><tbody><tr><th scope="row">down 5%</th><td>$250.20</td><td class="up">$752</td><td class="up">$723</td></tr><tr><th scope="row">down 3%</th><td>$255.47</td><td class="up">$417</td><td class="up">$383</td></tr><tr><th scope="row">down 1%</th><td>$260.74</td><td class="up">$123</td><td class="up">$85</td></tr><tr><th scope="row">up 1%</th><td>$266.00</td><td class="dn">($131)</td><td class="dn">($170)</td></tr><tr><th scope="row">up 3%</th><td>$271.27</td><td class="dn">($346)</td><td class="dn">($384)</td></tr><tr><th scope="row">up 5%</th><td>$276.54</td><td class="dn">($523)</td><td class="dn">($560)</td></tr><tr><th scope="row">up 10%</th><td>$289.71</td><td class="dn">($827)</td><td class="dn">($855)</td></tr></tbody></table><p class="oc-plan"><b>Plan per contract</b> Stop at $5.54 costs about ($555). Target at $16.63 makes about $554.</p><p class="oc-foot">Profit or loss for one contract (100 shares), from an options pricing model that holds implied volatility flat and includes time decay. An estimate, not a prediction. Parentheses mean a loss.</p></aside>

## MSFT PUT: Also cleared, Tactical
- Contract: Dec 18 $480 put, mark $19.78, delta 0.48, IV 41.0%
- Liquidity: Spread 2.3%, open interest 12,285, volume today 457. Ask size only 5.
- Plan: sell within 3 to 5 trading days, or at +50%, stop at 50% down. Cost $1,978.

<aside class="oc" aria-label="MSFT contract detail"><div class="oc-title">MSFT $480 put, Dec 18, 23 days left, stock $479.39</div><div class="oc-facts"><div><span>Cost to buy</span><b>$1,978</b></div><div><span>Most you can lose</span><b>$1,978</b></div><div><span>Each $1 the stock moves</span><b>about $48</b></div><div><span>Breakeven at expiry</span><b>$460.22 (down 4.0%)</b></div></div><table class="oc-table"><thead><tr><th>Stock moves</th><th>Stock price</th><th>In 1 day</th><th>In 5 days</th></tr></thead><tbody><tr><th scope="row">down 5%</th><td>$455.42</td><td class="up">$1,331</td><td class="up">$1,186</td></tr><tr><th scope="row">down 3%</th><td>$465.01</td><td class="up">$726</td><td class="up">$563</td></tr><tr><th scope="row">down 1%</th><td>$474.60</td><td class="up">$196</td><td class="up">$22</td></tr><tr><th scope="row">up 1%</th><td>$484.18</td><td class="dn">($260)</td><td class="dn">($437)</td></tr><tr><th scope="row">up 3%</th><td>$493.77</td><td class="dn">($643)</td><td class="dn">($816)</td></tr><tr><th scope="row">up 5%</th><td>$503.36</td><td class="dn">($958)</td><td class="dn">($1,120)</td></tr><tr><th scope="row">up 10%</th><td>$527.33</td><td class="dn">($1,495)</td><td class="dn">($1,613)</td></tr></tbody></table><p class="oc-plan"><b>Plan per contract</b> Stop at $9.89 costs about ($989). Target at $29.67 makes about $989.</p><p class="oc-foot">Profit or loss for one contract (100 shares), from an options pricing model that holds implied volatility flat and includes time decay. An estimate, not a prediction. Parentheses mean a loss.</p></aside>

## Calls
- **No call passes the Tactical tier.** Up sector chains went wide on a crash day.
- Closest: ABBV Jan 15 $300 call, blocked by spread 5.1% and a bid size of 1.

## Dropped for spread
- XLK $150P 7.8%, LLY $1380C 8.0%, JNJ $280C 6.3%, XLP $92C 8.3%, XLV $183C 5.8%, KO $97.5C 4.2%, WMT $132C 7.2%

## Rejected
- SMH Jan $400 put: IV 64%, breakeven 9.1% away.
- NOW Dec $90 put: IV 60.3%, breakeven 5.9% away.
- QQQ Jan $610 put: breakeven 5.2% away.


</div>
