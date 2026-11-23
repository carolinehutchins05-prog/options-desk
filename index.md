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

<div class="latest-head"><span class="eyebrow">Latest daily run</span><span class="meta">Premarket Plan, 2026-11-23</span></div>

<div class="report" markdown="1">

# Premarket Calls and Puts, November 23, 2026
> Provisional plan on Friday's closing chains and the 3:35 PM board, priced against 9:22 AM premarket quotes. The 10:00 AM run confirms on live quotes.

## Market Gate
- SPY closed Friday at $689.81 against a 200 day of $730.29. Premarket $722 is still below it, so no Core call clears today.
- Tape is a relief gap after the Nasdaq's worst week since 2020: SPY up 4.7%, QQQ up 7.2% premarket.

## Today's Catalysts
- **NVDA**: Trump urged the board to rehire Jensen Huang, WSJ says he is willing. SEC probe still open.
- **PDD** beat, $3.14 vs $2.69. **INTU** $2.91 vs $2.61, **KEYS** $3.61 vs $3.32, **ESTC** $0.94 vs $0.68.
- **BABA** missed, $1.21 vs $1.64. **NTES** missed, $2.12 vs $2.49.
- **CRWD** bid for Zscaler, ZS up about 20%.
- Reporting tonight: ZM, A, J, SYM, SMTC.

## Best Available

## AAPL CALL: Best Available, Tactical
- Why: no dated catalyst. The one megacap still above a rising 50 day through the rout, and the board's top liquid call.
- Trend: $342.56 close vs 50 day $341.81 and rising, RSI 47, supertrend up. Premarket $347.
- Contract: Dec 18 $350 call, mark $8.40, delta 0.48, IV 25.2%, provisional closing marks
- Liquidity: Spread 3.4% at the 3:35 PM board, 11.9% at the close, open interest 30,680, volume 5,759, volume to OI 0.19
- Break even $358.40, 3.3% above spot and below the 52 week high of $360.83.
- Plan: Dec 18 expiry, sell within about 3 to 5 trading days, or at +50% ($12.60), stop at 50% down ($4.20). Spread must print 4% or less at 10 AM.

<aside class="oc" aria-label="AAPL contract detail"><div class="oc-title">AAPL $350 call, Dec 18, 25 days left, stock $347.00</div><div class="oc-facts"><div><span>Cost to buy</span><b>$840</b></div><div><span>Most you can lose</span><b>$840</b></div><div><span>Each $1 the stock moves</span><b>about $48</b></div><div><span>Breakeven at expiry</span><b>$358.40 (up 3.3%)</b></div></div><table class="oc-table"><thead><tr><th>Stock moves</th><th>Stock price</th><th>In 1 day</th><th>In 5 days</th></tr></thead><tbody><tr><th scope="row">down 5%</th><td>$329.65</td><td class="dn">($599)</td><td class="dn">($654)</td></tr><tr><th scope="row">down 3%</th><td>$336.59</td><td class="dn">($425)</td><td class="dn">($496)</td></tr><tr><th scope="row">down 1%</th><td>$343.53</td><td class="dn">($176)</td><td class="dn">($259)</td></tr><tr><th scope="row">up 1%</th><td>$350.47</td><td class="up">$155</td><td class="up">$67</td></tr><tr><th scope="row">up 3%</th><td>$357.41</td><td class="up">$568</td><td class="up">$483</td></tr><tr><th scope="row">up 5%</th><td>$364.35</td><td class="up">$1,056</td><td class="up">$979</td></tr><tr><th scope="row">up 10%</th><td>$381.70</td><td class="up">$2,521</td><td class="up">$2,476</td></tr></tbody></table><p class="oc-plan"><b>Plan per contract</b> Stop at $4.20 costs about ($420). Target at $12.60 makes about $420.</p><p class="oc-foot">Profit or loss for one contract (100 shares), from an options pricing model that holds implied volatility flat and includes time decay. An estimate, not a prediction. Parentheses mean a loss.</p></aside>

