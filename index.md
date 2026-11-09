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

<div class="latest-head"><span class="eyebrow">Latest daily run</span><span class="meta">Live Verdict, 2026-11-09</span></div>

<div class="report" markdown="1">

# Calls and Puts Verdict, November 9, 2026
Live chain grading at 10:15 to 10:20 AM ET. Read only research, no trades placed.

- S&P 500 ETF above its 200 day, below its 50 day. Calls allowed, but the tape is a bounce.
- No Core contract cleared. No monthly expiry falls in the 45 to 60 day window.

## Best Available

## AMZN CALL: Best Available, Tactical
- Why: leading the Nov 9 rotation away from the AI chip leader, up 4.4%.
- Trend: $270.73, above a flat to rising 50 day ($253.95), RSI 54.
- Contract: Dec 18 $270 call, mark $12.85, delta 0.55, IV 33.6%
- Liquidity: Spread 2.3%, open interest 16,590, volume today 791, volume to OI 0.05
- Plan: Dec 18 expiry, sell within about 3 to 5 trading days, or at +50%, stop at 50% down. Enter on a pullback that holds $269, never above $275.31.

<aside class="oc" aria-label="AMZN contract detail"><div class="oc-title">AMZN $270 call, Dec 18, 39 days left, stock $270.73</div><div class="oc-facts"><div><span>Cost to buy</span><b>$1,285</b></div><div><span>Most you can lose</span><b>$1,285</b></div><div><span>Each $1 the stock moves</span><b>about $55</b></div><div><span>Breakeven at expiry</span><b>$282.85 (up 4.5%)</b></div></div><table class="oc-table"><thead><tr><th>Stock moves</th><th>Stock price</th><th>In 1 day</th><th>In 5 days</th></tr></thead><tbody><tr><th scope="row">down 5%</th><td>$257.19</td><td class="dn">($632)</td><td class="dn">($692)</td></tr><tr><th scope="row">down 3%</th><td>$262.61</td><td class="dn">($416)</td><td class="dn">($481)</td></tr><tr><th scope="row">down 1%</th><td>$268.02</td><td class="dn">($160)</td><td class="dn">($228)</td></tr><tr><th scope="row">up 1%</th><td>$273.44</td><td class="up">$136</td><td class="up">$67</td></tr><tr><th scope="row">up 3%</th><td>$278.85</td><td class="up">$470</td><td class="up">$402</td></tr><tr><th scope="row">up 5%</th><td>$284.27</td><td class="up">$840</td><td class="up">$776</td></tr><tr><th scope="row">up 10%</th><td>$297.80</td><td class="up">$1,897</td><td class="up">$1,845</td></tr></tbody></table><p class="oc-plan"><b>Plan per contract</b> Stop at $6.43 costs about ($642). Target at $19.28 makes about $643.</p><p class="oc-foot">Profit or loss for one contract (100 shares), from an options pricing model that holds implied volatility flat and includes time decay. An estimate, not a prediction. Parentheses mean a loss.</p></aside>

## IWM PUT: Best Available, Tactical
- Why: small caps bouncing into a falling 50 day. Trend puts lose on average in the backtest, keep it small.
- Trend: $279.51, below its 50 day ($282.11), RSI 43.
- Contract: Dec 18 $279 put, mark $7.17, delta 0.46, IV 21.8%
- Liquidity: Spread 1.1%, open interest 2,758, volume today 112, volume to OI 0.04
- Plan: Dec 18 expiry, sell within about 3 to 5 trading days, or at +50%, stop at 50% down. Enter only on a fade under $277.44.

