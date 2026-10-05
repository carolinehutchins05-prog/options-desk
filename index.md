---
layout: default
title: Options Desk
description: A systematic daily screen for single leg options, with the research and reasoning behind every gate it enforces.
---

<p class="eyebrow">Systematic options research</p>

# Rules I can defend, applied the same way every day

<p class="lede">An automated screen for single leg calls and puts. It runs twice each weekday and most days it reports nothing. This site publishes the gates it enforces, the measurements behind them, and a dated record of every rule I have changed and why.</p>

The interesting part of a screen is not the list it produces. It is whether each rule in it can be justified from something measured, and whether the author notices when a rule is wrong. That is what the pages below are for.

<div class="cards">
  <a class="card" href="{{ '/methodology' | relative_url }}">
    <span class="tag">Start here</span>
    <h3>Methodology</h3>
    <p>Thirteen gates, each with the reason it exists and what it rejects.</p>
  </a>
  <a class="card" href="{{ '/research/spread-is-the-edge' | relative_url }}">
    <span class="tag">Core finding</span>
    <h3>Leverage is priced. Spread is not.</h3>
    <p>Four calls at the same delta looked wildly different. Adjusted for implied volatility they were identical.</p>
  </a>
  <a class="card" href="{{ '/revisions' | relative_url }}">
    <span class="tag">The honest part</span>
    <h3>Revisions</h3>
    <p>Rules added after losses, a strategy I killed, and a backtest that did not survive forward testing.</p>
  </a>
</div>

## How the two runs work

<div class="scroll" markdown="0">
<table>
<thead><tr><th>Run</th><th>Time, ET</th><th>Does</th></tr></thead>
<tbody>
<tr><td><strong>Premarket plan</strong></td><td>8:36</td><td>Reads the morning news digest, sector outlook and momentum screen. Builds candidates with a trend check, a dated catalyst, and a provisional contract priced off the prior close.</td></tr>
<tr><td><strong>Live verdict</strong></td><td>10:11</td><td>Regrades the same candidates on live quotes, thirty minutes after the open. Issues the final list with an entry condition, an invalidation level, and a target.</td></tr>
</tbody>
</table>
</div>

**Thirty minutes is deliberate.** Entering at the opening bell is the error the second run exists to prevent. On 25 June 2026 Micron gapped from a close of $1,048.51 to open at $1,233.00, printed a high of $1,255.00, and closed at $1,213.56. The next session it opened $1,139.08 and closed $1,132.33. The opening print was the best price available all day and buyers at the bell were down 6.7% within 24 hours.

So the second run carries an explicit **gap filter**: if a candidate has moved far enough at the open that its break even is now more than 3% away, it is marked gapped past entry and dropped. It is never chased with a further strike.

## What is not here

No position sizing, account data, or portfolio information, by design. The publishing script strips book level sections mechanically and refuses to push if it finds an account identifier, so a drafting mistake cannot leak one.

No performance claims either, until there are enough closed observations to state honestly, losers included. The daily log began in October 2026. Why I am strict about that is in [Revisions]({{ '/revisions' | relative_url }}).

## Scope

Single leg long calls and puts only. Defined risk, maximum loss is the premium. No spreads, no written options, no zero day expiries, no leveraged products. Typical hold is a few days to about a week, which is what the delta and theta gates are tuned for.
