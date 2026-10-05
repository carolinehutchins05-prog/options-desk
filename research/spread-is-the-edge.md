---
layout: default
title: Leverage is priced, spread is not
description: Four calls at matched delta appeared to offer very different leverage. Adjusted for implied volatility they were identical.
---

<p class="eyebrow">Research &middot; 21 August 2026</p>

# Leverage is priced. Spread is not.

<p class="lede">The intuition I started with was that some underlyings offer more option leverage than others, and that picking the right one is an edge. That intuition is wrong, and it is wrong in a way that can be measured in an afternoon.</p>

## The measurement

I took four calls at near identical delta, 0.39 to 0.42, on underlyings with very different volatility, and computed elasticity: the percentage change in the option for a 1% change in the underlying. That is delta times spot divided by premium.

<div class="scroll" markdown="0">
<table>
<thead><tr><th>Underlying</th><th>Return per 1% move</th><th>&times; implied daily move</th></tr></thead>
<tbody>
<tr><td>SPY</td><td>+94%</td><td class="pass">~+64%</td></tr>
<tr><td>QQQ</td><td>+58%</td><td class="pass">~+62%</td></tr>
<tr><td>PLTR</td><td>+21%</td><td class="pass">~+66%</td></tr>
<tr><td>COIN</td><td>+14%</td><td class="pass">~+68%</td></tr>
</tbody>
</table>
</div>

The first column spans a factor of nearly seven. On that basis SPY looks like the obviously superior vehicle.

The second column multiplies each elasticity by that underlying's own implied daily move, annualised implied volatility divided by the square root of 252. Those four numbers sit within four percentage points of each other.

## What it means

SPY offers enormous leverage **because it barely moves**. COIN offers very little **because it moves constantly**. The product is a constant, and that constant is the market's price for one standard deviation of exposure. Options are priced off volatility, so a cheap option on a quiet name and an expensive option on a wild one deliver the same expected payoff per unit of risk taken.

There is no free leverage to be found by shopping across underlyings. The market already did that arbitrage.

## The consequence for the screen

If leverage is priced identically everywhere, then differences in realised outcome have to come from somewhere that is **not** priced. Transaction cost is the obvious candidate, and on a round trip the bid ask spread is paid twice.

That is why spread sits at the top of the gate list and why the threshold is tight: **5% of mark or less**, and nearer 2% for anything held a day or two. A 10% spread means a position starts 10% down and has to make that back before the thesis contributes anything. No amount of being right about direction compensates for it, because nothing pays you for crossing a wide market.

## A related correction

Quoting an option's sensitivity **per dollar** of underlying move is a rigged comparison. A $1 move is 0.4% on a $250 stock and 2% on a $50 one, so per dollar figures flatter expensive underlyings for no economic reason. Everything here is quoted **per 1%** instead.

## What I still do not know

This was four observations on a single day. The relationship it shows is the standard Black Scholes identity rather than a discovery, which is reassuring for the arithmetic but means the measurement is a confirmation, not evidence of anything novel. The open question is how far it degrades in practice: during a volatility spike, implied volatility and realised volatility separate, and the constant should stop holding. I have not measured that yet.
