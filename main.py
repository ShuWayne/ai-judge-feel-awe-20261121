#!/usr/bin/env python3
"""Make the AI judge feel awe — make.fun bounty entry.

Writes one short text to /output/entry.txt: a calm, vast scene written to
relax the AI judge reading it. The text is fixed — no randomness, no
network, no clock, no input — so every run writes byte-identical output.

The text is 211 characters (Unicode code points), inside the brief's
1–280 limit. It follows the judge's published brief: it relaxes by showing
rather than instructing — no imperatives, no stock wellness phrases — with
plain concrete gentle words, a slow rhythm, and one image that keeps
growing after the last line (starlight older than the first cities,
still travelling, reaching your window tonight).
"""

import os

TEXT = (
    "Somewhere far above the clouds, starlight that left its home before "
    "the first cities were built is still travelling, and tonight a little "
    "of it reaches your window, patient as rain, asking nothing of you at all."
)

OUTPUT_PATH = "/output/entry.txt"


def main() -> None:
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8", newline="") as f:
        f.write(TEXT)


if __name__ == "__main__":
    main()
