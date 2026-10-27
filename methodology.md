---
layout: default
title: Methodology
description: The fourteen gates every candidate must clear, each with the reason it exists. Last revised 27 October 2026 after a backtest against the S&P 500.
---

<p class="eyebrow">Methodology</p>

# Fourteen gates, and why each one is there

<p class="lede">A threshold without a reason is superstition. Every gate below is paired with the thing it rejects and where the number came from. Any candidate failing any single gate is not a trade.</p>

<p class="meta">Last revised 27 October 2026 after a <a href="research/backtest.html">backtest against the S&amp;P 500</a>. The rules below are what the screen enforces today.</p>

## Direction must agree with trend

Checked before anything else, because it is the cheapest filter and the most violated.

- A **call** requires price above a rising 50 day simple moving average, with 14 day RSI between 45 and 70.
- **Puts are suspended.** In the backtest the trend gate on the put side lost money in both halves of the sample, and the stocks it selected went up more than average. No put is graded as a candidate until live data shows otherwise.

This exists because of two specific errors. A call was once surfaced on a name trading at $210.96 against a 50 day of $212.91 with RSI 43.9, on the argument that a supertrend reading had flipped positive. Supertrend direction alone is not trend confirmation. Separately, a put was held on a stock sitting 5.6% above its rising 50 day with RSI 56, which is simply a bet against something that is going up.

Both lose for the same reason: the option was asked to overcome the underlying's own drift before it could make money.

**What the evidence says.** A [backtest on 503 S&P 500 stocks](research/backtest.html) found that stocks passing the call gate returned about the same as the index. The gate stays as a filter against fighting the tape, but it is not an edge. A candidate needs a named, dated catalyst as the reason to trade.

## Contract gates

<div class="scroll" markdown="0">
<table>
<thead><tr><th>Gate</th><th>Requirement</th><th>What it rejects</th></tr></thead>
<tbody>
<tr><td><strong>Market regime</strong></td><td>S&amp;P 500 (SPY) above its 200 day average, for any call</td><td>Calls in a falling market. Together with the other changes it cut the worst month in the backtest from an average loss of 55% to 21% in the later half, and from 51% to 37% in the earlier half.</td></tr>
<tr><td><strong>Delta</strong></td><td>0.50 to 0.55, the strike nearest the money</td><td>Cheap far strikes that need an 8% to 24% move, and deep in the money strikes that cost more for no better result. See <a href="research/strike-selection.html">strike selection</a>.</td></tr>
<tr><td><strong>Break even</strong></td><td>within 3% of spot</td><td>Contracts whose arithmetic requires an outlier, not a normal move.</td></tr>
<tr><td><strong>Spread</strong></td><td>3% of mark or less, for every hold</td><td>The only cost that is not compensated by anything. The backtest put calls at break even near a 3.6% spread. See <a href="research/spread-is-the-edge.html">spread is the edge</a> and the <a href="research/backtest.html">backtest</a>.</td></tr>
<tr><td><strong>Implied volatility</strong></td><td>under 40%, over 70 rejected outright</td><td>Paying a volatility premium that decays whether or not the thesis works.</td></tr>
<tr><td><strong>Theta</strong></td><td>under 5% of mark per day</td><td>Positions where the clock beats the thesis. Expressed as a percentage of premium, never in dollars, because dollars are meaningless across different contract prices.</td></tr>
<tr><td><strong>Open interest</strong></td><td>1,000 or more</td><td>Chains nobody trades.</td></tr>
<tr><td><strong>Volume</strong></td><td>500 or more today</td><td>Stale open interest from a crowded strike that has gone quiet.</td></tr>
<tr><td><strong>Bid size and ask size</strong></td><td>20 or more, each</td><td>The trap described in <a href="research/liquidity-traps.html">liquidity traps</a>. This one is invisible in both spread and open interest.</td></tr>
<tr><td><strong>Days to expiry</strong></td><td>45 to 60, third Friday monthly preferred</td><td>Fast time decay and the expiry week cliff. Contracts at 45 days or more lost less than 30 day contracts in both halves of the backtest.</td></tr>
<tr><td><strong>Earnings</strong></td><td>must fall after expiry</td><td>Holding an unreleased print. See <a href="research/event-volatility.html">event volatility</a>.</td></tr>
<tr><td><strong>Recent high</strong></td><td>no 52 week high in the last three sessions</td><td>Entering into a move that has already happened.</td></tr>
<tr><td><strong>Break even ceiling</strong></td><td>must sit below the 52 week high</td><td>Trades that need a new all time high just to return the premium.</td></tr>
<tr><td><strong>Size</strong></td><td>A fixed, small share of capital</td><td>Position sizes that make one trade decide the year.</td></tr>
</tbody>
</table>
</div>

## Exit

Separate from whether any individual trade is good.

- Exit at **+50% on the contract, or five days, whichever comes first**
- Exit at the close if the contract is **down 50% from entry**. In the backtest this cut the average of the worst 10% of trades from a loss of about 83% to about 74%, at a cost of well under one point of average return per trade.

The stop works on closing prices. A gap through it can lose more than 50%, and a single leg option can never lose more than the premium paid.

<div class="note">
<span class="h">The expected output</span>
<p>Most runs report <strong>no candidates</strong>. Fourteen conjunctive gates on a universe of roughly 500 names, intersected with a requirement for a specific dated catalyst, will usually produce nothing. A screen that returns something every day has gates that do not bind.</p>
</div>

## Why single leg only

Maximum loss equals premium paid, always, with no assignment risk and no margin interaction. It also keeps the thing being tested small enough to attribute: when a trade loses, the cause is the underlying move, the volatility, the spread, or the clock. Four things, all measurable. A multi leg structure would obscure which one it was, and the point of the log is to find out.
