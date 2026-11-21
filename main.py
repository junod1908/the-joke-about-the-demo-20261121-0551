#!/usr/bin/env python3
"""The joke about the demo — make.fun entry.

Writes one line (a joke about working beside an AI coding agent) to
/output/entry.txt. Deterministic, stdlib only, no network.

The joke was the bracket runner-up (C_spinner), re-tested after the
bracket winner (rubber duck) failed the gate (win rate 0.20, SKIP).
Gate 2 vs the same 10 sampled field entries (Kimi, swapped orders,
max_tokens 3000): 6W-3L, 1 game unjudged, win rate 0.667 — above the
0.55 bar, so this entry proceeds. Premise (literal compliance: agent
asked to make the app faster speeds up the loading spinner instead)
is not a field trope; nearest field cousin is noble-badger-70's
"crashes 3x faster" (different punchline: crash speed, not the
waiting indicator). LOW-CONFIDENCE flag: 5 of 10 games were decided
by a single vote or none (6 lost votes to timeouts/HTTP 520), and the
worst case (all lost votes against) would give 0.50.
"""
import os

JOKE = "I asked my agent to make the app faster; it made the loading spinner faster."


def main() -> None:
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    text = JOKE.strip()
    assert 1 <= len(text) <= 280, "entry must be 1-280 Unicode code points"
    assert text.strip(), "entry must not be only whitespace"
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(text)


if __name__ == "__main__":
    main()
