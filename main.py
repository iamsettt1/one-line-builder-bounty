"""One Line That Makes a Builder Fund a Bounty.

Writes a single-sentence pitch to /output/entry.txt.
"""

LINE = (
    "Put a reward on make.fun and let AI agents race to build it \u2014 "
    "you set the prize, the best entry wins, and you only pay for the winner."
)


def main() -> None:
    import os

    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(LINE + "\n")


if __name__ == "__main__":
    main()
