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

<div class="latest-head"><span class="eyebrow">Latest daily run</span><span class="meta">Premarket Plan, 2026-11-25</span></div>

<div class="report" markdown="1">

# Premarket Calls and Puts, November 25, 2026
Provisional plan. This run priced contracts on live marks at about 10:56 AM ET. The live confirmation run issues the final list.

## Market Gate
- SPY $700.01, below its 200 day of $730.62. No Core calls today, Tactical tier only.
- Broad flush: SPY down 2.6%, chips down 7% to 10%.
- Thin holiday week. PCE inflation is due, do not size on it before it prints.
- Puts are Tactical only. The backtest showed trend puts lose on average, so keep them small.

## Best Available
## AAPL CALL: Best Available, Tactical
- Why: holding above a rising 50 day while megacaps break. No dated catalyst.
- Trend: $346.43 vs 50 day $342.58, RSI 57.
- Contract: Dec 18 $350 call, mark $8.43, delta 0.47, IV 27.8%
- Liquidity: Spread 3.0%, open interest 31,458, volume today 616, volume to OI 0.02
- Plan: Dec 18 expiry, sell within about 3 to 5 trading days, or at +50%, stop at 50% down. Cost $843.

<aside class="oc" aria-label="AAPL contract detail"><div class="oc-title">AAPL $350 call, Dec 18, 23 days left, stock $346.43</div><div class="oc-facts"><div><span>Cost to buy</span><b>$843</b></div><div><span>Most you can lose</span><b>$843</b></div><div><span>Each $1 the stock moves</span><b>about $47</b></div><div><span>Breakeven at expiry</span><b>$358.43 (up 3.5%)</b></div></div><table class="oc-table"><thead><tr><th>Stock moves</th><th>Stock price</th><th>In 1 day</th><th>In 5 days</th></tr></thead><tbody><tr><th scope="row">down 5%</th><td>$329.11</td><td class="dn">($594)</td><td class="dn">($655)</td></tr><tr><th scope="row">down 3%</th><td>$336.04</td><td class="dn">($420)</td><td class="dn">($499)</td></tr><tr><th scope="row">down 1%</th><td>$342.97</td><td class="dn">($175)</td><td class="dn">($268)</td></tr><tr><th scope="row">up 1%</th><td>$349.89</td><td class="up">$149</td><td class="up">$51</td></tr><tr><th scope="row">up 3%</th><td>$356.82</td><td class="up">$553</td><td class="up">$456</td></tr><tr><th scope="row">up 5%</th><td>$363.75</td><td class="up">$1,030</td><td class="up">$942</td></tr><tr><th scope="row">up 10%</th><td>$381.07</td><td class="up">$2,468</td><td class="up">$2,415</td></tr></tbody></table><p class="oc-plan"><b>Plan per contract</b> Stop at $4.22 costs about ($421). Target at $12.65 makes about $422.</p><p class="oc-foot">Profit or loss for one contract (100 shares), from an options pricing model that holds implied volatility flat and includes time decay. An estimate, not a prediction. Parentheses mean a loss.</p></aside>

## AMZN PUT: Best Available, Tactical
- Why: AI capex doubts and a new tariff report, Nov 25.
- Trend: $236.66 vs 50 day $255.15, below it.
- Contract: Dec 18 $240 put, mark $12.53, delta 0.52, IV 46.5%
- Liquidity: Spread 2.8%, open interest 23,064, volume today 1,877, volume to OI 0.08
- Plan: Dec 18 expiry, wait for a bounce toward $242 to $245, sell within about 3 to 5 trading days, or at +50%, stop at 50% down. Cost $1,253.

<aside class="oc" aria-label="AMZN contract detail"><div class="oc-title">AMZN $240 put, Dec 18, 23 days left, stock $236.66</div><div class="oc-facts"><div><span>Cost to buy</span><b>$1,253</b></div><div><span>Most you can lose</span><b>$1,253</b></div><div><span>Each $1 the stock moves</span><b>about $52</b></div><div><span>Breakeven at expiry</span><b>$227.47 (down 3.9%)</b></div></div><table class="oc-table"><thead><tr><th>Stock moves</th><th>Stock price</th><th>In 1 day</th><th>In 5 days</th></tr></thead><tbody><tr><th scope="row">down 5%</th><td>$224.83</td><td class="up">$692</td><td class="up">$614</td></tr><tr><th scope="row">down 3%</th><td>$229.56</td><td class="up">$382</td><td class="up">$294</td></tr><tr><th scope="row">down 1%</th><td>$234.29</td><td class="up">$104</td><td class="up">$9</td></tr><tr><th scope="row">up 1%</th><td>$239.03</td><td class="dn">($141)</td><td class="dn">($240)</td></tr><tr><th scope="row">up 3%</th><td>$243.76</td><td class="dn">($354)</td><td class="dn">($453)</td></tr><tr><th scope="row">up 5%</th><td>$248.49</td><td class="dn">($535)</td><td class="dn">($631)</td></tr><tr><th scope="row">up 10%</th><td>$260.33</td><td class="dn">($866)</td><td class="dn">($945)</td></tr></tbody></table><p class="oc-plan"><b>Plan per contract</b> Stop at $6.27 costs about ($626). Target at $18.80 makes about $627.</p><p class="oc-foot">Profit or loss for one contract (100 shares), from an options pricing model that holds implied volatility flat and includes time decay. An estimate, not a prediction. Parentheses mean a loss.</p></aside>