## CVX PUT: Best Available, Tactical
- Why: energy is the only sector lagging a risk on gap, CVX is red premarket while SPY is up 4.7%. No dated catalyst.
- Trend: $208.37 close vs falling 50 day $215.38, RSI 40, supertrend down. Premarket $207.40.
- Contract: Dec 18 $210 put, mark $7.78, delta 0.51, IV 33.1%, provisional closing marks
- Liquidity: Spread 1.9%, open interest 4,620, volume 1,207, volume to OI 0.26. Bid and ask size only 6 and 5.
- Break even $202.22, 2.5% below spot. Reports after expiry.
- Plan: Dec 18 expiry, sell within about 3 to 5 trading days, or at +50% ($11.67), stop at 50% down ($3.89). Trend puts lose on average in the backtest, keep it small.

<aside class="oc" aria-label="CVX contract detail"><div class="oc-title">CVX $210 put, Dec 18, 25 days left, stock $207.40</div><div class="oc-facts"><div><span>Cost to buy</span><b>$778</b></div><div><span>Most you can lose</span><b>$778</b></div><div><span>Each $1 the stock moves</span><b>about $51</b></div><div><span>Breakeven at expiry</span><b>$202.22 (down 2.5%)</b></div></div><table class="oc-table"><thead><tr><th>Stock moves</th><th>Stock price</th><th>In 1 day</th><th>In 5 days</th></tr></thead><tbody><tr><th scope="row">down 5%</th><td>$197.03</td><td class="up">$667</td><td class="up">$634</td></tr><tr><th scope="row">down 3%</th><td>$201.18</td><td class="up">$366</td><td class="up">$324</td></tr><tr><th scope="row">down 1%</th><td>$205.33</td><td class="up">$104</td><td class="up">$54</td></tr><tr><th scope="row">up 1%</th><td>$209.47</td><td class="dn">($118)</td><td class="dn">($171)</td></tr><tr><th scope="row">up 3%</th><td>$213.62</td><td class="dn">($298)</td><td class="dn">($350)</td></tr><tr><th scope="row">up 5%</th><td>$217.77</td><td class="dn">($439)</td><td class="dn">($488)</td></tr><tr><th scope="row">up 10%</th><td>$228.14</td><td class="dn">($654)</td><td class="dn">($685)</td></tr></tbody></table><p class="oc-plan"><b>Plan per contract</b> Stop at $3.89 costs about ($389). Target at $11.67 makes about $389.</p><p class="oc-foot">Profit or loss for one contract (100 shares), from an options pricing model that holds implied volatility flat and includes time decay. An estimate, not a prediction. Parentheses mean a loss.</p></aside>

## Closest Misses
- Calls: **MO** Jan 15 $75C blocked by volume (96, needs 100). **PDD** Jan 15 $85C blocked by spread.
- Puts: **NFLX** Jan 15 $58P break even now 7.5% away after the bounce. **BA** Jan 15 $160P break even 6.4% away.

## Dropped for spread
- PDD $85C 12.9%, WMT $125C 6.8%, BA $160P 7.0%, NTES $100P 37%

## Rejected, and why
- **NVDA** call: far below a falling 50 day ($207), RSI 15.
- **INTU**, **KEYS**, **ESTC** calls: earnings beats, but all below a falling 50 day.
- **CMCSA** call: 50 day is flat to falling.
- **WMT** call: Jan $125C delta 0.63, out of band.
- **BABA** put: IV 72%, over the 70% instant reject. Printed a 52 week low Friday.
- **NTES** put: open interest 722.
- **AXP**, **CSCO** puts: premarket bounce pushes break even past 5%.
- **TSLA** put: premarket $374.50 is back at its 50 day ($375.64).
- **ADBE** put: Dec $230P now in the money, delta over 0.60. Reports Dec 9, sell before.
- **QQQ**: ETF. **CRWD**: earnings about Dec 1, inside the holding window. Tonight's reporters: inside the window.

A short covering gap into a holiday week can fade fast. A green close in semis invalidates the CVX put idea only if energy joins the bid.

</div>