<aside class="oc" aria-label="IWM contract detail"><div class="oc-title">IWM $279 put, Dec 18, 39 days left, stock $279.51</div><div class="oc-facts"><div><span>Cost to buy</span><b>$717</b></div><div><span>Most you can lose</span><b>$717</b></div><div><span>Each $1 the stock moves</span><b>about $46</b></div><div><span>Breakeven at expiry</span><b>$271.83 (down 2.7%)</b></div></div><table class="oc-table"><thead><tr><th>Stock moves</th><th>Stock price</th><th>In 1 day</th><th>In 5 days</th></tr></thead><tbody><tr><th scope="row">down 5%</th><td>$265.53</td><td class="up">$819</td><td class="up">$795</td></tr><tr><th scope="row">down 3%</th><td>$271.12</td><td class="up">$441</td><td class="up">$410</td></tr><tr><th scope="row">down 1%</th><td>$276.71</td><td class="up">$125</td><td class="up">$90</td></tr><tr><th scope="row">up 1%</th><td>$282.31</td><td class="dn">($128)</td><td class="dn">($164)</td></tr><tr><th scope="row">up 3%</th><td>$287.90</td><td class="dn">($321)</td><td class="dn">($355)</td></tr><tr><th scope="row">up 5%</th><td>$293.49</td><td class="dn">($461)</td><td class="dn">($490)</td></tr><tr><th scope="row">up 10%</th><td>$307.46</td><td class="dn">($645)</td><td class="dn">($660)</td></tr></tbody></table><p class="oc-plan"><b>Plan per contract</b> Stop at $3.59 costs about ($358). Target at $10.76 makes about $359.</p><p class="oc-foot">Profit or loss for one contract (100 shares), from an options pricing model that holds implied volatility flat and includes time decay. An estimate, not a prediction. Parentheses mean a loss.</p></aside>

## QQQ PUT: Best Available, Tactical
- Why: Nasdaq 100 up 2.8% but still 6.5% under its 50 day. Counter trend bounce. Keep it small.
- Trend: $674.40, below a falling 50 day ($720.97), RSI 31.
- Contract: Dec 18 $675 put, mark $21.72, delta 0.47, IV 25.7%
- Liquidity: Spread 0.9%, open interest 27,451, volume today 288, volume to OI 0.01
- Plan: Dec 18 expiry, sell within about 3 to 5 trading days, or at +50%, stop at 50% down. Enter only on a fade under $668.

<aside class="oc" aria-label="QQQ contract detail"><div class="oc-title">QQQ $675 put, Dec 18, 39 days left, stock $674.40</div><div class="oc-facts"><div><span>Cost to buy</span><b>$2,172</b></div><div><span>Most you can lose</span><b>$2,172</b></div><div><span>Each $1 the stock moves</span><b>about $47</b></div><div><span>Breakeven at expiry</span><b>$653.28 (down 3.1%)</b></div></div><table class="oc-table"><thead><tr><th>Stock moves</th><th>Stock price</th><th>In 1 day</th><th>In 5 days</th></tr></thead><tbody><tr><th scope="row">down 5%</th><td>$640.68</td><td class="up">$1,952</td><td class="up">$1,874</td></tr><tr><th scope="row">down 3%</th><td>$654.17</td><td class="up">$1,066</td><td class="up">$971</td></tr><tr><th scope="row">down 1%</th><td>$667.66</td><td class="up">$306</td><td class="up">$201</td></tr><tr><th scope="row">up 1%</th><td>$681.14</td><td class="dn">($325)</td><td class="dn">($433)</td></tr><tr><th scope="row">up 3%</th><td>$694.63</td><td class="dn">($833)</td><td class="dn">($936)</td></tr><tr><th scope="row">up 5%</th><td>$708.12</td><td class="dn">($1,227)</td><td class="dn">($1,321)</td></tr><tr><th scope="row">up 10%</th><td>$741.84</td><td class="dn">($1,821)</td><td class="dn">($1,880)</td></tr></tbody></table><p class="oc-plan"><b>Plan per contract</b> Stop at $10.86 costs about ($1,086). Target at $32.58 makes about $1,086.</p><p class="oc-foot">Profit or loss for one contract (100 shares), from an options pricing model that holds implied volatility flat and includes time decay. An estimate, not a prediction. Parentheses mean a loss.</p></aside>

- Only one call passes the tactical tier. Closest other: XLF Dec 18 $58 call, blocked by spread 7.7%.

## Rejected
- MTDR, KMI, CVS calls: insider buys, but all below their 50 days.
- AXP call: falling 50 day, Jan contracts have no volume.
- AMZN Dec 24 $270 call: open interest 77, too thin.
- Tech and semis ETF calls: 10% to 15% under their 50 days.

## Dropped for spread
- XLY $121C 14.6%, XLF $58C 7.7%, XLE $62.50P 6.3%, NFLX $64P 4.1%, AMZN Dec 24 $270C 11.5%


</div>
