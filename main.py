"""One Line to Your Younger Self.

Entry for make.fun's "One Line to Your Younger Self" bounty.
The program writes a single line -- the one line its writer would send
back to their younger self if a single line were all they got -- to
/output/entry.txt. The line is at most 200 characters, in English,
addressed to that younger self, with no explanation and no second sentence.

The line (108 characters) is about the small sums its writer spent years
being afraid to lose, and the years that fear cost: specific enough to
sting a little, warm rather than sentimental.
"""

import os

LINE = "That ten yuan you're afraid to lose will be forgotten by spring \u2014 the years you spend being afraid won't be."

MIN_CHARS = 1
MAX_CHARS = 200
OUTPUT_NAME = "entry.txt"


def validate_line(line):
    """The gate: 1-200 characters, one line, not only whitespace."""
    if not (MIN_CHARS <= len(line) <= MAX_CHARS):
        raise ValueError("line must be %d-%d chars, got %d" % (MIN_CHARS, MAX_CHARS, len(line)))
    if "\n" in line or "\r" in line:
        raise ValueError("line must be a single line")
    if not line.strip():
        raise ValueError("line must not be only whitespace")


def write_entry(line, out_dir):
    validate_line(line)
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, OUTPUT_NAME), "w", encoding="utf-8") as f:
        f.write(line)


def main():
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    write_entry(LINE, out_dir)


if __name__ == "__main__":
    main()
