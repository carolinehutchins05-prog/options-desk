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

<div class="latest-head"><span class="eyebrow">Latest daily run</span><span class="meta">Premarket Plan, 2026-11-27</span></div>

<div class="report" markdown="1">

# Premarket Calls and Puts, November 27, 2026
> Provisional plan, priced on live marks at about 12:07 PM ET on the Black Friday half day.

## Market Gate
- **SPY** $726.02, below its 200 day ($733.16). No Core calls, Tactical tier only.
- Holiday rally on thin volume: SPY up 1.3%, QQQ up 2.0%, semis lead.
- Puts are Tactical only. The backtest showed trend puts lose on average, so keep them small.

## Best Available
## AAPL CALL: Best Available, Tactical
- Why: holding above a rising 50 day through the AI selloff. Relative strength, no dated catalyst.
- Trend: $357.47 vs rising 50 day $343.05, RSI 58.
- Contract: Jan 15 $360 call, mark $11.53, delta 0.51, IV 22.3%
- Liquidity: Spread 2.2%, open interest 67,876, volume today 972, volume to OI 0.01
- Verdict: break even $371.53 sits above the $360.83 52 week high, so it needs a breakout. Sell within 3 to 5 days, +50% at $17.30, stop $5.77.

<aside class="oc" aria-label="AAPL contract detail"><div class="oc-title">AAPL $360 call, Jan 15, 49 days left, stock $357.47</div><div class="oc-facts"><div><span>Cost to buy</span><b>$1,153</b></div><div><span>Most you can lose</span><b>$1,153</b></div><div><span>Each $1 the stock moves</span><b>about $51</b></div><div><span>Breakeven at expiry</span><b>$371.53 (up 3.9%)</b></div></div><table class="oc-table"><thead><tr><th>Stock moves</th><th>Stock price</th><th>In 1 day</th><th>In 5 days</th></tr></thead><tbody><tr><th scope="row">down 5%</th><td>$339.60</td><td class="dn">($706)</td><td class="dn">($749)</td></tr><tr><th scope="row">down 3%</th><td>$346.75</td><td class="dn">($480)</td><td class="dn">($530)</td></tr><tr><th scope="row">down 1%</th><td>$353.90</td><td class="dn">($187)</td><td class="dn">($242)</td></tr><tr><th scope="row">up 1%</th><td>$361.04</td><td class="up">$176</td><td class="up">$118</td></tr><tr><th scope="row">up 3%</th><td>$368.19</td><td class="up">$607</td><td class="up">$549</td></tr><tr><th scope="row">up 5%</th><td>$375.34</td><td class="up">$1,100</td><td class="up">$1,046</td></tr><tr><th scope="row">up 10%</th><td>$393.22</td><td class="up">$2,553</td><td class="up">$2,512</td></tr></tbody></table><p class="oc-plan"><b>Plan per contract</b> Stop at $5.77 costs about ($576). Target at $17.30 makes about $577.</p><p class="oc-foot">Profit or loss for one contract (100 shares), from an options pricing model that holds implied volatility flat and includes time decay. An estimate, not a prediction. Parentheses mean a loss.</p></aside>

## GOOGL PUT: Best Available, Tactical
- Why: AI capex doubts Nov 25, new 52 week low that day. Today's bounce faded from $279.57.
- Trend: $273.39 vs falling 50 day $318.24, RSI 37.
- Contract: Dec 18 $275 put, mark $10.95, delta 0.50, IV 39.6%
- Liquidity: Spread 2.7%, open interest 7,090, volume today 193, volume to OI 0.03
- Verdict: break even $264.05, 3.4% away. Sell within 3 to 5 days, +50% at $16.43, stop $5.48.

<aside class="oc" aria-label="GOOGL contract detail"><div class="oc-title">GOOGL $275 put, Dec 18, 21 days left, stock $273.39</div><div class="oc-facts"><div><span>Cost to buy</span><b>$1,095</b></div><div><span>Most you can lose</span><b>$1,095</b></div><div><span>Each $1 the stock moves</span><b>about $50</b></div><div><span>Breakeven at expiry</span><b>$264.05 (down 3.4%)</b></div></div><table class="oc-table"><thead><tr><th>Stock moves</th><th>Stock price</th><th>In 1 day</th><th>In 5 days</th></tr></thead><tbody><tr><th scope="row">down 5%</th><td>$259.72</td><td class="up">$801</td><td class="up">$724</td></tr><tr><th scope="row">down 3%</th><td>$265.19</td><td class="up">$437</td><td class="up">$347</td></tr><tr><th scope="row">down 1%</th><td>$270.66</td><td class="up">$118</td><td class="up">$19</td></tr><tr><th scope="row">up 1%</th><td>$276.12</td><td class="dn">($154)</td><td class="dn">($256)</td></tr><tr><th scope="row">up 3%</th><td>$281.59</td><td class="dn">($380)</td><td class="dn">($480)</td></tr><tr><th scope="row">up 5%</th><td>$287.06</td><td class="dn">($563)</td><td class="dn">($656)</td></tr><tr><th scope="row">up 10%</th><td>$300.73</td><td class="dn">($863)</td><td class="dn">($928)</td></tr></tbody></table><p class="oc-plan"><b>Plan per contract</b> Stop at $5.48 costs about ($547). Target at $16.43 makes about $548.</p><p class="oc-foot">Profit or loss for one contract (100 shares), from an options pricing model that holds implied volatility flat and includes time decay. An estimate, not a prediction. Parentheses mean a loss.</p></aside>

