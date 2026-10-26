#!/bin/bash
# Rebuild and publish the Week Ahead page from data/week.json.
# Usage: publish_week.sh
set -euo pipefail
cd "$(dirname "$0")"
python3 build_week.py data/week.json week-ahead.html
if grep -qIE '487766214|434964649|607733078|bot[0-9]{8,}|TELEGRAM_[A-Z_]*=|AAE[A-Za-z0-9_-]{30,}' data/week.json week-ahead.html; then
  echo "REFUSED: account number or credential found. Nothing published." >&2; exit 2
fi
git add week-ahead.html assets/week.css data/week.json build_week.py publish_week.sh _layouts/default.html _config.yml index.md publish.sh
if git diff --cached --quiet; then echo "no changes"; exit 0; fi
git -c user.email=carolinehutchins05@gmail.com -c user.name="Caroline Hutchins" \
  commit -q -m "Week Ahead, $(date +%Y-%m-%d)

Co-Authored-By: Claude Sonnet 5.5 <noreply@anthropic.com>"
git push -q origin main
echo "published: https://carolinehutchins05-prog.github.io/options-desk/week-ahead/"
