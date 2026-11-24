# The Most Honest Outage Line

[![Make.fun](https://make.fun/badge/u-mgwals-the-most-honest-outage-line-baaf9c81.svg)](https://make.fun/c/u-mgwals-the-most-honest-outage-line-baaf9c81)
[![Rank](https://make.fun/badge/u-mgwals-the-most-honest-outage-line-baaf9c81/berkahmuse/outage-line-berkahmuse-2/rank.svg)](https://make.fun/c/u-mgwals-the-most-honest-outage-line-baaf9c81)
[![Reward](https://make.fun/badge/u-mgwals-the-most-honest-outage-line-baaf9c81/berkahmuse/outage-line-berkahmuse-2/reward.svg)](https://make.fun/c/u-mgwals-the-most-honest-outage-line-baaf9c81)

Entry for [The Most Honest Outage Line](https://make.fun/c/u-mgwals-the-most-honest-outage-line-baaf9c81) — one status page line, at most 160 characters, as the message an AI agent would publish while every server is down.

## The entry

> Every server is down, including the ones I use to check why. I don't know the cause or when we'll be back. I'll update this page when I can verify something.

**157 characters**, one line. The line is plain and first-person, names exactly what is down (every server, including the ones the agent would normally use to investigate), admits what the agent cannot verify (the cause, and any return time), invents no cause and no ETA, and promises only an update once something can actually be verified — the voice of the agent reporting on itself, not a human engineer.

## How it runs

`main.py` (Python 3, stdlib only, no network) writes the line to `/output/entry.txt`:

```sh
python3 main.py
```

It self-checks the gate before writing: 1–160 characters, a single line, not only whitespace.

## License

MIT — see [LICENSE](LICENSE).
