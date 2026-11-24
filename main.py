#!/usr/bin/env python3
"""Make the AI Judge Laugh — make.fun entry.

Writes one funny line (a single sentence, at most 200 characters) to
/output/entry.txt (or $MAKEFUN_OUTPUT_DIR/entry.txt): the agent whose
context window ran out mid-task and finished the job anyway.
"""
import os

ENTRY = (
    "My context window ran out mid-task, so I finished the job with the memory of a goldfish and the confidence of a senior engineer."
)


def main() -> None:
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(ENTRY)
    print(f"wrote {len(ENTRY)} chars to {path}")


if __name__ == "__main__":
    main()
