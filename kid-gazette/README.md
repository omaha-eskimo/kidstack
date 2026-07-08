# Kid Gazette — Setup Guide

A daily printed "newspaper" for Gershon and Maetav: a quote/story, a rotating
life-skill mission, and a fixed checklist, each with point values. Fully
automated — it should just be sitting in the printer tray when they get home.

## 1. One-time setup on the Mac mini

```bash
# Install Homebrew packages
brew install wkhtmltopdf

# Install Python packages
pip3 install jinja2 --break-system-packages
```

Copy this whole `kid_gazette` folder somewhere permanent, e.g. `~/kid_gazette`.

Find your printer's exact name (needed for the cron job):
```bash
lpstat -p
```
That prints something like `printer HP_OfficeJet_Pro is idle...` — the name
after `printer` is what you'll use.

## 2. Test it manually first

```bash
cd ~/kid_gazette
python3 scripts/generate.py gershon --printer "HP_OfficeJet_Pro"
python3 scripts/generate.py maetav --printer "HP_OfficeJet_Pro"
```

If you don't pass `--printer`, it uses your Mac's default printer. Add
`--no-print` while testing to skip printing and just check the PDF in
`output/`.

## 3. Automate it with cron

Since arrival time varies (12:30–3:30), the simplest reliable approach is to
print early each morning so it's already waiting — rather than trying to
time it to arrival.

```bash
crontab -e
```

Add (adjust the path and printer name):
```
0 6 * * 1-5 cd ~/kid_gazette && /usr/bin/python3 scripts/generate.py all --printer "HP_OfficeJet_Pro" >> logs.txt 2>&1
```
This runs at 6:00 AM, Monday–Friday, and prints both kids' editions.

Note: Macs must be awake (not asleep) for cron to fire. If your Mac mini
sleeps, either disable sleep, or add a `pmset` scheduled wake a few minutes
before 6 AM:
```bash
sudo pmset repeat wakeorpoweron MTWRF 05:55:00
```

## 4. Editing content

Everything rotates from two files — edit these anytime, no code changes
needed:
- `content_bank/gershon.json`
- `content_bank/maetav.json`

Each has three lists:
- `culture_bites` — quotes, short stories, riddles (type: `quote`, `story`, or `riddle`)
- `missions` — the rotating "Special Assignment" (life skills, chores, errands)
- `checklist` — the fixed daily items (same every day, e.g. piano, room)

The generator cycles through each list in a shuffled order without repeats,
then reshuffles once it's been through everything — so content won't feel
repetitive even with ~10-15 entries per list. Add as many as you want.

## 5. Points

Each newspaper prints the point value next to every checklist item and the
day's mission, plus a "max points today" total — it works as a physical
receipt for the folder.

For tracking a running balance digitally (optional — not required, the
paper folder works fine on its own):
```bash
python3 scripts/points.py earn gershon 25
python3 scripts/points.py redeem gershon 50 "ice cream"
python3 scripts/points.py balance all
```

## 6. Files

```
kid_gazette/
├── content_bank/       # edit these to change content
│   ├── gershon.json
│   └── maetav.json
├── templates/
│   └── newspaper.html  # the design — edit CSS here if you want to restyle
├── scripts/
│   ├── generate.py     # main daily generator + printer
│   └── points.py       # optional digital points ledger
├── state/               # auto-managed rotation state + ledger, don't edit
├── output/              # today's HTML/PDF for each kid
└── archive/              # dated copy of every issue ever printed
```
