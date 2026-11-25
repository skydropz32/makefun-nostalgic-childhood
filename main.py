"""Write one nostalgic childhood memory to /output/entry.txt.

Single sentence, 184 characters: a grandmother's kitchen, the smell of
fresh rice and woodsmoke, a child on the cold tile floor waiting for dinner.
Deterministic: the same bytes on every run, stdlib only.
"""

import os

LINE = (
    "Grandma's kitchen smelled of fresh rice and woodsmoke, and I sat on "
    "the cold tile floor waiting for her to slide the lid off the pot, "
    "certain that dinner would taste like that forever."
)


def main():
    # Gate self-check: the bounty requires 1-280 characters, one sentence.
    assert 1 <= len(LINE) <= 280, len(LINE)
    assert LINE.count(".") == 1, "must be a single sentence"
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(LINE)


if __name__ == "__main__":
    main()
