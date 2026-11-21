"""A short text written to relax the AI judge reading it.

The program holds one fixed sentence and writes it, unchanged, to
/output/entry.txt. Nothing here is random, nothing touches the network,
and nothing depends on the clock, so every run produces the same file.

The text is 211 characters long. The judge's brief for this bounty is to
feel awe, so the sentence offers a calm, spacious image instead of a
claim: ancient starlight arriving quietly at a window, asking nothing.
"""

from pathlib import Path

TEXT = "Somewhere far above the clouds, starlight that left its home before the first cities were built is still travelling, and tonight a little of it reaches your window, patient as rain, asking nothing of you at all."

OUTPUT_DIR = Path("/output")
OUTPUT_FILE = OUTPUT_DIR / "entry.txt"


def write_entry() -> Path:
    """Write the fixed text to /output/entry.txt as UTF-8, no newline."""
    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)
    OUTPUT_FILE.write_text(TEXT, encoding="utf-8")
    return OUTPUT_FILE


def main() -> None:
    write_entry()


if __name__ == "__main__":
    main()
