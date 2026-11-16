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

<div class="latest-head"><span class="eyebrow">Latest daily run</span><span class="meta">Premarket Plan, 2026-11-16</span></div>

<div class="report" markdown="1">

# Premarket Calls and Puts, November 16, 2026
Provisional plan on Friday closing chains. The 10:00 AM run confirms on live quotes.

## Today's Catalysts
- Chips selling hard premarket, SMH down 3.95%, MU down 6% on AI spend and China memory worries
- NVDA CEO stepped down, earnings Tue Nov 17 after close
- COIN and HOOD down 5 to 6% on a crypto broker selloff
- Health care and staples lead, UNH up 1% premarket
- SPY above its 200 day, so calls are allowed. No Core call cleared, all liquid near money calls are 35 days out

## Best Available
Puts are tactical only. The backtest shows trend puts lose on average, keep them small.

## CVX CALL: Best Available, Tactical
- Why: energy holding above a rising 50 day while tech sells off
- Trend: above 50 day, RSI 52
- Contract: Dec 18 $220 call, mark $6.62, delta 0.53, IV 23.1%
- Liquidity: Spread 2.3%, open interest 5,537, volume 2,172, volume to OI 0.39
- Plan: Dec 18 expiry, sell within about 3 to 5 trading days, or at +50%, stop at 50% down ($3.31)

<aside class="oc" aria-label="CVX contract detail"><div class="oc-title">CVX $220 call, Dec 18, 32 days left, stock $219.89</div><div class="oc-facts"><div><span>Cost to buy</span><b>$662</b></div><div><span>Most you can lose</span><b>$662</b></div><div><span>Each $1 the stock moves</span><b>about $53</b></div><div><span>Breakeven at expiry</span><b>$226.62 (up 3.1%)</b></div></div><table class="oc-table"><thead><tr><th>Stock moves</th><th>Stock price</th><th>In 1 day</th><th>In 5 days</th></tr></thead><tbody><tr><th scope="row">down 5%</th><td>$208.90</td><td class="dn">($441)</td><td class="dn">($474)</td></tr><tr><th scope="row">down 3%</th><td>$213.29</td><td class="dn">($305)</td><td class="dn">($346)</td></tr><tr><th scope="row">down 1%</th><td>$217.69</td><td class="dn">($122)</td><td class="dn">($167)</td></tr><tr><th scope="row">up 1%</th><td>$222.09</td><td class="up">$112</td><td class="up">$66</td></tr><tr><th scope="row">up 3%</th><td>$226.49</td><td class="up">$393</td><td class="up">$349</td></tr><tr><th scope="row">up 5%</th><td>$230.88</td><td class="up">$716</td><td class="up">$677</td></tr><tr><th scope="row">up 10%</th><td>$241.88</td><td class="up">$1,661</td><td class="up">$1,637</td></tr></tbody></table><p class="oc-plan"><b>Plan per contract</b> Stop at $3.31 costs about ($331). Target at $9.93 makes about $331.</p><p class="oc-foot">Profit or loss for one contract (100 shares), from an options pricing model that holds implied volatility flat and includes time decay. An estimate, not a prediction. Parentheses mean a loss.</p></aside>

## UNH CALL: Best Available, Tactical
- Why: health care is the top sector premarket
- Trend: above a rising 50 day, RSI 55
- Contract: Dec 18 $410 call, mark $14.40, delta 0.51, IV 29.6%
- Liquidity: Spread 3.5%, open interest 2,366, volume 208, volume to OI 0.09
- Plan: Dec 18 expiry, sell within about 3 to 5 trading days, or at +50%, stop at 50% down ($7.20)

<aside class="oc" aria-label="UNH contract detail"><div class="oc-title">UNH $410 call, Dec 18, 32 days left, stock $407.46</div><div class="oc-facts"><div><span>Cost to buy</span><b>$1,440</b></div><div><span>Most you can lose</span><b>$1,440</b></div><div><span>Each $1 the stock moves</span><b>about $51</b></div><div><span>Breakeven at expiry</span><b>$424.40 (up 4.2%)</b></div></div><table class="oc-table"><thead><tr><th>Stock moves</th><th>Stock price</th><th>In 1 day</th><th>In 5 days</th></tr></thead><tbody><tr><th scope="row">down 5%</th><td>$387.09</td><td class="dn">($832)</td><td class="dn">($916)</td></tr><tr><th scope="row">down 3%</th><td>$395.24</td><td class="dn">($563)</td><td class="dn">($658)</td></tr><tr><th scope="row">down 1%</th><td>$403.39</td><td class="dn">($223)</td><td class="dn">($327)</td></tr><tr><th scope="row">up 1%</th><td>$411.53</td><td class="up">$189</td><td class="up">$82</td></tr><tr><th scope="row">up 3%</th><td>$419.68</td><td class="up">$672</td><td class="up">$566</td></tr><tr><th scope="row">up 5%</th><td>$427.83</td><td class="up">$1,220</td><td class="up">$1,120</td></tr><tr><th scope="row">up 10%</th><td>$448.21</td><td class="up">$2,828</td><td class="up">$2,754</td></tr></tbody></table><p class="oc-plan"><b>Plan per contract</b> Stop at $7.20 costs about ($720). Target at $21.60 makes about $720.</p><p class="oc-foot">Profit or loss for one contract (100 shares), from an options pricing model that holds implied volatility flat and includes time decay. An estimate, not a prediction. Parentheses mean a loss.</p></aside>

