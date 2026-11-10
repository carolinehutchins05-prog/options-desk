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

<div class="latest-head"><span class="eyebrow">Latest daily run</span><span class="meta">Premarket Plan, 2026-11-10</span></div>

<div class="report" markdown="1">

# Premarket Calls and Puts, November 10, 2026
Provisional plan on last night's closing chains. The 10:00 AM run confirms on live quotes.

- S&P 500 ETF $754.49, above its 200 day ($728). Calls allowed.
- No Core contract cleared. No monthly expiry sits in the 45 to 60 day window (Dec 18 is 38 days, Jan 15 is 66).
- Futures mixed: Nasdaq proxy down 0.5%, Dow proxy up 0.4%. Chips are the drag again.

## Today's Catalysts
- **TTD**, **OXY**, **CEG**, **NRG**, **TTWO** beat Monday after the close.
- **TDG**, **ONON**, **WIX** beat this morning. **SE**, **HSAI** missed.
- **MARA**, **HIMS**, **RKLB** missed Monday night.
- **CRWV** reports tonight, the next AI capex read.

## Best Available

## UNH CALL: Best Available, Tactical
- Why: health care is the strongest sector premarket, up 0.6%. No dated catalyst, so keep it small.
- Trend: $397.21, above a flat to rising 50 day ($390.74), RSI 48.
- Contract: Dec 18 $400 call, mark $15.35, delta 0.51, IV 30.7%
- Liquidity: Spread 2.0%, open interest 3,795, volume today 543, volume to OI 0.14
- Plan: Dec 18 expiry, sell within about 3 to 5 trading days, or at +50%, stop at 50% down ($7.67). Breakeven $415.35, well under the $461.62 high.

<aside class="oc" aria-label="UNH contract detail"><div class="oc-title">UNH $400 call, Dec 18, 38 days left, stock $397.21</div><div class="oc-facts"><div><span>Cost to buy</span><b>$1,535</b></div><div><span>Most you can lose</span><b>$1,535</b></div><div><span>Each $1 the stock moves</span><b>about $51</b></div><div><span>Breakeven at expiry</span><b>$415.35 (up 4.6%)</b></div></div><table class="oc-table"><thead><tr><th>Stock moves</th><th>Stock price</th><th>In 1 day</th><th>In 5 days</th></tr></thead><tbody><tr><th scope="row">down 5%</th><td>$377.35</td><td class="dn">($832)</td><td class="dn">($909)</td></tr><tr><th scope="row">down 3%</th><td>$385.29</td><td class="dn">($556)</td><td class="dn">($643)</td></tr><tr><th scope="row">down 1%</th><td>$393.24</td><td class="dn">($217)</td><td class="dn">($310)</td></tr><tr><th scope="row">up 1%</th><td>$401.18</td><td class="up">$187</td><td class="up">$90</td></tr><tr><th scope="row">up 3%</th><td>$409.13</td><td class="up">$653</td><td class="up">$557</td></tr><tr><th scope="row">up 5%</th><td>$417.07</td><td class="up">$1,178</td><td class="up">$1,086</td></tr><tr><th scope="row">up 10%</th><td>$436.93</td><td class="up">$2,710</td><td class="up">$2,637</td></tr></tbody></table><p class="oc-plan"><b>Plan per contract</b> Stop at $7.67 costs about ($768). Target at $23.02 makes about $767.</p><p class="oc-foot">Profit or loss for one contract (100 shares), from an options pricing model that holds implied volatility flat and includes time decay. An estimate, not a prediction. Parentheses mean a loss.</p></aside>

## NFLX PUT: Best Available, Tactical
- Why: down trend intact after a 45% slide from its high. Trend puts lose on average in the backtest, so size it small.
- Trend: $63.81, below a falling 50 day ($70.68), RSI 41. Near its $61.39 low from Oct 29.
- Contract: Dec 18 $63 put, mark $2.34, delta 0.42, IV 34.6%
- Liquidity: Spread 2.6%, open interest 8,482, volume today 384, volume to OI 0.05
- Plan: Dec 18 expiry, sell within about 3 to 5 trading days, or at +50%, stop at 50% down ($1.17). Only on a bounce that fails, never into a flush.

