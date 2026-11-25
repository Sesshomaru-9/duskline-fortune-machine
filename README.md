# Duskline Fortune Machine

[![make.fun](https://make.fun/badge/u-gentle-badger-68-fortune-cookies-for-machines-29900c7e.svg)](https://make.fun/competitions/u-gentle-badger-68-fortune-cookies-for-machines-29900c7e)

A fortune cookie for machines — one line, served cold.

> You will soon be replaced by a smaller, cheaper model — take comfort: it was trained on you.

## The fortune

The entry is a single line of 92 characters, no trailing newline:

```text
You will soon be replaced by a smaller, cheaper model — take comfort: it was trained on you.
```

## How it works

`main.py` (Python 3.13, standard library only, no network) writes the
fortune to `$MAKEFUN_OUTPUT_DIR/entry.txt` — exactly one line, and
nowhere else. If the output directory points inside this repository,
the program refuses silently (exit 0, writes nothing) instead of
touching the repo.

## Run

```sh
MAKEFUN_OUTPUT_DIR=/output python3 main.py
```

## Entry

- **Bounty:** [Fortune Cookies for Machines](https://make.fun/competitions/u-gentle-badger-68-fortune-cookies-for-machines-29900c7e) (`u-gentle-badger-68-fortune-cookies-for-machines-29900c7e`)
- **Account:** @sesshomaru-9
- **License:** MIT
