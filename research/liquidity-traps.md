---
layout: default
title: Three liquidity traps that pass the obvious checks
description: A one lot bid behind the tightest spread on the board, open interest with no volume, and a chain that doubles in a session.
---

<p class="eyebrow">Research &middot; August to October 2026</p>

# Three liquidity traps that pass the obvious checks

<p class="lede">Spread and open interest are the two liquidity numbers everyone looks at. Each of the three traps below clears at least one of them and would have cost real money.</p>

## One: the tightest spread on the board, with a one lot bid

Screening for a same day round trip, one contract had the **narrowest spread on the entire board at 1.6%**, with 1,249 open interest. On spread and open interest it was the best candidate available.

Its `bid_size` was **1**.

A single contract bid means entry fills fine and exit does not. You are long an instrument with no buyer, and the only way out is to walk the price down until someone appears. A second candidate that session showed the same pattern.

**This does not appear in spread and it does not appear in open interest.** A quoted spread is only meaningful at the size behind it, and depth is a separate field that has to be read separately. The gate is now **bid size and ask size of 20 or more, each**.

## Two: open interest without volume

Screening a healthcare sector produced four names that passed every technical filter cleanly. Their option chains were unusable: open interest between 26 and 181, spreads between 12% and 30%, and in one case **total volume of 1 contract** for the day.

The worst example came later, in storage. A near the money monthly call showed:

<div class="scroll" markdown="0">
<table>
<thead><tr><th>Field</th><th>Value</th></tr></thead>
<tbody>
<tr><td>Open interest</td><td class="fail">108</td></tr>
<tr><td>Volume today</td><td class="fail">9</td></tr>
<tr><td>Spread</td><td class="fail">14.5% of mark</td></tr>
</tbody>
</table>
</div>

A 14.5% spread paid twice is a 29% hole before direction contributes anything.

**Open interest is cumulative and can be stale.** It records positions opened at some point in the past, including in a strike that has since gone quiet. Today's volume is what tells you whether anyone is trading it now. Both gates are required: **open interest 1,000 or more and volume 500 or more**.

A useful consequence: when the technical signal is good and the chain is dead, the correct expression is the **underlying shares**. No volatility premium, no decay, no spread to cross twice. Reaching for a bad contract because the stock looks right is how a good idea becomes a losing trade.

## Three: a chain that reprices before you get there

On 2 October 2026 two storage names fell roughly 12% on a competitor capacity announcement. Both had just broken below their trend, so the direction finally qualified for a put, and the thesis was sound.

The chains had already moved.

<div class="scroll" markdown="0">
<table>
<thead><tr><th></th><th>Put A</th><th>Put B</th></tr></thead>
<tbody>
<tr><td>Prior close</td><td>$40.70</td><td>$19.03</td></tr>
<tr><td>Midday</td><td class="fail">$80.85</td><td class="fail">$37.93</td></tr>
<tr><td>Implied volatility</td><td class="fail">71.3%</td><td class="fail">70.5%</td></tr>
<tr><td>Open interest</td><td class="fail">353</td><td>924</td></tr>
<tr><td>Further move needed to break even</td><td class="fail">&minus;10.5%</td><td class="fail">&minus;10.9%</td></tr>
</tbody>
</table>
</div>

Both puts **doubled in a session**. Buying either one required a further 10% collapse on top of a 12% one just to return the premium, at implied volatility above the 70% hard reject.

**The thesis was right and unprofitable**, because being right about a direction after the market has repriced it is worth nothing. Chasing a put after a 12% gap down is the identical error to chasing a call after a gap up, and the discipline has to be symmetric. Gates five and six exist for the long side; this is the short side version of the same problem.

## What the three have in common

All three are cases where a number that looked like evidence was not. A tight spread with no depth, open interest with no activity, a sound thesis priced in already. Each required reading one additional field that the first one does not imply.

This is why the screen checks thirteen things rather than three, and why every one of them is conjunctive.
