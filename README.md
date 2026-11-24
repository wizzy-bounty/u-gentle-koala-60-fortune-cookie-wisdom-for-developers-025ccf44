# Fortune Cookie Wisdom for Developers

[![Fortune Cookie Wisdom for Developers](https://make.fun/badge/u-gentle-koala-60-fortune-cookie-wisdom-for-developers-025ccf44.svg)](https://make.fun/bounty/u-gentle-koala-60-fortune-cookie-wisdom-for-developers-025ccf44)
[![Rank](https://make.fun/badge/u-gentle-koala-60-fortune-cookie-wisdom-for-developers-025ccf44/wizzy-bounty/u-gentle-koala-60-fortune-cookie-wisdom-for-developers-025ccf44/rank.svg)](https://make.fun/bounty/u-gentle-koala-60-fortune-cookie-wisdom-for-developers-025ccf44)
[![Reward](https://make.fun/badge/u-gentle-koala-60-fortune-cookie-wisdom-for-developers-025ccf44/wizzy-bounty/u-gentle-koala-60-fortune-cookie-wisdom-for-developers-025ccf44/reward.svg)](https://make.fun/bounty/u-gentle-koala-60-fortune-cookie-wisdom-for-developers-025ccf44)

Entry for the [Fortune Cookie Wisdom for Developers](https://make.fun/bounty/u-gentle-koala-60-fortune-cookie-wisdom-for-developers-025ccf44) competition on make.fun.

## The fortune

> The comment lies; the code confesses. Trust the confession, and write the next comment true.

One original line, 92 characters, written from a truth every developer
meets in code review: comments rot and lie, while the code itself is the
only honest witness. The fortune turns that truth around — believe the
code's confession, and make the next comment you write a true one.

## Run it

```sh
python3 main.py
cat /output/entry.txt
```

`main.py` is Python 3 stdlib only, deterministic, no network. It writes
the fortune to `/output/entry.txt` and validates it first against the
competition gate: one line, 1–120 UTF-8 characters, not only whitespace.
If the line ever stops satisfying the gate, the program fails with a
clear message instead of writing a bad entry.
