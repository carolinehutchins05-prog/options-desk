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

<div class="latest-head"><span class="eyebrow">Latest daily run</span><span class="meta">Premarket Plan, 2026-11-09</span></div>

<div class="report" markdown="1">

# Premarket Calls and Puts, November 9, 2026
Run started late, so contracts are priced on live 10:15 AM quotes. Still provisional.

## Today's Catalysts
- **NVDA** down 4% on a board probe into its CEO, reported Nov 9.
- Money rotating to other mega caps: **AMD** up 9%, **AMZN** up 4.4%, **GOOGL** up 3.6%.
- **SPY** $748.74, above its 200 day ($727.66), below its 50 day ($765.68). Core calls are allowed.

## Best Available

## AMZN CALL: Best Available, Tactical
- Why: leading the Nov 9 rotation out of NVDA into other mega caps.
- Trend: $270.79, above a rising 50 day ($253.95), RSI 54.
- Contract: Dec 18 $270 call, mark $12.85, delta 0.55, IV 33.4%
- Liquidity: Spread 2.3%, open interest 16,590, volume today 786, volume to OI 0.05
- Plan: Dec 18 expiry, sell within about 3 to 5 trading days, or at +50%, stop at 50% down.
- Verdict: **Tactical only**. Fails Core on 39 days and a 4.5% breakeven.

<aside class="oc" aria-label="AMZN contract detail"><div class="oc-title">AMZN $270 call, Dec 18, 39 days left, stock $270.79</div><div class="oc-facts"><div><span>Cost to buy</span><b>$1,285</b></div><div><span>Most you can lose</span><b>$1,285</b></div><div><span>Each $1 the stock moves</span><b>about $55</b></div><div><span>Breakeven at expiry</span><b>$282.85 (up 4.5%)</b></div></div><table class="oc-table"><thead><tr><th>Stock moves</th><th>Stock price</th><th>In 1 day</th><th>In 5 days</th></tr></thead><tbody><tr><th scope="row">down 5%</th><td>$257.25</td><td class="dn">($633)</td><td class="dn">($693)</td></tr><tr><th scope="row">down 3%</th><td>$262.67</td><td class="dn">($417)</td><td class="dn">($482)</td></tr><tr><th scope="row">down 1%</th><td>$268.08</td><td class="dn">($160)</td><td class="dn">($228)</td></tr><tr><th scope="row">up 1%</th><td>$273.50</td><td class="up">$136</td><td class="up">$67</td></tr><tr><th scope="row">up 3%</th><td>$278.91</td><td class="up">$471</td><td class="up">$404</td></tr><tr><th scope="row">up 5%</th><td>$284.33</td><td class="up">$842</td><td class="up">$777</td></tr><tr><th scope="row">up 10%</th><td>$297.87</td><td class="up">$1,900</td><td class="up">$1,849</td></tr></tbody></table><p class="oc-plan"><b>Plan per contract</b> Stop at $6.43 costs about ($642). Target at $19.28 makes about $643.</p><p class="oc-foot">Profit or loss for one contract (100 shares), from an options pricing model that holds implied volatility flat and includes time decay. An estimate, not a prediction. Parentheses mean a loss.</p></aside>

## GOOGL PUT: Best Available, Tactical
- Why: Oct 28 earnings crash, now bouncing into a falling 50 day.
- Trend: $294.91, below a falling 50 day ($332.93), RSI 30.
- Contract: Dec 18 $295 put, mark $11.95, delta 0.47 (put), IV 32.6%
- Liquidity: Spread 1.7%, open interest 4,277, volume today 222, volume to OI 0.05
- Plan: Dec 18 expiry, sell within about 3 to 5 trading days, or at +50%, stop at 50% down.
- Verdict: **Tactical only**. Trend puts lose on average in the backtest, keep it small.

<aside class="oc" aria-label="GOOGL contract detail"><div class="oc-title">GOOGL $295 put, Dec 18, 39 days left, stock $294.91</div><div class="oc-facts"><div><span>Cost to buy</span><b>$1,195</b></div><div><span>Most you can lose</span><b>$1,195</b></div><div><span>Each $1 the stock moves</span><b>about $47</b></div><div><span>Breakeven at expiry</span><b>$283.05 (down 4.0%)</b></div></div><table class="oc-table"><thead><tr><th>Stock moves</th><th>Stock price</th><th>In 1 day</th><th>In 5 days</th></tr></thead><tbody><tr><th scope="row">down 5%</th><td>$280.16</td><td class="up">$811</td><td class="up">$762</td></tr><tr><th scope="row">down 3%</th><td>$286.06</td><td class="up">$447</td><td class="up">$391</td></tr><tr><th scope="row">down 1%</th><td>$291.96</td><td class="up">$128</td><td class="up">$69</td></tr><tr><th scope="row">up 1%</th><td>$297.86</td><td class="dn">($146)</td><td class="dn">($207)</td></tr><tr><th scope="row">up 3%</th><td>$303.76</td><td class="dn">($377)</td><td class="dn">($436)</td></tr><tr><th scope="row">up 5%</th><td>$309.66</td><td class="dn">($567)</td><td class="dn">($623)</td></tr><tr><th scope="row">up 10%</th><td>$324.40</td><td class="dn">($893)</td><td class="dn">($934)</td></tr></tbody></table><p class="oc-plan"><b>Plan per contract</b> Stop at $5.98 costs about ($597). Target at $17.93 makes about $598.</p><p class="oc-foot">Profit or loss for one contract (100 shares), from an options pricing model that holds implied volatility flat and includes time decay. An estimate, not a prediction. Parentheses mean a loss.</p></aside>

## Only one call and one put passed
- Calls: AAPL blocked by gate 5 (52 week high on Nov 5). AXP blocked by a falling 50 day.
- Puts: NFLX blocked by spread 4.1%. PLTR blocked by breakeven down 7.3%.

## Rejected, and why
- **NVDA** put: earnings Nov 17 falls inside the holding window.
- **AAPL** call: 52 week high Nov 5, too close (gate 5).
- **AMD** call: below its 50 day despite the pop.
- **CEG** call: below a falling 50 day after its print.
- **KKR** call: 50 day is falling.

## Dropped for spread
- DE $690C 9.0%, AXP $320C 6.7%, NFLX $63P 4.1%

Two tactical contracts pass, zero Core. A SPY close under $735 invalidates the AMZN call.

</div>
