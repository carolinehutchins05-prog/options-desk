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
> "$CLEAN"

if ! grep -qIE '[[:alnum:]]' "$CLEAN"; then
  echo "REFUSED: body was empty after redaction. Nothing published." >&2; rm -f "$CLEAN"; exit 3
fi
BODY="$CLEAN"

OUT="archive/${DATE}-${KIND}.md"
{ printf -- '---\nlayout: default\ntitle: "%s, %s"\n---\n\n' "$LABEL" "$DATE"; cat "$BODY"; } > "$OUT"

# index.md shows the newest file in full.
NEWEST=$(ls -1 archive/*-*.md 2>/dev/null | grep -vE 'archive/index' | sort | tail -1)
{ printf -- '---\nlayout: default\ntitle: Options Desk\n---\n\n[Archive](archive/) · [How this works](https://github.com/carolinehutchins05-prog/options-desk#readme)\n\n'
  tail -n +5 "$NEWEST"
  printf -- '\n---\n*Not investment advice. A personal research log. No position or account data is published here.*\n'
} > index.md

# Rebuild the archive list, newest first.
{ printf -- '---\nlayout: default\ntitle: Archive\n---\n\n# Archive\n\n'
  ls -1 archive/*-*.md | grep -vE 'archive/index' | sort -r | while read -r f; do
    b=$(basename "$f" .md); d=${b%-*}; k=${b##*-}
    [ "$k" = premarket ] && n="Premarket Plan" || n="Live Verdict"
    printf -- '- [%s, %s](%s.html)\n' "$n" "$d" "$b"
  done
} > archive/index.md

git add -A
if git diff --cached --quiet; then echo "no changes"; exit 0; fi
git -c user.email=carolinehutchins05@gmail.com -c user.name="Caroline Hutchins" \
  commit -q -m "${LABEL}, ${DATE}

Co-Authored-By: Claude Opus 5 <noreply@anthropic.com>"
git push -q origin main
rm -f "${CLEAN:-}" 2>/dev/null || true
echo "published: https://carolinehutchins05-prog.github.io/options-desk/ (page: archive/${DATE}-${KIND}.html)"