<aside class="oc" aria-label="NFLX contract detail"><div class="oc-title">NFLX $63 put, Dec 18, 38 days left, stock $63.81</div><div class="oc-facts"><div><span>Cost to buy</span><b>$234</b></div><div><span>Most you can lose</span><b>$234</b></div><div><span>Each $1 the stock moves</span><b>about $42</b></div><div><span>Breakeven at expiry</span><b>$60.66 (down 4.9%)</b></div></div><table class="oc-table"><thead><tr><th>Stock moves</th><th>Stock price</th><th>In 1 day</th><th>In 5 days</th></tr></thead><tbody><tr><th scope="row">down 5%</th><td>$60.62</td><td class="up">$159</td><td class="up">$146</td></tr><tr><th scope="row">down 3%</th><td>$61.90</td><td class="up">$87</td><td class="up">$73</td></tr><tr><th scope="row">down 1%</th><td>$63.17</td><td class="up">$24</td><td class="up">$10</td></tr><tr><th scope="row">up 1%</th><td>$64.45</td><td class="dn">($29)</td><td class="dn">($43)</td></tr><tr><th scope="row">up 3%</th><td>$65.72</td><td class="dn">($74)</td><td class="dn">($87)</td></tr><tr><th scope="row">up 5%</th><td>$67.00</td><td class="dn">($110)</td><td class="dn">($123)</td></tr><tr><th scope="row">up 10%</th><td>$70.19</td><td class="dn">($174)</td><td class="dn">($183)</td></tr></tbody></table><p class="oc-plan"><b>Plan per contract</b> Stop at $1.17 costs about ($117). Target at $3.51 makes about $117.</p><p class="oc-foot">Profit or loss for one contract (100 shares), from an options pricing model that holds implied volatility flat and includes time decay. An estimate, not a prediction. Parentheses mean a loss.</p></aside>

## SCHW PUT: Best Available, Tactical
- Why: brokers weak while the 50 day rolls over. No dated catalyst. Trend puts lose on average, keep it small.
- Trend: $93.15, below a falling 50 day ($98.14), RSI 49.
- Contract: Jan 15 $95 put, mark $4.88, delta 0.52, IV 26.7%
- Liquidity: Spread 3.1%, open interest 6,035, volume today 115, volume to OI 0.02
- Plan: Jan 15 expiry, sell within about 3 to 5 trading days, or at +50%, stop at 50% down ($2.44). Ex dividend Nov 13.

<aside class="oc" aria-label="SCHW contract detail"><div class="oc-title">SCHW $95 put, Jan 15, 66 days left, stock $93.15</div><div class="oc-facts"><div><span>Cost to buy</span><b>$488</b></div><div><span>Most you can lose</span><b>$488</b></div><div><span>Each $1 the stock moves</span><b>about $52</b></div><div><span>Breakeven at expiry</span><b>$90.12 (down 3.3%)</b></div></div><table class="oc-table"><thead><tr><th>Stock moves</th><th>Stock price</th><th>In 1 day</th><th>In 5 days</th></tr></thead><tbody><tr><th scope="row">down 5%</th><td>$88.49</td><td class="up">$281</td><td class="up">$273</td></tr><tr><th scope="row">down 3%</th><td>$90.36</td><td class="up">$158</td><td class="up">$148</td></tr><tr><th scope="row">down 1%</th><td>$92.22</td><td class="up">$48</td><td class="up">$37</td></tr><tr><th scope="row">up 1%</th><td>$94.08</td><td class="dn">($50)</td><td class="dn">($61)</td></tr><tr><th scope="row">up 3%</th><td>$95.94</td><td class="dn">($134)</td><td class="dn">($145)</td></tr><tr><th scope="row">up 5%</th><td>$97.81</td><td class="dn">($206)</td><td class="dn">($217)</td></tr><tr><th scope="row">up 10%</th><td>$102.47</td><td class="dn">($337)</td><td class="dn">($346)</td></tr></tbody></table><p class="oc-plan"><b>Plan per contract</b> Stop at $2.44 costs about ($244). Target at $7.31 makes about $243.</p><p class="oc-foot">Profit or loss for one contract (100 shares), from an options pricing model that holds implied volatility flat and includes time decay. An estimate, not a prediction. Parentheses mean a loss.</p></aside>

## Rejected, and why
- **TTD** call: IV 85%, bid size 1, stock down 7% premarket despite the beat.
- **TTWO** call: 50 day is falling ($206.97).
- **OXY** call: below a falling 50 day ($59.99), RSI 32.
- **CEG** call: 50 day falling, premarket $267 is under it.
- **TDG**: over $1,000 a share.
- **SBUX** call: printed a 52 week high Nov 5, breakeven above it.
- **DAL** call: breakeven $96.33 sits above the $95.68 high.
- **HIMS** put: IV 92%.
- **MARA** put: sub $7 miner, not graded.
- **CRWV**: reports tonight, inside the holding window.

## Dropped for spread
- **ONON** Jan $37.50C 9.2%, **SE** Dec $75P 45%

One clean tactical call and two small tactical puts. A chip rebound after **CRWV** tonight would undo the put side.

</div>
