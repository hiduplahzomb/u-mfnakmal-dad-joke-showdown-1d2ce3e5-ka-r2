"""Dad Joke Showdown entry — one-line dad joke anchored on a concrete number.

The joke is anchored on a specific thermostat setting (68 degrees), with
a concrete setup and a closed punchline built on the double wordplay
"degree-cipline": degrees of temperature and a lack of discipline for
turning the heat up. One line, no trailing question, under the
200-character limit.
"""

import os
import sys

# Gate: one line, <=200 chars, anchored on the concrete number 68,
# closed punchline (no trailing question, no open ending).
# Punchline wordplay: "degree" (temperature unit) inside
# "degree-cipline" (discipline) — the groan is the point.
TEXT = "Dad keeps the thermostat at 68 degrees to save on heat — he says turning it up would show a real lack of degree-cipline."


def main() -> int:
    if not TEXT:
        print("error: TEXT is empty", file=sys.stderr)
        return 1
    if len(TEXT) > 200:
        print(f"error: TEXT is {len(TEXT)} characters, over the 200 limit", file=sys.stderr)
        return 1
    if "\n" in TEXT or "\r" in TEXT:
        print("error: TEXT must be a single line", file=sys.stderr)
        return 1

    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output"
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(TEXT)

    with open(path, "r", encoding="utf-8") as f:
        back = f.read()
    if back != TEXT:
        print("error: entry.txt does not match TEXT byte-for-byte", file=sys.stderr)
        return 1

    lines = back.splitlines()
    if len(lines) != 1:
        print(f"error: entry.txt has {len(lines)} lines, expected 1", file=sys.stderr)
        return 1

    print(f"entry written: {path}")
    print(f"characters: {len(TEXT)}")
    print(f"lines: {len(lines)}")
    print("verified byte-for-byte: OK")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
