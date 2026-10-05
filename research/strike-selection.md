---
layout: default
title: Strike selection dominates thesis
description: A self audit found every open call required a move between 7.6% and 23.8%. A near the money contract on the same theme returned 77% on a 2.6% move.
---

<p class="eyebrow">Research &middot; 2 October 2026</p>

# Strike selection dominates thesis

<p class="lede">I audited my own open option positions against the delta rule I had already written down. Every one violated it, in the same direction, for the same reason. The rule was correct. I was not following it.</p>

## The audit

Five open single leg positions, four of them calls. For each I computed the distance from spot to strike and read the delta off the chain.

<div class="scroll" markdown="0">
<table>
<thead><tr><th>Contract</th><th>Delta</th><th>Move needed to strike</th><th>Chance of profit</th></tr></thead>
<tbody>
<tr><td>Nov 20 call, mega cap retail</td><td class="fail">0.33</td><td>+7.6%</td><td>22%</td></tr>
<tr><td>Nov 20 call, security software</td><td class="fail">0.28</td><td>+15.0%</td><td>18%</td></tr>
<tr><td>Nov 20 call, mega cap hardware</td><td class="fail">0.21</td><td>+8.1%</td><td>16%</td></tr>
<tr><td>Nov 20 call, brokerage</td><td class="fail">0.22</td><td>+23.8%</td><td>14%</td></tr>
</tbody>
</table>
</div>

My own gate for a hold of a few days is **delta 0.50 to 0.65**. Every position sat at 0.21 to 0.33. None of them was a bad idea about the underlying. All four were bad arithmetic.

## The counterexample, the same week

On 30 September, with a semiconductor name at $230.40 against a rising 50 day of $217.40 and RSI 57.7, the near the money contract was the October 16 $230 call at $5.35.

<div class="kpi">
  <div><span class="n">0.478</span><span class="l">Delta at entry</span></div>
  <div><span class="n">2.1%</span><span class="l">Break even distance</span></div>
  <div><span class="n">+2.6%</span><span class="l">Underlying move over two sessions</span></div>
  <div><span class="n">+77%</span><span class="l">Contract, $5.35 to $9.48</span></div>
</div>

The stock did nothing dramatic. It went from $230.40 to $236.48, a move entirely ordinary for the name. The contract nearly doubled because the strike was close enough that an ordinary move mattered.

Meanwhile the far strikes in the table above needed between 7.6% and 23.8%, which for most of those names is a multi month event, not a few day one.

## Why the error is attractive

A cheap contract feels like prudent risk control. Paying $300 instead of $900 looks like risking less. It is not, because the probability of the cheap one expiring worthless is far higher. Spending less per trade while lowering hit rate is not conservatism, it is just a worse bet at a smaller size, and a chance of profit in the teens makes that explicit.

The pull toward it is a budget constraint dressed up as analysis. I caught myself proposing a contract at delta 0.25 with theta at 3.9% of premium per day **because it fit an available dollar amount**, which is not a reason to buy anything.

## The rule, tightened

> Pick the strike nearest the money. If the near the money contract exceeds the position size limit, the answer is **no trade**. It is never a cheaper, further strike.

That last sentence is the whole fix. The failure was not ignorance of the delta band; the band was already written down. The failure was treating a size constraint as permission to relax it. So the automation now states cost as a percentage of capital next to every candidate, and a candidate that only fits by moving the strike out is reported as rejected rather than resized.

## Caveats

This is four positions, which is an anecdote rather than a study. The direction of the effect is not in doubt, since lower delta means lower probability by construction, but the magnitude here is specific to a period when these names were range bound. In a sustained trend the far strikes would have resolved differently. What generalises is the process error, not the numbers.
