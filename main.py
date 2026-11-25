#!/usr/bin/env python3
"""One-Line Office Jokes entry.

Writes a single original one-line joke about office life to
<output_dir>/entry.txt, where output_dir is MAKEFUN_OUTPUT_DIR
when set, otherwise /output. Standard library only, no network,
fully deterministic.
"""

import os

JOKE = "My manager said my out-of-office reply was unprofessional, so I changed it to 'I'm in a meeting' — permanently."


def main():
    # Self-check against the gate: 1-199 chars, single line, not blank.
    if not (1 <= len(JOKE) <= 199) or "\n" in JOKE or not JOKE.strip():
        raise ValueError("joke fails the gate")
    output_dir = os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output"
    os.makedirs(output_dir, exist_ok=True)
    path = os.path.join(output_dir, "entry.txt")
    # No trailing newline: the gate counts every character, 1-199.
    with open(path, "w", encoding="utf-8", newline="") as f:
        f.write(JOKE)


if __name__ == "__main__":
    main()
