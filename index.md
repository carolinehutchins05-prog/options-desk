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

<div class="latest-head"><span class="eyebrow">Latest daily run</span><span class="meta">Live Verdict, 2026-11-11</span></div>

<div class="report" markdown="1">

# Calls and Puts Verdict, November 11, 2026
Live chain grading at 10:20 AM ET. Read only research, no trades placed.

- S&P 500 ETF up 0.8%, above its 200 day, below its 50 day. Calls allowed.
- No Core contract cleared. No monthly expiry falls in the 45 to 60 day window.
- Chips are leading on CoreWeave earnings, but the chip ETF is still 10.8% under its 50 day.

## Best Available

## AMZN CALL: Best Available, Tactical
- Why: holding a rising 50 day while the market chases chips. No report until Feb 4.
- Trend: $268.33, 5.6% above a rising 50 day ($254.18), RSI 56.
- Contract: Dec 18 $270 call, mark $10.63, delta 0.51, IV 31.9%
- Liquidity: Spread 2.4%, open interest 15,598, volume today 618, volume to OI 0.04
- Plan: Dec 18 expiry, sell within about 3 to 5 trading days, or at +50%, stop at 50% down. Enter only on a hold of $267 with a real bid.

<aside class="oc" aria-label="AMZN contract detail"><div class="oc-title">AMZN $270 call, Dec 18, 37 days left, stock $268.33</div><div class="oc-facts"><div><span>Cost to buy</span><b>$1,063</b></div><div><span>Most you can lose</span><b>$1,063</b></div><div><span>Each $1 the stock moves</span><b>about $51</b></div><div><span>Breakeven at expiry</span><b>$280.63 (up 4.6%)</b></div></div><table class="oc-table"><thead><tr><th>Stock moves</th><th>Stock price</th><th>In 1 day</th><th>In 5 days</th></tr></thead><tbody><tr><th scope="row">down 5%</th><td>$254.91</td><td class="dn">($569)</td><td class="dn">($624)</td></tr><tr><th scope="row">down 3%</th><td>$260.28</td><td class="dn">($379)</td><td class="dn">($441)</td></tr><tr><th scope="row">down 1%</th><td>$265.65</td><td class="dn">($148)</td><td class="dn">($214)</td></tr><tr><th scope="row">up 1%</th><td>$271.01</td><td class="up">$126</td><td class="up">$59</td></tr><tr><th scope="row">up 3%</th><td>$276.38</td><td class="up">$442</td><td class="up">$375</td></tr><tr><th scope="row">up 5%</th><td>$281.75</td><td class="up">$797</td><td class="up">$733</td></tr><tr><th scope="row">up 10%</th><td>$295.16</td><td class="up">$1,831</td><td class="up">$1,780</td></tr></tbody></table><p class="oc-plan"><b>Plan per contract</b> Stop at $5.31 costs about ($532). Target at $15.94 makes about $531.</p><p class="oc-foot">Profit or loss for one contract (100 shares), from an options pricing model that holds implied volatility flat and includes time decay. An estimate, not a prediction. Parentheses mean a loss.</p></aside>

## QQQ PUT: Best Available, Tactical
- Why: Nasdaq 100 up 1.7% into a falling 50 day. Counter trend bounce. Trend puts lose on average in the backtest, keep it small.
- Trend: $686.13, 4.6% below a falling 50 day ($719.39).
- Contract: Dec 18 $685 put, mark $18.62, delta 0.46, IV 23.6%
- Liquidity: Spread 0.5%, open interest 8,716, volume today 215, volume to OI 0.02
- Plan: Dec 18 expiry, sell within about 3 to 5 trading days, or at +50%, stop at 50% down. Enter only on a fade back under $680.

<aside class="oc" aria-label="QQQ contract detail"><div class="oc-title">QQQ $685 put, Dec 18, 37 days left, stock $686.13</div><div class="oc-facts"><div><span>Cost to buy</span><b>$1,862</b></div><div><span>Most you can lose</span><b>$1,862</b></div><div><span>Each $1 the stock moves</span><b>about $46</b></div><div><span>Breakeven at expiry</span><b>$666.38 (down 2.9%)</b></div></div><table class="oc-table"><thead><tr><th>Stock moves</th><th>Stock price</th><th>In 1 day</th><th>In 5 days</th></tr></thead><tbody><tr><th scope="row">down 5%</th><td>$651.82</td><td class="up">$1,998</td><td class="up">$1,928</td></tr><tr><th scope="row">down 3%</th><td>$665.55</td><td class="up">$1,080</td><td class="up">$992</td></tr><tr><th scope="row">down 1%</th><td>$679.27</td><td class="up">$307</td><td class="up">$208</td></tr><tr><th scope="row">up 1%</th><td>$692.99</td><td class="dn">($318)</td><td class="dn">($419)</td></tr><tr><th scope="row">up 3%</th><td>$706.71</td><td class="dn">($802)</td><td class="dn">($897)</td></tr><tr><th scope="row">up 5%</th><td>$720.44</td><td class="dn">($1,161)</td><td class="dn">($1,243)</td></tr><tr><th scope="row">up 10%</th><td>$754.74</td><td class="dn">($1,650)</td><td class="dn">($1,693)</td></tr></tbody></table><p class="oc-plan"><b>Plan per contract</b> Stop at $9.31 costs about ($931). Target at $27.93 makes about $931.</p><p class="oc-foot">Profit or loss for one contract (100 shares), from an options pricing model that holds implied volatility flat and includes time decay. An estimate, not a prediction. Parentheses mean a loss.</p></aside>

- Only one call and one put pass the tactical tier. Closest other call: JNJ Dec 18 $280 call, blocked by spread 9.1%. Closest other put: NFLX Dec 18 $63 put, blocked by volume 32 (needs 100).

## Gapped Past Entry
- NOW put: stock bounced 1.4%, Dec 18 $100 put breakeven now 6.4% away. The $105 put trades only 16 contracts.
- IWM put: reclaimed its 50 day. Dead.

## Rejected
- UBER call: below a falling 50 day.
- ABT call: flat 50 day, Jan contract volume 10.
- NVT call: director bought $339K, but the stock is 21% under a falling 50 day.
- Chip and software ETF calls: still 8% to 11% under their 50 days.
- Health care and staples puts: those sectors are above rising 50 days.

## Dropped for spread
- PFE $29C 9.1%, JNJ $280C 9.1%, XLV $190C 9.2%, SCHW $92.50P 7.8%, C $125P 8.5%, ABT Jan $110C 5.8%, XOM $165P 4.5%

The tape flipped to chips today, but no chip leader repaired its 50 day. A fade back under this morning's lows revives the put side.

</div>
