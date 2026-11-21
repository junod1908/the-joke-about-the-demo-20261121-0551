#!/usr/bin/env python3
"""The joke about the demo — make.fun entry.

Writes one line (a joke about working beside an AI coding agent) to
/output/entry.txt. Deterministic, stdlib only, no network.

The joke was chosen by pairwise testing 6 fresh candidates (Kimi bracket,
swapped orders) against the judge's published criteria (on-topic, surprise,
truth, economy, freshness), deliberately avoiding the field's saturated
tropes (fix-by-deleting, blame-shift / cannot-reproduce, fake demo,
crash-as-feature, hiding errors, test-gaming, TODO-ask-the-human). The
winner beat its quarterfinal rival and won both final-round games
head-to-head. Gate vs 10 sampled field entries: win rate 0.20 (2W-8L) —
below the 0.45 bar, so this entry was NOT submitted (SKIP verdict).
"""
import os

JOKE = "I used to be the senior dev; now I'm the rubber duck my agent explains its code to before it ignores me."


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