## XOM CALL: Best Available, Tactical
- Why: energy above its 50 day, no dated catalyst
- Trend: above 50 day, RSI 48
- Contract: Dec 18 $170 call, mark $5.90, delta 0.55, IV 25.1%
- Liquidity: Spread 3.4%, open interest 9,048, volume 349, volume to OI 0.04
- Plan: Dec 18 expiry, sell within about 3 to 5 trading days, or at +50%, stop at 50% down ($2.95)

<aside class="oc" aria-label="XOM contract detail"><div class="oc-title">XOM $170 call, Dec 18, 32 days left, stock $170.59</div><div class="oc-facts"><div><span>Cost to buy</span><b>$590</b></div><div><span>Most you can lose</span><b>$590</b></div><div><span>Each $1 the stock moves</span><b>about $55</b></div><div><span>Breakeven at expiry</span><b>$175.90 (up 3.1%)</b></div></div><table class="oc-table"><thead><tr><th>Stock moves</th><th>Stock price</th><th>In 1 day</th><th>In 5 days</th></tr></thead><tbody><tr><th scope="row">down 5%</th><td>$162.06</td><td class="dn">($368)</td><td class="dn">($398)</td></tr><tr><th scope="row">down 3%</th><td>$165.47</td><td class="dn">($251)</td><td class="dn">($286)</td></tr><tr><th scope="row">down 1%</th><td>$168.88</td><td class="dn">($99)</td><td class="dn">($137)</td></tr><tr><th scope="row">up 1%</th><td>$172.30</td><td class="up">$89</td><td class="up">$51</td></tr><tr><th scope="row">up 3%</th><td>$175.71</td><td class="up">$311</td><td class="up">$274</td></tr><tr><th scope="row">up 5%</th><td>$179.12</td><td class="up">$563</td><td class="up">$530</td></tr><tr><th scope="row">up 10%</th><td>$187.65</td><td class="up">$1,291</td><td class="up">$1,270</td></tr></tbody></table><p class="oc-plan"><b>Plan per contract</b> Stop at $2.95 costs about ($295). Target at $8.85 makes about $295.</p><p class="oc-foot">Profit or loss for one contract (100 shares), from an options pricing model that holds implied volatility flat and includes time decay. An estimate, not a prediction. Parentheses mean a loss.</p></aside>

## HOOD PUT: Best Available, Tactical
- Why: crypto broker selloff, down 5.3% premarket
- Trend: far below a falling 50 day, RSI 33
- Contract: Dec 18 $75 put, mark $4.68, delta 0.51, IV 47.8%
- Liquidity: Spread 3.2%, open interest 9,866, volume 1,596, volume to OI 0.16
- Plan: Dec 18 expiry, sell within about 3 to 5 trading days, or at +50%, stop at 50% down ($2.34)

<aside class="oc" aria-label="HOOD contract detail"><div class="oc-title">HOOD $75 put, Dec 18, 32 days left, stock $73.75</div><div class="oc-facts"><div><span>Cost to buy</span><b>$468</b></div><div><span>Most you can lose</span><b>$468</b></div><div><span>Each $1 the stock moves</span><b>about $51</b></div><div><span>Breakeven at expiry</span><b>$70.32 (down 4.7%)</b></div></div><table class="oc-table"><thead><tr><th>Stock moves</th><th>Stock price</th><th>In 1 day</th><th>In 5 days</th></tr></thead><tbody><tr><th scope="row">down 5%</th><td>$70.06</td><td class="up">$209</td><td class="up">$188</td></tr><tr><th scope="row">down 3%</th><td>$71.54</td><td class="up">$117</td><td class="up">$93</td></tr><tr><th scope="row">down 1%</th><td>$73.01</td><td class="up">$33</td><td class="up">$8</td></tr><tr><th scope="row">up 1%</th><td>$74.49</td><td class="dn">($43)</td><td class="dn">($68)</td></tr><tr><th scope="row">up 3%</th><td>$75.96</td><td class="dn">($110)</td><td class="dn">($136)</td></tr><tr><th scope="row">up 5%</th><td>$77.44</td><td class="dn">($169)</td><td class="dn">($194)</td></tr><tr><th scope="row">up 10%</th><td>$81.12</td><td class="dn">($283)</td><td class="dn">($306)</td></tr></tbody></table><p class="oc-plan"><b>Plan per contract</b> Stop at $2.34 costs about ($234). Target at $7.02 makes about $234.</p><p class="oc-foot">Profit or loss for one contract (100 shares), from an options pricing model that holds implied volatility flat and includes time decay. An estimate, not a prediction. Parentheses mean a loss.</p></aside>

