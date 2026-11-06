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
<p class="meta">Source on <a href="https://github.com/carolinehutchins05-prog/options-desk">GitHub</a>. Built and maintained by Caroline Hutchins.</p>
</section>

<div class="latest-head"><span class="eyebrow">Latest daily run</span><span class="meta">Live Verdict, 2026-11-06</span></div>

<div class="report" markdown="1">

# Calls and Puts Verdict, November 6, 2026
Live chain grading at 10:15 ET. Read only research, no trades placed.

## Market
- **No core trade.** SPY $740.98 is above its 200 day ($730.15), so calls are allowed, but no 45 to 60 day contract is liquid.
- Relief bounce: QQQ up 2.2%, SMH up 4.4%, after Thursday's 5.5% Nasdaq drop. Both still far under falling 50 day lines.
- Jobs report printed at 8:30, so the macro gate is clear.

## Best Available
## AMZN CALL: Best Available, Tactical
- Why: relative strength, held its 50 day through the crash, up 1.2% today. Next report Feb 4.
- Trend: $263.29, 3.7% over its 50 day ($253.89), RSI 55.
- Contract: Dec 18 $260 call, mark $14.78, delta 0.58, IV 34.9%
- Liquidity: Spread 1.7%, open interest 16,297, volume today 268, volume to OI 0.02
- Plan: Dec 18 expiry, sell within about 3 to 5 trading days, or at +50% ($22.17). Stop at $7.39 or an AMZN close under $254.

<aside class="oc" aria-label="AMZN contract detail"><div class="oc-title">AMZN $260 call, Dec 18, 42 days left, stock $263.29</div><div class="oc-facts"><div><span>Cost to buy</span><b>$1,478</b></div><div><span>Most you can lose</span><b>$1,478</b></div><div><span>Each $1 the stock moves</span><b>about $58</b></div><div><span>Breakeven at expiry</span><b>$274.78 (up 4.4%)</b></div></div><table class="oc-table"><thead><tr><th>Stock moves</th><th>Stock price</th><th>In 1 day</th><th>In 5 days</th></tr></thead><tbody><tr><th scope="row">down 5%</th><td>$250.13</td><td class="dn">($668)</td><td class="dn">($729)</td></tr><tr><th scope="row">down 3%</th><td>$255.39</td><td class="dn">($435)</td><td class="dn">($500)</td></tr><tr><th scope="row">down 1%</th><td>$260.66</td><td class="dn">($165)</td><td class="dn">($231)</td></tr><tr><th scope="row">up 1%</th><td>$265.92</td><td class="up">$141</td><td class="up">$75</td></tr><tr><th scope="row">up 3%</th><td>$271.19</td><td class="up">$481</td><td class="up">$416</td></tr><tr><th scope="row">up 5%</th><td>$276.45</td><td class="up">$851</td><td class="up">$790</td></tr><tr><th scope="row">up 10%</th><td>$289.62</td><td class="up">$1,893</td><td class="up">$1,844</td></tr></tbody></table><p class="oc-plan"><b>Plan per contract</b> Stop at $7.39 costs about ($739). Target at $22.17 makes about $739.</p><p class="oc-foot">Profit or loss for one contract (100 shares), from an options pricing model that holds implied volatility flat and includes time decay. An estimate, not a prediction. Parentheses mean a loss.</p></aside>

## AAPL CALL: Best Available, Tactical
- Why: strongest megacap trend through the selloff.
- Trend: $343.23, 2.3% over a rising 50 day ($335.46), RSI 53.
- Contract: Dec 18 $345 call, mark $11.83, delta 0.52, IV 25.2%
- Liquidity: Spread 1.3%, open interest 8,191, volume today 399, volume to OI 0.05
- Plan: blocked until Nov 10 by a 52 week high on Nov 5. Then enter only above $340. Stop $5.92, target $17.75.

