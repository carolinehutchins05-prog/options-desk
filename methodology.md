---
layout: default
title: Methodology
description: The thirteen gates every candidate must clear, each with the reason it exists.
---

<p class="eyebrow">Methodology</p>

# Thirteen gates, and why each one is there

<p class="lede">A threshold without a reason is superstition. Every gate below is paired with the thing it rejects and where the number came from. Any candidate failing any single gate is not a trade.</p>

## Direction must agree with trend

Checked before anything else, because it is the cheapest filter and the most violated.

- A **call** requires price above a rising 50 day simple moving average, with 14 day RSI between 45 and 70.
- A **put** requires price below the 50 day.

This exists because of two specific errors. A call was once surfaced on a name trading at $210.96 against a 50 day of $212.91 with RSI 43.9, on the argument that a supertrend reading had flipped positive. Supertrend direction alone is not trend confirmation. Separately, a put was held on a stock sitting 5.6% above its rising 50 day with RSI 56, which is simply a bet against something that is going up.

Both lose for the same reason: the option was asked to overcome the underlying's own drift before it could make money.

## Contract gates

<div class="scroll" markdown="0">
<table>
<thead><tr><th>Gate</th><th>Requirement</th><th>What it rejects</th></tr></thead>
<tbody>
<tr><td><strong>Delta</strong></td><td>0.50 to 0.65</td><td>Cheap far strikes that need an 8% to 24% move. See <a href="research/strike-selection.html">strike selection</a>.</td></tr>
<tr><td><strong>Break even</strong></td><td>within 3% of spot</td><td>Contracts whose arithmetic requires an outlier, not a normal move.</td></tr>
<tr><td><strong>Spread</strong></td><td>5% of mark or less</td><td>The only cost that is not compensated by anything. See <a href="research/spread-is-the-edge.html">spread is the edge</a>.</td></tr>
<tr><td><strong>Implied volatility</strong></td><td>under 40%, over 70 rejected outright</td><td>Paying a volatility premium that decays whether or not the thesis works.</td></tr>
<tr><td><strong>Theta</strong></td><td>under 5% of mark per day</td><td>Positions where the clock beats the thesis. Expressed as a percentage of premium, never in dollars, because dollars are meaningless across different contract prices.</td></tr>
<tr><td><strong>Open interest</strong></td><td>1,000 or more</td><td>Chains nobody trades.</td></tr>
<tr><td><strong>Volume</strong></td><td>500 or more today</td><td>Stale open interest from a crowded strike that has gone quiet.</td></tr>
<tr><td><strong>Bid size and ask size</strong></td><td>20 or more, each</td><td>The trap described in <a href="research/liquidity-traps.html">liquidity traps</a>. This one is invisible in both spread and open interest.</td></tr>
<tr><td><strong>Days to expiry</strong></td><td>21 to 60, third Friday monthly preferred</td><td>The expiry week theta cliff, and the thin spreads on weeklies.</td></tr>
<tr><td><strong>Earnings</strong></td><td>must fall after expiry</td><td>Holding an unreleased print. See <a href="research/event-volatility.html">event volatility</a>.</td></tr>
<tr><td><strong>Recent high</strong></td><td>no 52 week high in the last three sessions</td><td>Entering into a move that has already happened.</td></tr>
<tr><td><strong>Break even ceiling</strong></td><td>must sit below the 52 week high</td><td>Trades that need a new all time high just to return the premium.</td></tr>
<tr><td><strong>Size</strong></td><td>5% to 8% of capital</td><td>Position sizes that make one trade decide the year.</td></tr>
</tbody>
</table>
</div>

## Pacing

Separate from whether any individual trade is good.

- At most **two new positions per week**, at most **one per day**
- At most **six open contracts** at once
- Exit at **+50% on the contract, or five days, whichever comes first**

Pacing limits exist because the failure mode is not holding a loser. It is opening a seventh position because the first six are uncomfortable. The weekly cap is a hard gate in the automation, not a guideline: when it is reached, the screen reports no ideas rather than producing a list that cannot be acted on.

<div class="note">
<span class="h">The expected output</span>
<p>Most runs report <strong>no candidates</strong>. Thirteen conjunctive gates on a universe of roughly 500 names, intersected with a requirement for a specific dated catalyst, will usually produce nothing. A screen that returns something every day has gates that do not bind.</p>
</div>

## Why single leg only

Maximum loss equals premium paid, always, with no assignment risk and no margin interaction. It also keeps the thing being tested small enough to attribute: when a trade loses, the cause is the underlying move, the volatility, the spread, or the clock. Four things, all measurable. A multi leg structure would obscure which one it was, and the point of the log is to find out.
