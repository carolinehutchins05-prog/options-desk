#!/usr/bin/env python3
"""Stdin to stdout. Make a run note render cleanly on the plain-markdown site:
tables become bullets, horizontal rules go, and an empty Today's Trades section is dropped."""
import re, sys

lines = sys.stdin.read().split("\n")
out, i = [], 0

def cells(l):
    return [c.strip() for c in l.strip().strip("|").split("|")]

while i < len(lines):
    l = lines[i]
    if l.lstrip().startswith("|") and i + 1 < len(lines) and re.fullmatch(r"\s*\|[\s:\-|]+\|\s*", lines[i + 1]):
        head = cells(l)
        i += 2
        while i < len(lines) and lines[i].lstrip().startswith("|"):
            row = cells(lines[i])
            rest = [f"{h} {v}" if h else v for h, v in zip(head[1:], row[1:]) if v]
            out.append(f"- {row[0]}" + (": " + ", ".join(rest) if rest else ""))
            i += 1
        out.append("")
        continue
    if re.fullmatch(r"\s*(-{3,}|\*{3,}|_{3,})\s*", l):
        i += 1
        continue
    out.append(l)
    i += 1

text = "\n".join(out)
# Drop a Today's Trades section whose body just says nothing cleared.
text = re.sub(r"^##\s*Today.s Trades[ \t]*\n(?:(?!#).*\n?)*?(?=^#|\Z)",
              lambda m: "" if re.search(r"none|no (trade|candidate)", m.group(0), re.I) else m.group(0),
              text, flags=re.M | re.I)
text = re.sub(r"\n{3,}", "\n\n", text)
sys.stdout.write(text)