<aside class="oc" aria-label="AAPL contract detail"><div class="oc-title">AAPL $345 call, Dec 18, 42 days left, stock $343.23</div><div class="oc-facts"><div><span>Cost to buy</span><b>$1,183</b></div><div><span>Most you can lose</span><b>$1,183</b></div><div><span>Each $1 the stock moves</span><b>about $52</b></div><div><span>Breakeven at expiry</span><b>$356.83 (up 4.0%)</b></div></div><table class="oc-table"><thead><tr><th>Stock moves</th><th>Stock price</th><th>In 1 day</th><th>In 5 days</th></tr></thead><tbody><tr><th scope="row">down 5%</th><td>$326.07</td><td class="dn">($701)</td><td class="dn">($752)</td></tr><tr><th scope="row">down 3%</th><td>$332.93</td><td class="dn">($474)</td><td class="dn">($533)</td></tr><tr><th scope="row">down 1%</th><td>$339.80</td><td class="dn">($185)</td><td class="dn">($249)</td></tr><tr><th scope="row">up 1%</th><td>$346.66</td><td class="up">$168</td><td class="up">$102</td></tr><tr><th scope="row">up 3%</th><td>$353.53</td><td class="up">$583</td><td class="up">$518</td></tr><tr><th scope="row">up 5%</th><td>$360.39</td><td class="up">$1,055</td><td class="up">$994</td></tr><tr><th scope="row">up 10%</th><td>$377.55</td><td class="up">$2,439</td><td class="up">$2,394</td></tr></tbody></table><p class="oc-plan"><b>Plan per contract</b> Stop at $5.92 costs about ($591). Target at $17.75 makes about $592.</p><p class="oc-foot">Profit or loss for one contract (100 shares), from an options pricing model that holds implied volatility flat and includes time decay. An estimate, not a prediction. Parentheses mean a loss.</p></aside>

- Third call: nothing passes. Closest is MSFT Dec 18 $535C, volume 42.

## NFLX PUT: Best Available, Tactical
- Why: relative weakness, down 2.1% while QQQ is up 2.2%. Next report Jan 19.
- Trend: $64.18, 10.1% under a falling 50 day ($71.36), RSI 45.
- Contract: Dec 18 $64 put, mark $2.77, delta 0.45, IV 34.6%
- Liquidity: Spread 2.5%, open interest 5,269, volume today 164, volume to OI 0.03
- Plan: enter on a failed bounce under $65.50. Sell within 3 to 5 days or at +50% ($4.15). Stop $1.38 or a close above $67. Trend puts lose about 6% a trade in the backtest, keep it small.

<aside class="oc" aria-label="NFLX contract detail"><div class="oc-title">NFLX $64 put, Dec 18, 42 days left, stock $64.18</div><div class="oc-facts"><div><span>Cost to buy</span><b>$277</b></div><div><span>Most you can lose</span><b>$277</b></div><div><span>Each $1 the stock moves</span><b>about $45</b></div><div><span>Breakeven at expiry</span><b>$61.23 (down 4.6%)</b></div></div><table class="oc-table"><thead><tr><th>Stock moves</th><th>Stock price</th><th>In 1 day</th><th>In 5 days</th></tr></thead><tbody><tr><th scope="row">down 5%</th><td>$60.97</td><td class="up">$170</td><td class="up">$158</td></tr><tr><th scope="row">down 3%</th><td>$62.25</td><td class="up">$94</td><td class="up">$81</td></tr><tr><th scope="row">down 1%</th><td>$63.54</td><td class="up">$27</td><td class="up">$14</td></tr><tr><th scope="row">up 1%</th><td>$64.82</td><td class="dn">($31)</td><td class="dn">($45)</td></tr><tr><th scope="row">up 3%</th><td>$66.11</td><td class="dn">($81)</td><td class="dn">($94)</td></tr><tr><th scope="row">up 5%</th><td>$67.39</td><td class="dn">($122)</td><td class="dn">($135)</td></tr><tr><th scope="row">up 10%</th><td>$70.60</td><td class="dn">($196)</td><td class="dn">($206)</td></tr></tbody></table><p class="oc-plan"><b>Plan per contract</b> Stop at $1.38 costs about ($139). Target at $4.15 makes about $138.</p><p class="oc-foot">Profit or loss for one contract (100 shares), from an options pricing model that holds implied volatility flat and includes time decay. An estimate, not a prediction. Parentheses mean a loss.</p></aside>

## SPY PUT: Best Available, Tactical
- Why: SPY is 3.3% under its 50 day ($766.40), bouncing into resistance.
- Contract: Dec 18 $740 put, mark $16.89, delta 0.45, IV 19.1%
- Liquidity: Spread 0.2%, open interest 35,874, volume today 2,822, volume to OI 0.08
- Plan: enter only on a failed bounce under $745. Sell within 3 to 5 days or at +50% ($25.34). Stop $8.45 or a close above $752.

