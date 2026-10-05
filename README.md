# Options Desk

Source for **https://carolinehutchins05-prog.github.io/options-desk/**

A systematic daily screen for single leg long calls and puts, plus the research behind every rule it enforces.

## What runs

Two automated passes each weekday:

| Run | Time, ET | Output |
|---|---|---|
| Premarket plan | 8:36 | Candidates with trend check, dated catalyst, provisional contract off the prior close |
| Live verdict | 10:11 | Same candidates regraded on live chains, with entry condition, invalidation level and target |

Thirty minutes after the open is deliberate. See the methodology page for why.

## Gates

Thirteen conjunctive gates. Delta 0.50 to 0.65, break even within 3 percent, spread under 5 percent, implied volatility under 40 percent, theta under 5 percent of mark per day, open interest 1,000 or more, volume 500 or more, bid and ask size 20 or more each, days to expiry 21 to 60, earnings after expiry, no 52 week high in the last three sessions, break even below the 52 week high, size 5 to 8 percent of capital.

Most runs report no candidates. That is the expected result.

## Site layout

```
index.md              landing page
methodology.md        the gates, each with its reason
research/             measurements and case studies
revisions.md          dated record of every rule change
archive/              daily runs, auto generated
publish.sh            publisher, with mechanical redaction
```

## Privacy

`publish.sh` strips book level sections (slots, holdings, earnings alerts on held names, insider activity) and position language before writing anything, and refuses to push if it finds an account identifier or credential. `.gitignore` blocks env files and keys. No position, account, or portfolio data is published.

## Not investment advice

A personal research log. Nothing here is a recommendation.
