---
layout: default
title: What an earnings print actually pays for
description: A case study where the earnings beat was irrelevant, implied volatility was more than double the realised move, and one of my two predictions was wrong.
---

<p class="eyebrow">Research &middot; 30 September to 2 October 2026</p>

# What an earnings print actually pays for

<p class="lede">A memory manufacturer reported on 30 September 2026. I made two calls going in. One was right for the reason I gave. The other was wrong, and the way it was wrong is more instructive than the one that worked.</p>

## The setup

Consensus was $31.50. The company had beaten four quarters running, and beaten enormously.

<div class="scroll" markdown="0">
<table>
<thead><tr><th>Quarter</th><th>Estimate</th><th>Actual</th><th>Beat by</th></tr></thead>
<tbody>
<tr><td>Dec 2025</td><td>$3.82</td><td>$4.78</td><td>+25.1%</td></tr>
<tr><td>Mar 2026</td><td>$8.60</td><td>$12.20</td><td class="pass">+41.9%</td></tr>
<tr><td>Jun 2026</td><td>$20.20</td><td>$25.11</td><td>+24.3%</td></tr>
<tr><td><strong>Sep 2026</strong></td><td>$31.50</td><td>$33.42</td><td class="fail">+6.1%</td></tr>
</tbody>
</table>
</div>

The beat shrank by a factor of four. That is the number worth watching, not whether there was a beat.

The March 2026 print is the clearest evidence that the beat itself is not the trade. The company beat by **41.9%** and the stock **fell 3.8%** the following session, then another 4.8% the day after. A beat that large being sold means the beat was already in the price.

## Call one, right: do not trade the print

The weekly at the money straddle priced a **7.4% move** ($39.90 call plus $39.53 put against spot of $1,074.86), at **120% implied volatility**.

<div class="kpi">
  <div><span class="n">&plusmn;7.4%</span><span class="l">Implied move</span></div>
  <div><span class="n">+3.0%</span><span class="l">Realised, close to close</span></div>
  <div><span class="n">120%</span><span class="l">Implied volatility pre print</span></div>
</div>

The stock closed the next session at $1,097.39 against a prior close of $1,065.11, a move of **+3.03%**. Well inside the implied move, which means both sides of that straddle lost. Long volatility into a scheduled event is a bet that the event exceeds a number the market has already set generously, and there is no information edge available on a date everyone knows.

This is now gate seven: **never hold an unreleased print**.

## Call two, wrong: the stock would fall

My premarket read was that the shrinking beat plus a 65% increase in planned capital spending would send the stock lower, and I put a target of $1,040 to $1,050 on it. It opened down 0.67% and then **closed up 3.03%**, nowhere near that level.

What I got wrong was the sign on the capital expenditure guidance. The company raised fiscal 2027 capex from roughly $27 billion to **above the mid $40 billions**, and said its high bandwidth memory was sold out beyond 2027 with most of next year's volume already committed at higher prices. I read the capex as a cash outflow, which it is. The market read it as confirmation of demand visibility strong enough to justify committing that much capital, which it also is, and that reading was better than mine.

**The lesson I took:** a capital spending increase is ambiguous on its own. It is bearish for free cash flow and bullish as a demand signal, and which dominates depends on whether the sold out order book is credible. I weighted the cash flow effect without checking the order book claim, and the order book was the stronger fact.

## The part that did work: second order exposure

The capital spending number is unambiguous for the companies **receiving** it. Equipment makers rallied on the same session.

<div class="scroll" markdown="0">
<table>
<thead><tr><th>Name</th><th>1 Oct</th><th>2 Oct</th></tr></thead>
<tbody>
<tr><td>Test equipment</td><td>+3.71%</td><td class="pass">+7.75%</td></tr>
<tr><td>Metrology</td><td>+2.29%</td><td class="pass">+5.47%</td></tr>
<tr><td>Process control</td><td>+2.77%</td><td>+3.72%</td></tr>
<tr><td>Etch and deposition</td><td>+3.53%</td><td>+3.02%</td></tr>
<tr><td>The reporting company</td><td>+3.03%</td><td class="fail">&minus;1.28%</td></tr>
</tbody>
</table>
</div>

On day one everything rose together, so the divergence was not yet visible. It appeared on day two, when a competitor announced a 60 billion yen investment to double hard drive output. Storage names fell between 12% and 13% on supply glut fear while the equipment makers rose again, because doubling capacity is an equipment order.

**Two independent events in three days pointed the same way:** announced capacity is revenue for whoever builds the capacity. That is a more durable read than guessing a reporting company's one day reaction.

## And a correction to my own reading

Going into that week, one of the two storage names was trading below its 50 day moving average and the other was comfortably above it. I said at the time that the weaker one was therefore the one that would break.

That was not borne out. **Both fell, and the one that had been in an uptrend fell slightly harder**, 12.68% against 12.15%. A moving average describes where a stock sits relative to its own recent history. It does not forecast which name a piece of industry news will hit hardest, and I overstated what the signal could do.

What the trend filter is actually for is the direction of a position, not the magnitude of a reaction to news that has not happened yet. That is how it is used in the [methodology]({{ '/methodology' | relative_url }}) and the overstatement has been removed.

## Volatility contagion, the practical cost

One more thing this episode showed. The print inflated implied volatility across the entire supply chain, including names with no earnings date.

<div class="scroll" markdown="0">
<table>
<thead><tr><th>Vehicle</th><th>Implied volatility</th><th>Spread</th><th>Verdict</th></tr></thead>
<tbody>
<tr><td>Etch and deposition call</td><td class="fail">61%</td><td class="fail">9.7%</td><td>Rejected</td></tr>
<tr><td>Process equipment call</td><td class="fail">60%</td><td class="fail">11.9%</td><td>Rejected</td></tr>
<tr><td>Semiconductor ETF call</td><td>34%</td><td>5.4%</td><td>Borderline</td></tr>
<tr><td>Large cap chip call</td><td class="pass">30%</td><td class="pass">1.9%</td><td class="pass">Cleared</td></tr>
</tbody>
</table>
</div>

The names that looked like the purest expression of the thesis were the most expensive way to own it, because everyone else had the same idea and bid their volatility up. The liquid large cap in the same sector carried half the volatility and one fifth the spread for substantially the same exposure.

**When an event inflates a sector's implied volatility, the cheapest expression is usually the most liquid name in that sector, not the most thematically precise one.**
