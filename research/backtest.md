---
layout: default
title: The screen against the S&P 500
description: A backtest of the trend gate and the contract rules on 503 S&P 500 stocks over ten years, with the index as the benchmark. The trend gate showed no edge.
---

<p class="eyebrow">Research &middot; 26 October 2026</p>

# The screen against the S&P 500

<p class="lede">I tested the mechanical part of the screen on every stock in the S&P 500 over ten years, with the index itself as the benchmark. The trend gate did not beat the index. The contract rules did not make money after realistic costs. Spread turned out to decide almost everything.</p>

## What was tested, and what was not

Every rule was fixed before any result was seen, and nothing was tuned afterward. The test uses the rules exactly as written on the methodology page.

- **Universe:** 503 stocks in the index today, daily prices from mid 2015 through 23 October 2026, with SPY as the S&P 500 benchmark. About 418,000 call signals and 314,000 put signals.
- **Entry and exit:** next session open, exit at plus 50% on the contract or the close of the fifth session, whichever comes first. Round trip cost of 2% each way.
- **Real data:** the trend gate, the RSI band and the recent high gate, tested on actual stock prices.
- **Modeled:** option prices. No free source has historical option chains, so contracts were priced with an options pricing model, delta 0.55, 30 days to expiry, using each stock's recent volatility with a 15% premium on top.
- **Not testable:** spread, open interest, volume, bid size and the earnings gate. These need real chains.

The result describes the mechanical screen. It cannot see a catalyst such as an insider purchase, an earnings gap or a sector rotation, and the daily runs are driven by catalysts.

## Finding one: the trend gate matched the index

<div class="kpi">
  <div><span class="n">+1.02%</span><span class="l">Average 21 day return of stocks passing the call trend gate</span></div>
  <div><span class="n">+1.03%</span><span class="l">The S&P 500 over the same windows</span></div>
  <div><span class="n">+2.19%</span><span class="l">Stocks passing the put trend gate went up, against +1.76% for the index</span></div>
</div>

Buying stocks that sit above a rising 50 day average with a healthy RSI returned the same as buying the index. Over 21 days the call signal trailed the average S&P 500 stock by 0.18 percentage points, a small gap that is statistically different from zero but economically trivial.

The put side was worse. Stocks below a falling 50 day average went up more than the average stock, by 0.26 points over 21 days. On average the put gate pointed the wrong way, which is consistent with oversold names bouncing in a market that rose for most of the decade.

<div class="scroll" markdown="0">
<table>
<thead><tr><th>21 trading days after the signal</th><th>Signals</th><th>Stock</th><th>S&amp;P 500</th><th>Edge over the average stock</th></tr></thead>
<tbody>
<tr><td>Call trend gate</td><td>418,058</td><td>+1.02%</td><td>+1.03%</td><td class="fail">(0.18%), range (0.35%) to (0.02%)</td></tr>
<tr><td>Put trend gate</td><td>313,896</td><td>+2.19%</td><td>+1.76%</td><td class="fail">+0.26% the wrong way, range 0.00% to +0.52%</td></tr>
</tbody>
</table>
</div>

At five days the picture is the same: no measurable difference from an average stock. Ranges are 95% intervals resampled by calendar month, because signals on the same stock on adjacent days are not independent.

## Finding two: after costs the calls break even and the puts lose

<div class="scroll" markdown="0">
<table>
<thead><tr><th>Modeled contract, per trade</th><th>Trades</th><th>Average return</th><th>Win rate</th><th>Hit the +50% exit</th></tr></thead>
<tbody>
<tr><td>Calls on the screen</td><td>117,754</td><td>(0.4%), range (2.7%) to +1.9%</td><td>45%</td><td>26%</td></tr>
<tr><td>Same call on any S&amp;P stock, any day</td><td>340,526</td><td>(0.4%)</td><td>45%</td><td>27%</td></tr>
<tr><td>Same call on SPY, every day</td><td>893</td><td>+1.4%, range (4.5%) to +7.7%</td><td>52%</td><td>30%</td></tr>
<tr><td>Puts on the screen</td><td>185,813</td><td class="fail">(6.1%), range (8.5%) to (3.7%)</td><td>38%</td><td>21%</td></tr>
<tr><td>Same put on any S&amp;P stock, any day</td><td>865,893</td><td>(5.3%)</td><td>38%</td><td>21%</td></tr>
<tr><td>Same put on SPY, every day</td><td>2,503</td><td>(8.4%)</td><td>33%</td><td>19%</td></tr>
</tbody>
</table>
</div>

Only 893 days pass the modeled gates on SPY, so that row is noisy. The screen's calls did exactly as well as the same contract on a random stock on a random day, so the trend gate added nothing measurable. Calls were not significantly different from zero in any of three sub periods. The puts lost money in every period and at every setting tested, which is why they are tactical only. Only with zero trading cost did they reach roughly break even (a loss of 2.3%, with a range that includes zero).

## Finding three: spread decides it

For calls, the average return per trade moves almost one for one with the cost of getting in and out.

<div class="scroll" markdown="0">
<table>
<thead><tr><th>Cost each way, as a share of the premium</th><th>Average call return per trade</th></tr></thead>
<tbody>
<tr><td>0%</td><td class="pass">+3.7%, range +1.3% to +6.1%</td></tr>
<tr><td>2%, the base case</td><td>(0.4%)</td></tr>
<tr><td>4%</td><td class="fail">(4.3%), range (6.4%) to (2.1%)</td></tr>
</tbody>
</table>
</div>

