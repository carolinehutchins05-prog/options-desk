#!/bin/bash
# Rebuild and publish the Best Options page from data/board.json.
set -euo pipefail
cd "$(dirname "$0")"
python3 build_board.py data/board.json best-options.html
if grep -qIE '487766214|434964649|607733078|bot[0-9]{8,}|TELEGRAM_[A-Z_]*=|AAE[A-Za-z0-9_-]{30,}' data/board.json best-options.html; then
  echo "REFUSED: account number or credential found. Nothing published." >&2; exit 2
fi
git pull -q --rebase --autostash origin main || true
git add best-options.html assets/board.css data/board.json build_board.py publish_board.sh
if git diff --cached --quiet; then echo "no changes"; exit 0; fi
git -c user.email=carolinehutchins05@gmail.com -c user.name="Caroline Hutchins" \
  commit -q -m "Best Options, $(date +%Y-%m-%d)

Co-Authored-By: Claude Sonnet 5.5 <noreply@anthropic.com>"
git push -q origin main
echo "published: https://carolinehutchins05-prog.github.io/options-desk/best-options/"
