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

<div class="latest-head"><span class="eyebrow">Latest daily run</span><span class="meta">Live Verdict, 2026-11-16</span></div>

<div class="report" markdown="1">

# Calls and Puts Verdict, November 16, 2026
Live chain grading at 10:25 AM ET. Read only research, no trades placed.

## Market
- SPY $744.3, down 1.3%, still above its 200 day ($731.9), so calls are allowed
- QQQ down 2.2%, SMH down 4.2%. Money is rotating into health care and staples
- No Core contract cleared. The best Core length call, AMZN Jan 15 $260C, has a break even 6.0% away

## Best Available
## AMZN CALL: Best Available, Tactical
- Why: holds above a rising 50 day through the tech selloff; Anthropic IPO expected this week, Amazon is a major holder
- Trend: $259.42, down 2.7% today, 50 day $254.81 rising, RSI 57
- Contract: Dec 18 $260 call, mark $11.08, delta 0.53, IV 35.3%
- Liquidity: Spread 2.3%, open interest 19,827, volume today 1,008, volume to OI 0.05
- Plan: Dec 18 expiry, enter Wednesday after Tuesday night's chip earnings report only if AMZN holds $255, sell within 3 to 5 trading days or at +50% ($16.62), stop at 50% down ($5.54). Cost $1,108

<aside class="oc" aria-label="AMZN contract detail"><div class="oc-title">AMZN $260 call, Dec 18, 32 days left, stock $259.42</div><div class="oc-facts"><div><span>Cost to buy</span><b>$1,108</b></div><div><span>Most you can lose</span><b>$1,108</b></div><div><span>Each $1 the stock moves</span><b>about $53</b></div><div><span>Breakeven at expiry</span><b>$271.08 (up 4.5%)</b></div></div><table class="oc-table"><thead><tr><th>Stock moves</th><th>Stock price</th><th>In 1 day</th><th>In 5 days</th></tr></thead><tbody><tr><th scope="row">down 5%</th><td>$246.45</td><td class="dn">($575)</td><td class="dn">($639)</td></tr><tr><th scope="row">down 3%</th><td>$251.64</td><td class="dn">($382)</td><td class="dn">($454)</td></tr><tr><th scope="row">down 1%</th><td>$256.83</td><td class="dn">($150)</td><td class="dn">($226)</td></tr><tr><th scope="row">up 1%</th><td>$262.01</td><td class="up">$123</td><td class="up">$45</td></tr><tr><th scope="row">up 3%</th><td>$267.20</td><td class="up">$434</td><td class="up">$358</td></tr><tr><th scope="row">up 5%</th><td>$272.39</td><td class="up">$782</td><td class="up">$709</td></tr><tr><th scope="row">up 10%</th><td>$285.36</td><td class="up">$1,785</td><td class="up">$1,729</td></tr></tbody></table><p class="oc-plan"><b>Plan per contract</b> Stop at $5.54 costs about ($554). Target at $16.62 makes about $554.</p><p class="oc-foot">Profit or loss for one contract (100 shares), from an options pricing model that holds implied volatility flat and includes time decay. An estimate, not a prediction. Parentheses mean a loss.</p></aside>

## Puts
- No single stock put passes the Tactical tier today
- Closest: NOW Dec 18 $105 put, spread 2.2%, open interest 3,739, volume 193, blocked by delta 0.62 (limit 0.60)
- Trend puts lose about 6% a trade on average in the backtest

## Gapped Past Entry
- FCX: down 5.2% to $56.15. The planned put now chases a 5% flush, dead for today

## Rejected
- CVX call: break even 5.0% away, ask size 2
- XOM call: price fell below its 50 day
- ORCL put: IV 74%
- PLTR put: break even 6.6% away, volume 92
- BA put: volume 32. NFLX put: volume 28
- JNJ call: new 52 week high today
- GE call: volume 4. ISRG call: volume 0

## Dropped for spread
- UNH $410C 4.2%, CVX Dec $220C 6.8%, ABBV $300C 5.1%, JNJ $290C 5.5%, V $430C 5.7%, ABT $110C 8.5%, SHOP $140P 11.7%, SNDK put 14%

The tape is a defensive rotation ahead of Tuesday night's chip earnings report. A strong report would put AMZN back in play.

</div>