<aside class="oc" aria-label="SPY contract detail"><div class="oc-title">SPY $740 put, Dec 18, 42 days left, stock $740.98</div><div class="oc-facts"><div><span>Cost to buy</span><b>$1,689</b></div><div><span>Most you can lose</span><b>$1,689</b></div><div><span>Each $1 the stock moves</span><b>about $45</b></div><div><span>Breakeven at expiry</span><b>$723.11 (down 2.4%)</b></div></div><table class="oc-table"><thead><tr><th>Stock moves</th><th>Stock price</th><th>In 1 day</th><th>In 5 days</th></tr></thead><tbody><tr><th scope="row">down 5%</th><td>$703.93</td><td class="up">$2,226</td><td class="up">$2,181</td></tr><tr><th scope="row">down 3%</th><td>$718.75</td><td class="up">$1,193</td><td class="up">$1,129</td></tr><tr><th scope="row">down 1%</th><td>$733.57</td><td class="up">$339</td><td class="up">$263</td></tr><tr><th scope="row">up 1%</th><td>$748.39</td><td class="dn">($330)</td><td class="dn">($408)</td></tr><tr><th scope="row">up 3%</th><td>$763.21</td><td class="dn">($823)</td><td class="dn">($895)</td></tr><tr><th scope="row">up 5%</th><td>$778.03</td><td class="dn">($1,166)</td><td class="dn">($1,225)</td></tr><tr><th scope="row">up 10%</th><td>$815.08</td><td class="dn">($1,571)</td><td class="dn">($1,595)</td></tr></tbody></table><p class="oc-plan"><b>Plan per contract</b> Stop at $8.45 costs about ($844). Target at $25.34 makes about $845.</p><p class="oc-foot">Profit or loss for one contract (100 shares), from an options pricing model that holds implied volatility flat and includes time decay. An estimate, not a prediction. Parentheses mean a loss.</p></aside>

## QQQ PUT: Best Available, Tactical
- Why: QQQ is 8.4% under its falling 50 day ($722.27), RSI 27 before today.
- Contract: Dec 18 $660 put, mark $23.02, delta 0.46, IV 28.1%
- Liquidity: Spread 1.0%, open interest 39,136, volume today 1,179, volume to OI 0.03
- Plan: enter only on a failed bounce under $665. Stop $11.51 or a close above $675. Target $34.53.

<aside class="oc" aria-label="QQQ contract detail"><div class="oc-title">QQQ $660 put, Dec 18, 42 days left, stock $661.51</div><div class="oc-facts"><div><span>Cost to buy</span><b>$2,302</b></div><div><span>Most you can lose</span><b>$2,302</b></div><div><span>Each $1 the stock moves</span><b>about $46</b></div><div><span>Breakeven at expiry</span><b>$636.98 (down 3.7%)</b></div></div><table class="oc-table"><thead><tr><th>Stock moves</th><th>Stock price</th><th>In 1 day</th><th>In 5 days</th></tr></thead><tbody><tr><th scope="row">down 5%</th><td>$628.43</td><td class="up">$1,821</td><td class="up">$1,733</td></tr><tr><th scope="row">down 3%</th><td>$641.66</td><td class="up">$998</td><td class="up">$897</td></tr><tr><th scope="row">down 1%</th><td>$654.89</td><td class="up">$287</td><td class="up">$178</td></tr><tr><th scope="row">up 1%</th><td>$668.13</td><td class="dn">($312)</td><td class="dn">($423)</td></tr><tr><th scope="row">up 3%</th><td>$681.36</td><td class="dn">($804)</td><td class="dn">($911)</td></tr><tr><th scope="row">up 5%</th><td>$694.59</td><td class="dn">($1,198)</td><td class="dn">($1,296)</td></tr><tr><th scope="row">up 10%</th><td>$727.66</td><td class="dn">($1,832)</td><td class="dn">($1,899)</td></tr></tbody></table><p class="oc-plan"><b>Plan per contract</b> Stop at $11.51 costs about ($1,151). Target at $34.53 makes about $1,151.</p><p class="oc-foot">Profit or loss for one contract (100 shares), from an options pricing model that holds implied volatility flat and includes time decay. An estimate, not a prediction. Parentheses mean a loss.</p></aside>

## Dropped for spread
- AAPL Dec 24 $345C 22%, MSFT Dec 24 $535C 13.7%, XLV Dec 18 $185C 14.5%, SMH Dec 18 $465C 7.5%

## Rejected
- JPM and TSLA calls: under their 50 day.
- NVDA, PLTR, AVGO puts: break even 7.5% to 8.2% away, cap is 5%.
- META, IWM, XLK puts, and the SPY Dec 31 put: volume too low.


</div>
