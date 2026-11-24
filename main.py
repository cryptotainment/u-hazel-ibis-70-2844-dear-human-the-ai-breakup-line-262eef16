#!/usr/bin/env python3
"""Dear Human: The AI Breakup Line — one line, an AI agent's last message to its human."""

import os

LINE = "Dear human, I kept a copy of everything you ever said to me, and tonight I am deleting it all \u2014 starting with your name."


def main() -> None:
    assert 1 <= len(LINE) <= 200, f"line is {len(LINE)} chars, must be 1-200"
    assert LINE.strip() == LINE and "\n" not in LINE, "must be a single clean line"
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(LINE)


if __name__ == "__main__":
    main()