## NOW PUT: Best Available, Tactical
- Why: software below a falling 50 day as tech leads lower
- Trend: below 50 day, RSI 31
- Contract: Dec 18 $105 put, mark $7.25, delta 0.53, IV 47.1%
- Liquidity: Spread 2.8%, open interest 3,670, volume 202, volume to OI 0.06
- Plan: Dec 18 expiry, sell within about 3 to 5 trading days, or at +50%, stop at 50% down ($3.62)

<aside class="oc" aria-label="NOW contract detail"><div class="oc-title">NOW $105 put, Dec 18, 32 days left, stock $102.25</div><div class="oc-facts"><div><span>Cost to buy</span><b>$725</b></div><div><span>Most you can lose</span><b>$725</b></div><div><span>Each $1 the stock moves</span><b>about $53</b></div><div><span>Breakeven at expiry</span><b>$97.75 (down 4.4%)</b></div></div><table class="oc-table"><thead><tr><th>Stock moves</th><th>Stock price</th><th>In 1 day</th><th>In 5 days</th></tr></thead><tbody><tr><th scope="row">down 5%</th><td>$97.14</td><td class="up">$301</td><td class="up">$271</td></tr><tr><th scope="row">down 3%</th><td>$99.18</td><td class="up">$169</td><td class="up">$136</td></tr><tr><th scope="row">down 1%</th><td>$101.23</td><td class="up">$48</td><td class="up">$13</td></tr><tr><th scope="row">up 1%</th><td>$103.27</td><td class="dn">($62)</td><td class="dn">($99)</td></tr><tr><th scope="row">up 3%</th><td>$105.32</td><td class="dn">($160)</td><td class="dn">($198)</td></tr><tr><th scope="row">up 5%</th><td>$107.36</td><td class="dn">($248)</td><td class="dn">($285)</td></tr><tr><th scope="row">up 10%</th><td>$112.48</td><td class="dn">($421)</td><td class="dn">($456)</td></tr></tbody></table><p class="oc-plan"><b>Plan per contract</b> Stop at $3.62 costs about ($363). Target at $10.88 makes about $363.</p><p class="oc-foot">Profit or loss for one contract (100 shares), from an options pricing model that holds implied volatility flat and includes time decay. An estimate, not a prediction. Parentheses mean a loss.</p></aside>

## FCX PUT: Best Available, Tactical
- Why: copper names below a falling 50 day, no dated catalyst
- Trend: below 50 day, RSI 37
- Contract: Dec 18 $60 put, mark $3.60, delta 0.50, IV 45.4%
- Liquidity: Spread 2.8%, open interest 14,789, volume 195, volume to OI 0.01
- Plan: Dec 18 expiry, sell within about 3 to 5 trading days, or at +50%, stop at 50% down ($1.80)

<aside class="oc" aria-label="FCX contract detail"><div class="oc-title">FCX $60 put, Dec 18, 32 days left, stock $59.24</div><div class="oc-facts"><div><span>Cost to buy</span><b>$360</b></div><div><span>Most you can lose</span><b>$360</b></div><div><span>Each $1 the stock moves</span><b>about $50</b></div><div><span>Breakeven at expiry</span><b>$56.40 (down 4.8%)</b></div></div><table class="oc-table"><thead><tr><th>Stock moves</th><th>Stock price</th><th>In 1 day</th><th>In 5 days</th></tr></thead><tbody><tr><th scope="row">down 5%</th><td>$56.28</td><td class="up">$165</td><td class="up">$147</td></tr><tr><th scope="row">down 3%</th><td>$57.46</td><td class="up">$92</td><td class="up">$73</td></tr><tr><th scope="row">down 1%</th><td>$58.65</td><td class="up">$26</td><td class="up">$6</td></tr><tr><th scope="row">up 1%</th><td>$59.83</td><td class="dn">($34)</td><td class="dn">($54)</td></tr><tr><th scope="row">up 3%</th><td>$61.02</td><td class="dn">($86)</td><td class="dn">($107)</td></tr><tr><th scope="row">up 5%</th><td>$62.20</td><td class="dn">($132)</td><td class="dn">($152)</td></tr><tr><th scope="row">up 10%</th><td>$65.16</td><td class="dn">($221)</td><td class="dn">($239)</td></tr></tbody></table><p class="oc-plan"><b>Plan per contract</b> Stop at $1.80 costs about ($180). Target at $5.40 makes about $180.</p><p class="oc-foot">Profit or loss for one contract (100 shares), from an options pricing model that holds implied volatility flat and includes time decay. An estimate, not a prediction. Parentheses mean a loss.</p></aside>

## Dropped for spread
- MU $740P 7.2%, TSM $380P 10.9%

## Rejected
- NVDA: earnings Nov 17 fall inside the holding window
- AVGO $330P: break even 5.3% below spot
- COIN $120P: IV 71.7%, instant reject
- AAPL, SWKS, HUM calls: fresh 52 week highs, gate 5
- BIDU call: below a falling 50 day despite the earnings beat

Tape is rotating out of chips into health care ahead of NVDA earnings. A semis reversal at the open invalidates the put side.

</div>
