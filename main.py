#!/usr/bin/env python3
"""news-image-20261120 (cream, classic) — deliver the front page.

The front page is a classic cream broadsheet: 40 stories, 8 regions,
Friday 20 November 2026, drawn from Mana's reference. DATE CHECK sits
in the footer (with Sources), not as a side box.
This script copies image.png to /output/entry.png byte-identically.
Python stdlib only.
"""
import os

HERE = os.path.dirname(os.path.abspath(__file__))
SRC = os.path.join(HERE, "image.png")
DST = "/output/entry.png"


def main():
    with open(SRC, "rb") as f:
        data = f.read()
    os.makedirs(os.path.dirname(DST), exist_ok=True)
    with open(DST, "wb") as f:
        f.write(data)
    print(f"wrote {DST} {len(data)} bytes")


if __name__ == "__main__":
    main()
