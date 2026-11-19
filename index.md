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

<div class="latest-head"><span class="eyebrow">Latest daily run</span><span class="meta">Live Verdict, 2026-11-19</span></div>

<div class="report" markdown="1">

# Calls and Puts Verdict, November 19, 2026
Live chain grading at 10:38 AM ET. Read only research, no trades placed.

## Market Gate
- The S&P 500 is below its 200 day average ($727.68 vs $732.55). **No Core call clears today.**
- The premarket AI gap on Anthropic IPO day fully reversed in the first hour.
- Puts are Tactical only. The backtest shows trend puts lose on average, so keep them small and short.

## QQQ PUT: Best Available, Tactical
- Why: QQQ opened up 2% on the Anthropic IPO and gave it all back by 10:30.
- Trend: $659.20, 7.7% below a falling 50 day ($714.36), RSI 38.
- Contract: Dec 18 $660 put, mark $22.27, delta 0.48, IV 30.5%
- Liquidity: Spread 0.7%, open interest 38,151, volume today 7,589, volume to OI 0.20
- Plan: Dec 18 expiry, enter only below $655, sell within about 3 to 5 trading days, or at +50%, stop at 50% down or QQQ above $673.

<aside class="oc" aria-label="QQQ contract detail"><div class="oc-title">QQQ $660 put, Dec 18, 29 days left, stock $659.20</div><div class="oc-facts"><div><span>Cost to buy</span><b>$2,227</b></div><div><span>Most you can lose</span><b>$2,227</b></div><div><span>Each $1 the stock moves</span><b>about $48</b></div><div><span>Breakeven at expiry</span><b>$637.73 (down 3.3%)</b></div></div><table class="oc-table"><thead><tr><th>Stock moves</th><th>Stock price</th><th>In 1 day</th><th>In 5 days</th></tr></thead><tbody><tr><th scope="row">down 5%</th><td>$626.24</td><td class="up">$1,910</td><td class="up">$1,796</td></tr><tr><th scope="row">down 3%</th><td>$639.42</td><td class="up">$1,041</td><td class="up">$905</td></tr><tr><th scope="row">down 1%</th><td>$652.61</td><td class="up">$292</td><td class="up">$143</td></tr><tr><th scope="row">up 1%</th><td>$665.79</td><td class="dn">($334)</td><td class="dn">($486)</td></tr><tr><th scope="row">up 3%</th><td>$678.98</td><td class="dn">($840)</td><td class="dn">($987)</td></tr><tr><th scope="row">up 5%</th><td>$692.16</td><td class="dn">($1,237)</td><td class="dn">($1,371)</td></tr><tr><th scope="row">up 10%</th><td>$725.12</td><td class="dn">($1,847)</td><td class="dn">($1,931)</td></tr></tbody></table><p class="oc-plan"><b>Plan per contract</b> Stop at $11.14 costs about ($1,113). Target at $33.41 makes about $1,114.</p><p class="oc-foot">Profit or loss for one contract (100 shares), from an options pricing model that holds implied volatility flat and includes time decay. An estimate, not a prediction. Parentheses mean a loss.</p></aside>

## IWM PUT: Best Available, Tactical
- Why: small caps are the weakest index today, down 0.9% while QQQ is flat.
- Trend: $267.57, 4.2% below a falling 50 day ($279.38), RSI 41.
- Contract: Dec 18 $268 put, mark $7.47, delta 0.48, IV 25.4%
- Liquidity: Spread 2.5%, open interest 28,358, volume today 173, volume to OI 0.01
- Plan: Dec 18 expiry, enter below $267, sell within about 3 to 5 trading days, or at +50%, stop at 50% down or IWM close above $272.

<aside class="oc" aria-label="IWM contract detail"><div class="oc-title">IWM $268 put, Dec 18, 29 days left, stock $267.57</div><div class="oc-facts"><div><span>Cost to buy</span><b>$747</b></div><div><span>Most you can lose</span><b>$747</b></div><div><span>Each $1 the stock moves</span><b>about $48</b></div><div><span>Breakeven at expiry</span><b>$260.53 (down 2.6%)</b></div></div><table class="oc-table"><thead><tr><th>Stock moves</th><th>Stock price</th><th>In 1 day</th><th>In 5 days</th></tr></thead><tbody><tr><th scope="row">down 5%</th><td>$254.19</td><td class="up">$813</td><td class="up">$781</td></tr><tr><th scope="row">down 3%</th><td>$259.54</td><td class="up">$440</td><td class="up">$397</td></tr><tr><th scope="row">down 1%</th><td>$264.89</td><td class="up">$124</td><td class="up">$75</td></tr><tr><th scope="row">up 1%</th><td>$270.25</td><td class="dn">($132)</td><td class="dn">($182)</td></tr><tr><th scope="row">up 3%</th><td>$275.60</td><td class="dn">($330)</td><td class="dn">($377)</td></tr><tr><th scope="row">up 5%</th><td>$280.95</td><td class="dn">($475)</td><td class="dn">($516)</td></tr><tr><th scope="row">up 10%</th><td>$294.33</td><td class="dn">($669)</td><td class="dn">($689)</td></tr></tbody></table><p class="oc-plan"><b>Plan per contract</b> Stop at $3.73 costs about ($374). Target at $11.20 makes about $373.</p><p class="oc-foot">Profit or loss for one contract (100 shares), from an options pricing model that holds implied volatility flat and includes time decay. An estimate, not a prediction. Parentheses mean a loss.</p></aside>

## Calls: nothing passes the Tactical tier
- Closest: **XLV** Dec 18 $180 call failed spread at 14.5%.
- **XLY** Dec 18 $120 call: spread 22.6%, volume 0.

## Rejected, and why
- **COHR**: CEO bought $997K, but price is below its 50 day ($223 vs $260).
- **ROK**: CEO bought $1.55M, but price is below its 50 day ($388 vs $425).
- **BA**: director cluster near $2M, but RSI 30 and below its 50 day.
- **NFLX** Dec 18 $60 put: volume 89 today, needs 100.
- Every morning leader (SMH, XLK, XLC) is below its 50 day. The AI rally was a counter trend bounce.

## Dropped for spread
- SMH $460P 6.8%, XLK $165P 16.0%, IGV $98P 12.1%, XLV $180C 14.5%, XLY $120C 22.6%


</div>