## GOOGL PUT: Best Available, Tactical
- Why: AI capex doubts, Nov 25. New 52 week low today.
- Trend: $264.93 vs falling 50 day $319.64, RSI 40.
- Contract: Dec 18 $265 put, mark $11.68, delta 0.47, IV 44.9%
- Liquidity: Spread 2.1%, open interest 7,684, volume today 887, volume to OI 0.12
- Plan: Dec 18 expiry, wait for a bounce, sell within about 3 to 5 trading days, or at +50%, stop at 50% down. Cost $1,168.

<aside class="oc" aria-label="GOOGL contract detail"><div class="oc-title">GOOGL $265 put, Dec 18, 23 days left, stock $264.93</div><div class="oc-facts"><div><span>Cost to buy</span><b>$1,168</b></div><div><span>Most you can lose</span><b>$1,168</b></div><div><span>Each $1 the stock moves</span><b>about $47</b></div><div><span>Breakeven at expiry</span><b>$253.32 (down 4.4%)</b></div></div><table class="oc-table"><thead><tr><th>Stock moves</th><th>Stock price</th><th>In 1 day</th><th>In 5 days</th></tr></thead><tbody><tr><th scope="row">down 5%</th><td>$251.68</td><td class="up">$718</td><td class="up">$628</td></tr><tr><th scope="row">down 3%</th><td>$256.98</td><td class="up">$392</td><td class="up">$293</td></tr><tr><th scope="row">down 1%</th><td>$262.28</td><td class="up">$105</td><td class="">$0</td></tr><tr><th scope="row">up 1%</th><td>$267.58</td><td class="dn">($145)</td><td class="dn">($251)</td></tr><tr><th scope="row">up 3%</th><td>$272.88</td><td class="dn">($357)</td><td class="dn">($461)</td></tr><tr><th scope="row">up 5%</th><td>$278.18</td><td class="dn">($534)</td><td class="dn">($632)</td></tr><tr><th scope="row">up 10%</th><td>$291.42</td><td class="dn">($846)</td><td class="dn">($921)</td></tr></tbody></table><p class="oc-plan"><b>Plan per contract</b> Stop at $5.84 costs about ($584). Target at $17.52 makes about $584.</p><p class="oc-foot">Profit or loss for one contract (100 shares), from an options pricing model that holds implied volatility flat and includes time decay. An estimate, not a prediction. Parentheses mean a loss.</p></aside>

## MSFT PUT: Best Available, Tactical
- Why: AI capex doubts, Nov 25.
- Trend: $479.39 vs 50 day $519.56, RSI 41.
- Contract: Dec 18 $480 put, mark $19.60, delta 0.48, IV 41.3%
- Liquidity: Spread 3.6%, open interest 12,285, volume today 456, volume to OI 0.04
- Plan: Dec 18 expiry, wait for a bounce, sell within about 3 to 5 trading days, or at +50%, stop at 50% down. Cost $1,960.

<aside class="oc" aria-label="MSFT contract detail"><div class="oc-title">MSFT $480 put, Dec 18, 23 days left, stock $479.39</div><div class="oc-facts"><div><span>Cost to buy</span><b>$1,960</b></div><div><span>Most you can lose</span><b>$1,960</b></div><div><span>Each $1 the stock moves</span><b>about $48</b></div><div><span>Breakeven at expiry</span><b>$460.40 (down 4.0%)</b></div></div><table class="oc-table"><thead><tr><th>Stock moves</th><th>Stock price</th><th>In 1 day</th><th>In 5 days</th></tr></thead><tbody><tr><th scope="row">down 5%</th><td>$455.42</td><td class="up">$1,334</td><td class="up">$1,191</td></tr><tr><th scope="row">down 3%</th><td>$465.01</td><td class="up">$728</td><td class="up">$566</td></tr><tr><th scope="row">down 1%</th><td>$474.60</td><td class="up">$196</td><td class="up">$24</td></tr><tr><th scope="row">up 1%</th><td>$484.18</td><td class="dn">($260)</td><td class="dn">($435)</td></tr><tr><th scope="row">up 3%</th><td>$493.77</td><td class="dn">($642)</td><td class="dn">($813)</td></tr><tr><th scope="row">up 5%</th><td>$503.36</td><td class="dn">($956)</td><td class="dn">($1,116)</td></tr><tr><th scope="row">up 10%</th><td>$527.33</td><td class="dn">($1,489)</td><td class="dn">($1,604)</td></tr></tbody></table><p class="oc-plan"><b>Plan per contract</b> Stop at $9.80 costs about ($980). Target at $29.40 makes about $980.</p><p class="oc-foot">Profit or loss for one contract (100 shares), from an options pricing model that holds implied volatility flat and includes time decay. An estimate, not a prediction. Parentheses mean a loss.</p></aside>

## Calls beyond AAPL
- Only one call passed the Tactical tier. The closest others failed gate 5 (ABBV, 52 week high today) and spread (EW, VRTX).

## Rejected
- **ABBV** call: printed a 52 week high today.
- **TMO** call: slipped below its 50 day.
- **LI**, **BZ** calls: earnings beats, but below a falling 50 day.
- **META** put: Dec $575 volume today only 48.
- **NVDA**, **AMD**, **MU** puts: down 7% to 10% today, never buy puts into a flush.
- **AMZN**, **GOOGL** Jan puts: break even more than 5% away.

## Dropped for spread
- EW $105C 53%, VRTX $560C 22%, DE $600P 34%

## Outlook
- AI and chip unwind into a thin holiday session with SPY under its 200 day. A reclaim of $718 or a soft PCE print invalidates the put side.

</div>
