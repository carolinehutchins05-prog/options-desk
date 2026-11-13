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

<div class="latest-head"><span class="eyebrow">Latest daily run</span><span class="meta">Premarket Plan, 2026-11-13</span></div>

<div class="report" markdown="1">

# Premarket Calls and Puts, November 13, 2026
Provisional plan on closing marks from Nov 12. The 10:00 AM run confirms on live quotes.

## Market Gate
- S&P 500 ETF closed $757.12, above its 200 day of $731.62. Calls allowed.
- No core contract today. The only 45 to 60 day expiry is the Dec 31 weekly, and it has almost no open interest.

## XOM CALL: Best Available, Tactical
- Why: oil up 2.6% after Houthi attacks on Saudi energy sites.
- Trend: $169.78, above a rising 50 day at $169.21, RSI 47. Supertrend still bearish.
- Contract: Dec 18 $170 call, mark $5.68, delta 0.53, IV 25.9%
- Liquidity: spread 2.6%, open interest 9,048, volume today 1,437, volume to OI 0.16
- Plan: Dec 18 expiry, sell within about 3 to 5 trading days, or at +50%, stop at 50% down ($2.84). Ex dividend Nov 16 trims the call.

<aside class="oc" aria-label="XOM contract detail"><div class="oc-title">XOM $170 call, Dec 18, 35 days left, stock $169.78</div><div class="oc-facts"><div><span>Cost to buy</span><b>$568</b></div><div><span>Most you can lose</span><b>$568</b></div><div><span>Each $1 the stock moves</span><b>about $53</b></div><div><span>Breakeven at expiry</span><b>$175.68 (up 3.5%)</b></div></div><table class="oc-table"><thead><tr><th>Stock moves</th><th>Stock price</th><th>In 1 day</th><th>In 5 days</th></tr></thead><tbody><tr><th scope="row">down 5%</th><td>$161.29</td><td class="dn">($351)</td><td class="dn">($379)</td></tr><tr><th scope="row">down 3%</th><td>$164.69</td><td class="dn">($239)</td><td class="dn">($272)</td></tr><tr><th scope="row">down 1%</th><td>$168.08</td><td class="dn">($94)</td><td class="dn">($130)</td></tr><tr><th scope="row">up 1%</th><td>$171.48</td><td class="up">$85</td><td class="up">$49</td></tr><tr><th scope="row">up 3%</th><td>$174.87</td><td class="up">$297</td><td class="up">$262</td></tr><tr><th scope="row">up 5%</th><td>$178.27</td><td class="up">$539</td><td class="up">$507</td></tr><tr><th scope="row">up 10%</th><td>$186.76</td><td class="up">$1,246</td><td class="up">$1,224</td></tr></tbody></table><p class="oc-plan"><b>Plan per contract</b> Stop at $2.84 costs about ($284). Target at $8.52 makes about $284.</p><p class="oc-foot">Profit or loss for one contract (100 shares), from an options pricing model that holds implied volatility flat and includes time decay. An estimate, not a prediction. Parentheses mean a loss.</p></aside>

## NOW PUT: Best Available, Tactical
- Why: no dated catalyst. Rate pressure on software with the 10 year at 5.10%. Trend puts lost on average in the backtest, keep it small.
- Trend: $100.66, far under a falling 50 day at $132.96.
- Contract: Dec 18 $105 put, mark $8.25, delta 0.58, IV 47.5%
- Liquidity: spread 1.2%, open interest 3,670, volume today 117, volume to OI 0.03
- Plan: Dec 18 expiry, sell within about 3 to 5 trading days, or at +50%, stop at 50% down ($4.13). Next report Jan 27.

