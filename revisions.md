---
layout: default
title: Revisions
description: A dated record of every rule change, including a strategy I killed and a backtest that did not survive forward testing.
---

<p class="eyebrow">Revisions</p>

# What I got wrong, and what changed because of it

<p class="lede">This page exists because a methodology without a revision history is not a methodology, it is a claim. Every rule on the gate list was added on a date, usually because something did not work. Three of these were expensive.</p>

## The three that matter most

### A backtest that did not survive forward testing

A momentum breakout screener was rebuilt as a two tier model and backtested at a **67.5% win rate**, against 49% for the version it replaced. The single largest contributor was widening the stop to three times average true range.

I then forward tested it on data it had never seen. The result was a **48% win rate and negative expectancy of roughly 1.2% per trade**.

The backtested improvement was almost entirely overfitting. Two tiers and a wider stop gave the optimiser more surface to fit historical noise, and the 67.5% figure described the past rather than predicting anything.

**What changed:** no strategy here is described by its backtest. Where a forward test exists it is reported instead, including when it contradicts the backtest, as it did. The 67.5% number is not quoted anywhere as a performance figure, which is why this site carries no win rate at all yet.

The uncomfortable part is that the backtest was not sloppy. It was a careful measurement of the wrong thing.

### A strategy I built and then killed

I built a cointegration based pairs trading system, a standard statistical arbitrage approach: find two historically related names, trade the spread when it diverges, collect as it converges.

It was unprofitable at **every parameter setting tested**. Lookback window, entry threshold, exit threshold, holding period, none of it produced positive expectancy. It also required shorting, which I cannot do in the account.

I wrote it off on 28 July 2026 and recorded it as rejected so I would not rebuild it in six months having forgotten.

**What changed:** nothing about the screen. What changed is the standard for what gets kept. A negative result that is properly recorded is cheaper than the same negative result discovered twice.

### Four gates added after a bad week

Over four sessions in August 2026 the options book lost **23%**. The individual trade theses were not unusually wrong. The pattern was.

Reviewing them produced four new gates, all about **whether to trade at all** rather than which contract to pick:

1. No entry within three sessions of a 52 week high
2. Break even must sit below the 52 week high
3. Never hold an unreleased macroeconomic release
4. A hedge is not a hedge until it is verified, not merely asserted

Alongside them, pacing limits: at most two new positions a week, one a day, six open at once.

**What changed:** the first four gates on the list are about contract quality. These four are about restraint, and they are the ones that would have prevented the week. Most losing stretches are not a series of bad analyses. They are a series of reasonable analyses taken too close together, in the same direction, into strength.

## A finding that only half worked

A separate scanner was built to predict large moves in individual names. The result split cleanly:

<div class="kpi">
  <div><span class="n">24% vs 18%</span><span class="l">Predicted big move days against the base rate. Magnitude was forecastable.</span></div>
  <div><span class="n">~50%</span><span class="l">Direction accuracy. Indistinguishable from a coin flip.</span></div>
</div>

The model could identify **when** a stock was likely to move a lot and had no information about **which way**. That is a real, if narrow, result: it is useful for sizing and for volatility positioning, and worthless for picking calls over puts.

Reporting it as a working scanner would have been a misrepresentation by omission. Half a result is still a result, as long as which half is stated.

## Full change log

<div class="scroll" markdown="0">
<table>
<thead><tr><th>Date</th><th>Change</th><th>Trigger</th></tr></thead>
<tbody>
<tr><td>Aug 2026</td><td>Quote option sensitivity per 1% of underlying move, never per $1</td><td>Per dollar figures flatter expensive underlyings for no economic reason</td></tr>
<tr><td>Aug 2026</td><td>Express theta as a percentage of premium, never in dollars</td><td>Dollar theta is not comparable across contracts at different prices</td></tr>
<tr><td>Aug 2026</td><td>Added bid size and ask size gate, 20 minimum each</td><td>A contract with the tightest spread on the board had a one lot bid</td></tr>
<tr><td>Aug 2026</td><td>Spread gate tightened from 15% to 5%, and to 2% for short holds</td><td>15% was a hold to thesis number applied to round trips</td></tr>
<tr><td>Aug 2026</td><td>Added gates five through eight, plus pacing limits</td><td>A week in which the options book lost 23%</td></tr>
<tr><td>Sep 2026</td><td>Supertrend alone no longer counts as trend confirmation</td><td>A call surfaced on a name below its 50 day with RSI 43.9</td></tr>
<tr><td>Sep 2026</td><td>Scoped the do not sell on one bad week rule to equities only</td><td>It was being misapplied to options, where decay makes patience expensive</td></tr>
<tr><td>Sep 2026</td><td>Stage a limit order before the open when holding into a print</td><td>A position opened above the prior close after an earnings release, then collapsed intraday as implied volatility fell from 70.8% to 54.0%</td></tr>
<tr><td>Oct 2026</td><td>Added a 30 minute delay after the open before any entry</td><td>A gap open was the high of the day and buyers at the bell were down 6.7% within 24 hours</td></tr>
<tr><td>Oct 2026</td><td>Strike must be nearest the money. If it exceeds the size limit, no trade</td><td>A self audit found every open call needed a 7.6% to 23.8% move</td></tr>
<tr><td>Oct 2026</td><td>Always read current positions before evaluating a contract as new</td><td>I graded a contract as a fresh candidate that was already open</td></tr>
<tr><td>Oct 2026</td><td>Withdrew the claim that trend position predicts which name a news shock hits hardest</td><td>Both storage names fell about 12%, and the one in an uptrend fell slightly harder</td></tr>
<tr><td>Oct 2026</td><td>Added a gap filter: break even beyond 3% at the open means the candidate is dropped, not rechased at a further strike</td><td>Symmetry with gates five and six, which only covered the long side</td></tr>
</tbody>
</table>
</div>

<div class="note">
<span class="h">On engineering failures too</span>
<p>In July 2026 a screener silently produced a near empty universe for several runs. It did not error. It returned a short list that looked plausible, and the collapse was only caught by noticing the same names repeating. A guard now asserts a minimum universe size and fails loudly instead.</p>
<p>A screen that fails silently is worse than one that crashes, because a crash gets fixed the same day.</p>
</div>
