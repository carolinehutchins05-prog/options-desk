#!/bin/bash
# Publish one run to the public Options Desk site.
# Usage: publish.sh <premarket|verdict> <YYYY-MM-DD> <body-file>
# The body file must ALREADY be redacted: no position counts, no slots line,
# no dollar sizing, no book percentages, no account numbers.
set -euo pipefail
KIND="${1:?premarket or verdict}"
DATE="${2:?YYYY-MM-DD}"
BODY="${3:?path to markdown body}"
cd "$(dirname "$0")"

case "$KIND" in premarket) LABEL="Premarket Plan";; verdict) LABEL="Live Verdict";; *) echo "kind must be premarket or verdict" >&2; exit 1;; esac

# Hard stop if anything secret-shaped slipped into the body.
if grep -qIE '487766214|434964649|607733078|bot[0-9]{8,}|TELEGRAM_[A-Z_]*=|AAE[A-Za-z0-9_-]{30,}' "$BODY"; then
  echo "REFUSED: body contains an account number or credential. Nothing published." >&2
  exit 2
fi

# --- Mechanical redaction. Runs regardless of what the task prompt did. ---
CLEAN=$(mktemp)
# Drop whole sections that are about HER book, not about candidates.
awk '
  /^#{2,3}[[:space:]]*(Slots?|Holdings|Holdings Flow|Earnings Gap Alert|Insider Activity|Congressional|Corporate Insiders|Portfolio|My Positions|Book)([[:space:]]|$)/ { skip=1; next }
  /^#{1,3}[[:space:]]/ { skip=0 }
  skip { next }
  { print }
' "$BODY" \
| grep -vIiE '(open contracts|slots? (available|remaining|used)|new this week|of (my|her) book|% of book|percent of book|already (held|hold)|currently hold|my position|she (holds|owns))' \
| perl -pe 's/==([^=\n]+)==/$1/g' \
| python3 "$(dirname "$0")/clean_for_web.py" \
| python3 "$(dirname "$0")/options_card.py" "$DATE" \
> "$CLEAN"

if ! grep -qIE '[[:alnum:]]' "$CLEAN"; then
  echo "REFUSED: body was empty after redaction. Nothing published." >&2; rm -f "$CLEAN"; exit 3
fi
BODY="$CLEAN"

OUT="archive/${DATE}-${KIND}.md"
{ printf -- '---\nlayout: default\ntitle: "%s, %s"\n---\n\n' "$LABEL" "$DATE"; cat "$BODY"; } > "$OUT"

# index.md: hero, key gates, then the newest run in full.
NEWEST=$(ls -1 archive/*-*.md 2>/dev/null | grep -vE 'archive/index' | sort | tail -1)
nb=$(basename "$NEWEST" .md); nd=${nb%-*}; nk=${nb##*-}
[ "$nk" = premarket ] && nl="Premarket Plan" || nl="Live Verdict"
{ printf -- '---\nlayout: default\ntitle: Options Desk\n---\n\n'
  cat <<'HERO'
<section class="hero">
<p class="eyebrow">Daily research</p>
<h1 class="hero-title">Calls and puts, held to a standard.</h1>
<p class="hero-sub">Each morning the desk screens for liquid, trend aligned single leg contracts, then publishes what passed, what failed, and why. Most days nothing clears, and that is the right answer.</p>
<p class="hero-links"><a href="week-ahead/">Week ahead</a><span>&middot;</span><a href="archive/">The daily log</a><span>&middot;</span><a href="methodology">Methodology</a><span>&middot;</span><a href="research/">Research</a></p>
<p class="rules">Thirteen gates &nbsp;&middot;&nbsp; Delta 0.50 to 0.65 &nbsp;&middot;&nbsp; Spread under 3% &nbsp;&middot;&nbsp; Open interest over 1,000</p>
</section>
HERO
  printf -- '<div class="latest-head"><span class="eyebrow">Latest run</span><span class="meta">%s, %s</span></div>\n\n<div class="report" markdown="1">\n' "$nl" "$nd"
  tail -n +5 "$NEWEST"
  printf -- '\n</div>\n'
} > index.md

# Rebuild the archive list, newest first, one row per day.
{ printf -- '---\nlayout: default\ntitle: Daily log\n---\n\n<p class="eyebrow">Daily log</p>\n\n# Every run, newest first\n\n<div class="runlist">\n'
  ls -1 archive/*-*.md | grep -vE 'archive/index' | sed -E 's#archive/([0-9-]{10})-.*#\1#' | sort -ur | while read -r d; do
    nice=$(date -j -f "%Y-%m-%d" "$d" "+%a, %b %d" 2>/dev/null || echo "$d")
    printf -- '<div class="runrow"><span class="d">%s</span>' "$nice"
    [ -f "archive/${d}-premarket.md" ] && printf -- '<a href="%s-premarket.html">Premarket Plan</a>' "$d"
    [ -f "archive/${d}-verdict.md" ] && printf -- '<a href="%s-verdict.html">Live Verdict</a>' "$d"
    printf -- '</div>\n'
  done
  printf -- '</div>\n'
} > archive/index.md

git add -A
if git diff --cached --quiet; then echo "no changes"; exit 0; fi
git -c user.email=carolinehutchins05@gmail.com -c user.name="Caroline Hutchins" \
  commit -q -m "${LABEL}, ${DATE}

Co-Authored-By: Claude Opus 5 <noreply@anthropic.com>"
git push -q origin main
rm -f "${CLEAN:-}" 2>/dev/null || true
echo "published: https://carolinehutchins05-prog.github.io/options-desk/ (page: archive/${DATE}-${KIND}.html)"