<aside class="oc" aria-label="NOW contract detail"><div class="oc-title">NOW $105 put, Dec 18, 35 days left, stock $100.66</div><div class="oc-facts"><div><span>Cost to buy</span><b>$825</b></div><div><span>Most you can lose</span><b>$825</b></div><div><span>Each $1 the stock moves</span><b>about $58</b></div><div><span>Breakeven at expiry</span><b>$96.75 (down 3.9%)</b></div></div><table class="oc-table"><thead><tr><th>Stock moves</th><th>Stock price</th><th>In 1 day</th><th>In 5 days</th></tr></thead><tbody><tr><th scope="row">down 5%</th><td>$95.63</td><td class="up">$315</td><td class="up">$289</td></tr><tr><th scope="row">down 3%</th><td>$97.64</td><td class="up">$178</td><td class="up">$150</td></tr><tr><th scope="row">down 1%</th><td>$99.65</td><td class="up">$52</td><td class="up">$21</td></tr><tr><th scope="row">up 1%</th><td>$101.67</td><td class="dn">($64)</td><td class="dn">($97)</td></tr><tr><th scope="row">up 3%</th><td>$103.68</td><td class="dn">($169)</td><td class="dn">($204)</td></tr><tr><th scope="row">up 5%</th><td>$105.69</td><td class="dn">($264)</td><td class="dn">($298)</td></tr><tr><th scope="row">up 10%</th><td>$110.73</td><td class="dn">($456)</td><td class="dn">($489)</td></tr></tbody></table><p class="oc-plan"><b>Plan per contract</b> Stop at $4.13 costs about ($412). Target at $12.38 makes about $413.</p><p class="oc-foot">Profit or loss for one contract (100 shares), from an options pricing model that holds implied volatility flat and includes time decay. An estimate, not a prediction. Parentheses mean a loss.</p></aside>

## NFLX PUT: Best Available, Tactical
- Why: no dated catalyst, trend only. Smallest idea on the page.
- Trend: $62.69, under a falling 50 day at $69.59.
- Contract: Dec 18 $63 put, mark $2.74, delta 0.46, IV 37.0%
- Liquidity: spread 3.6%, open interest 8,903, volume today 262, volume to OI 0.03
- Plan: Dec 18 expiry, sell within about 3 to 5 trading days, or at +50%, stop at 50% down ($1.37). Next report Jan 19.

<aside class="oc" aria-label="NFLX contract detail"><div class="oc-title">NFLX $63 put, Dec 18, 35 days left, stock $62.69</div><div class="oc-facts"><div><span>Cost to buy</span><b>$274</b></div><div><span>Most you can lose</span><b>$274</b></div><div><span>Each $1 the stock moves</span><b>about $46</b></div><div><span>Breakeven at expiry</span><b>$60.26 (down 3.9%)</b></div></div><table class="oc-table"><thead><tr><th>Stock moves</th><th>Stock price</th><th>In 1 day</th><th>In 5 days</th></tr></thead><tbody><tr><th scope="row">down 5%</th><td>$59.56</td><td class="up">$177</td><td class="up">$166</td></tr><tr><th scope="row">down 3%</th><td>$60.81</td><td class="up">$98</td><td class="up">$85</td></tr><tr><th scope="row">down 1%</th><td>$62.06</td><td class="up">$28</td><td class="up">$14</td></tr><tr><th scope="row">up 1%</th><td>$63.32</td><td class="dn">($33)</td><td class="dn">($48)</td></tr><tr><th scope="row">up 3%</th><td>$64.57</td><td class="dn">($84)</td><td class="dn">($99)</td></tr><tr><th scope="row">up 5%</th><td>$65.82</td><td class="dn">($127)</td><td class="dn">($141)</td></tr><tr><th scope="row">up 10%</th><td>$68.96</td><td class="dn">($201)</td><td class="dn">($212)</td></tr></tbody></table><p class="oc-plan"><b>Plan per contract</b> Stop at $1.37 costs about ($137). Target at $4.11 makes about $137.</p><p class="oc-foot">Profit or loss for one contract (100 shares), from an options pricing model that holds implied volatility flat and includes time decay. An estimate, not a prediction. Parentheses mean a loss.</p></aside>

## Best Available, what blocked the rest
- Only one call passed the tactical tier. Third put blocked: PLTR $175 put, spread 4.2%.

## Dropped for spread
- CVX $220C 6.6%, CSCO $100P 7.2%, AMAT $380P 4.9%, PLTR $175P 4.2%

## Rejected
- CSCO: beat and raised, yet down 3% premarket. Put spread too wide.
- AMAT: beat, below a falling 50 day. Put IV 63%, over the 60% cap.
- NU: up 5% premarket on its print. No put against that.
- STNE: missed, but a $7 stock with a chain too thin to grade.

Oil names have the headline, software has the rate pressure. A fast oil reversal or yields back under 5% kills both sides.

</div>