Calls break even at about 1.8% each way, which is a quoted spread near **3.6% of the mark**. The old gate allowed 5% for a multi day hold. At 5% the modeled call loses roughly 1.4% per trade on average before anything else goes wrong. That is the same lesson as the [leverage and spread note](spread-is-the-edge.html), now measured on ten years of stocks.

## Finding four: what actually reduces losses

A second test asked which rule changes cut losses. I split the data in two, 2016 to 2021 and 2022 to October 2026, tried a small set of changes one at a time, and checked that a change helped in both halves before keeping it. The puts were excluded from this step because they lost in both halves anyway.

<div class="scroll" markdown="0">
<table>
<thead><tr><th>Change to the call rules</th><th>Average per trade, 2016 to 2021</th><th>Average per trade, 2022 to 2026</th><th>Verdict</th></tr></thead>
<tbody>
<tr><td>Baseline: 30 days to expiry, delta 0.55</td><td>+0.5%</td><td>(1.8%)</td><td></td></tr>
<tr><td>45 days to expiry</td><td>+1.2%</td><td>+0.1%</td><td class="pass">Better in both, kept</td></tr>
<tr><td>Delta 0.50, nearest the money</td><td>+1.9%</td><td>+0.4%</td><td class="pass">Better in both, kept</td></tr>
<tr><td>Delta 0.65</td><td>(1.0%)</td><td>(3.1%)</td><td class="fail">Worse in both, rejected</td></tr>
<tr><td>Calls only when the S&amp;P 500 is above its 200 day average</td><td>+0.5%</td><td>(1.0%)</td><td class="pass">Better, and it cut the worst month, kept</td></tr>
<tr><td>Stop at 50% down on the contract</td><td>(0.2%)</td><td>(2.0%)</td><td>Costs under a point, shrinks the worst trades, kept</td></tr>
<tr><td>Stop at 30% down</td><td>(0.9%)</td><td>(2.5%)</td><td class="fail">Triggers on noise, rejected</td></tr>
<tr><td>Hold 10 days instead of 5</td><td>+4.3%</td><td>+0.1%</td><td class="fail">Higher average, but the worst 10% of trades lose about 96%, rejected</td></tr>
</tbody>
</table>
</div>

The combination of the kept changes, a 45 to 60 day contract at delta 0.50 with the market filter and the 50% stop:

<div class="scroll" markdown="0">
<table>
<thead><tr><th></th><th>Trades</th><th>Average per trade</th><th>Worst 10% of trades</th><th>Worst month</th></tr></thead>
<tbody>
<tr><td>Old call rules, 2016 to 2021</td><td>73,219</td><td>+0.5%</td><td>(83%)</td><td>(51%)</td></tr>
<tr><td>New call rules, 2016 to 2021</td><td>15,541</td><td>+2.6%</td><td>(73%)</td><td>(37%)</td></tr>
<tr><td>Old call rules, 2022 to 2026</td><td>44,503</td><td>(1.8%)</td><td>(83%)</td><td>(55%)</td></tr>
<tr><td>New call rules, 2022 to 2026</td><td>4,108</td><td>+1.0%</td><td>(74%)</td><td>(21%)</td></tr>
</tbody>
</table>
</div>

Read this carefully. The gain is consistent in both halves, but it is small and the ranges still include zero, so it is not proof of an edge. It also removes most trades, 79% fewer in the earlier half and 91% fewer in the later one. What it does reliably is shrink the worst outcomes. The share of trades that lose 30% or more did not improve, because a stop cannot stop a trade from being a loser, only from being a bigger one.

One result was rejected on purpose. The method I set up in advance would have combined a 60 day contract, a 10 day hold and a 100% target, and that combination showed an average of +17.6% in the earlier half. It left only a few hundred trades in the later half, all on the quietest stocks, and looks like an artifact of pricing options off recent volatility. I did not adopt it.

Two honesty notes. The kept changes were chosen after reading the one at a time results, so the later half is a check on consistency and not a clean out of sample test. And the numbers are still modeled option prices.

## How much to trust this

- **Survivorship bias.** Only stocks in the index today are tested, which flatters long signals. The true result for calls is, if anything, a little worse.
- **Constant volatility.** The model holds implied volatility flat. Real options gain or lose value as volatility moves, and that is not captured.
- **The contract gates look helpful in the model, but do not rely on that.** With no modeled gates the call average is (3.1%) against (0.4%) with them. Part of that gap is probably an artifact: the model prices options from recent realized volatility, and quiet stocks tend to get more volatile, which flatters low volatility picks. Real chains would price that in.
- **Volatility premium.** If the volatility priced into options equals realized volatility the calls make +1.9% per trade. At 30% above realized they lose 1.9%. The result depends on an assumption that cannot be pinned down without real chains.
- **Tuning.** The first test used the rules as written, which came from live mistakes in 2026 and not from searching this data. The second test tried a small set of changes, and how they were chosen is described in finding four.

## What changed

1. **Puts are tactical only.** They lost in both halves of the sample and at every setting tested, so they are short, small and never the core idea.
2. **Calls only when the S&P 500 is above its 200 day average.**
3. **Contracts expire in 45 to 60 days, not 21 to 60, and the strike is the one nearest the money, delta 0.50 to 0.55.**
4. **A stop at 50% down on the contract, on top of the existing exit at +50% or five days.**
5. **The spread gate is 3% of the mark for every hold.** It was 5% for a multi day hold.
6. **The trend gate is described as a filter, not an edge.** A candidate needs a named, dated catalyst as the reason to trade.
7. **A real chain archive is the next step.** Until the daily runs have collected enough live chains to test spread, open interest and volume directly, the contract level results stay modeled.

The code and full results are in the [backtest folder on GitHub](https://github.com/carolinehutchins05-prog/options-desk/tree/main/backtest).