## MSFT PUT: Best Available, Tactical
- Why: AI capex doubts Nov 25. Up only 0.2% on a 2% Nasdaq day.
- Trend: $490.84 vs flat 50 day $519.55, RSI 39.
- Contract: Dec 18 $490 put, mark $15.43, delta 0.46, IV 35.0%
- Liquidity: Spread 3.6%, open interest 10,846, volume today 676, volume to OI 0.06
- Verdict: break even $474.57, 3.3% away. Sell within 3 to 5 days, +50% at $23.15, stop $7.72.

<aside class="oc" aria-label="MSFT contract detail"><div class="oc-title">MSFT $490 put, Dec 18, 21 days left, stock $490.84</div><div class="oc-facts"><div><span>Cost to buy</span><b>$1,543</b></div><div><span>Most you can lose</span><b>$1,543</b></div><div><span>Each $1 the stock moves</span><b>about $46</b></div><div><span>Breakeven at expiry</span><b>$474.57 (down 3.3%)</b></div></div><table class="oc-table"><thead><tr><th>Stock moves</th><th>Stock price</th><th>In 1 day</th><th>In 5 days</th></tr></thead><tbody><tr><th scope="row">down 5%</th><td>$466.30</td><td class="up">$1,402</td><td class="up">$1,282</td></tr><tr><th scope="row">down 3%</th><td>$476.11</td><td class="up">$756</td><td class="up">$613</td></tr><tr><th scope="row">down 1%</th><td>$485.93</td><td class="up">$203</td><td class="up">$48</td></tr><tr><th scope="row">up 1%</th><td>$495.75</td><td class="dn">($253)</td><td class="dn">($411)</td></tr><tr><th scope="row">up 3%</th><td>$505.57</td><td class="dn">($617)</td><td class="dn">($766)</td></tr><tr><th scope="row">up 5%</th><td>$515.38</td><td class="dn">($898)</td><td class="dn">($1,030)</td></tr><tr><th scope="row">up 10%</th><td>$539.92</td><td class="dn">($1,313)</td><td class="dn">($1,389)</td></tr></tbody></table><p class="oc-plan"><b>Plan per contract</b> Stop at $7.72 costs about ($771). Target at $23.15 makes about $772.</p><p class="oc-foot">Profit or loss for one contract (100 shares), from an options pricing model that holds implied volatility flat and includes time decay. An estimate, not a prediction. Parentheses mean a loss.</p></aside>

## NOW PUT: Best Available, Tactical
- Why: software selloff, lagging today's rally. RSI 31 is stretched, expect bounces.
- Trend: $92.51 vs falling 50 day $124.91.
- Contract: Dec 18 $94 put, mark $5.53, delta 0.51, IV 54.7%
- Liquidity: Spread 0.9%, open interest 2,176, volume today 567, volume to OI 0.26
- Verdict: break even $88.47, 4.4% away. Sell within 3 to 5 days, +50% at $8.30, stop $2.77.

<aside class="oc" aria-label="NOW contract detail"><div class="oc-title">NOW $94 put, Dec 18, 21 days left, stock $92.51</div><div class="oc-facts"><div><span>Cost to buy</span><b>$553</b></div><div><span>Most you can lose</span><b>$553</b></div><div><span>Each $1 the stock moves</span><b>about $51</b></div><div><span>Breakeven at expiry</span><b>$88.47 (down 4.4%)</b></div></div><table class="oc-table"><thead><tr><th>Stock moves</th><th>Stock price</th><th>In 1 day</th><th>In 5 days</th></tr></thead><tbody><tr><th scope="row">down 5%</th><td>$87.88</td><td class="up">$264</td><td class="up">$225</td></tr><tr><th scope="row">down 3%</th><td>$89.73</td><td class="up">$146</td><td class="up">$102</td></tr><tr><th scope="row">down 1%</th><td>$91.58</td><td class="up">$38</td><td class="dn">($8)</td></tr><tr><th scope="row">up 1%</th><td>$93.44</td><td class="dn">($57)</td><td class="dn">($106)</td></tr><tr><th scope="row">up 3%</th><td>$95.29</td><td class="dn">($142)</td><td class="dn">($190)</td></tr><tr><th scope="row">up 5%</th><td>$97.14</td><td class="dn">($215)</td><td class="dn">($263)</td></tr><tr><th scope="row">up 10%</th><td>$101.76</td><td class="dn">($355)</td><td class="dn">($396)</td></tr></tbody></table><p class="oc-plan"><b>Plan per contract</b> Stop at $2.77 costs about ($276). Target at $8.30 makes about $277.</p><p class="oc-foot">Profit or loss for one contract (100 shares), from an options pricing model that holds implied volatility flat and includes time decay. An estimate, not a prediction. Parentheses mean a loss.</p></aside>

## Rejected
- **TSLA** Dec $400 call: break even 5.3% away, contract already up 53% today.
- **ABBV** and **LH** calls: gate 5, 52 week highs this week.
- **LLY** call: above $1,000 a share.
- **AMZN** Dec $250 put: passes, but Black Friday is a live bull catalyst. Fourth choice.
- **NFLX** Dec $60 put: bid size 5, thin top of book.
- **META** Dec $625 put: open interest 1,844.
- **PLTR**, **CVX**, **GS**, **CAT**, **XOM**, **JPM**, **TSM**, **ANET** calls: below their 50 day.

## Dropped for spread
- AAPL Dec $357.50C 3.7% (open interest 365), GOOGL Dec $270P 4.7%

A thin holiday bounce inside a broken trend sets up the puts as fades for Monday. SPY reclaiming $733 on volume would flip the desk to calls.

</div>
