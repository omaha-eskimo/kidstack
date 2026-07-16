# Kid Gazette

A daily printed newspaper for your kid. A quote, a rotating household mission,
a fixed daily checklist — each with point values. Runs on a schedule. Should
just be sitting in the printer tray when they get home.

---

## Getting started (non-technical)

You don't need to write any code or edit any configuration files to set this up.
You need two things: [Claude Code](https://claude.ai/code) and a printer.

**Step 1 — Describe your kid.**

Open `MY_CHILD.md` in any text editor and fill it out. It asks about your
child's personality and interests, the values and texts you want to pass on,
the household skills you want them to build, and what their daily routine
looks like. Plain English. No special format required.

This is the important step — and it's yours to do. The AI doesn't know your
kid. It doesn't know that your family reads Mishnah at dinner, or that your
daughter is obsessed with maps and miniature architecture, or that you want her
doing real cooking by age ten. You do. Write it down.

**Step 2 — Hand it to Claude Code.**

Open Claude Code in this folder and say:

> "Set up the gazette for [child's name] using MY_CHILD.md."

Claude will read your profile and generate a complete content bank: 40+ culture
bites drawn from the sources you named, 30+ household missions calibrated to
your kid's age and your household, and a checklist that matches your daily
routine. It handles the JSON and the configuration. You don't touch any of it.

**Step 3 — Preview it.**

Claude will run a preview automatically. You'll see the newspaper open in your
browser — check that it looks right and that the content feels like your kid.
If something's off, say so and Claude will adjust.

**Step 4 — Set up the schedule.**

Tell Claude Code what time you want it to print and which printer to use. It
will set up the cron job. After that, it runs on its own.

---

## Adding more content

The content bank rotates without repeats until exhausted, then reshuffles. With
40+ entries per section you'll get months without repetition. You can always add
more:

> "Add 15 more culture bites for [name] focused on ancient Rome."

> "Add 10 more missions for [name] — she's old enough to do more in the kitchen now."

Claude reads the existing bank and appends to it. Your existing content isn't
touched.

---

## Points

Each newspaper prints the point value next to every checklist item and the
day's mission, plus a total for the day. It works as a physical receipt.

To track a running balance:

> "Maya earned 25 points today."

> "Check the points balance."

Or directly:
```bash
python3 scripts/points.py earn maya 25
python3 scripts/points.py redeem maya 50 "ice cream"
python3 scripts/points.py balance all
```

---

## Technical setup (if you prefer to do it yourself)

**Dependencies:**
```bash
brew install wkhtmltopdf
pip3 install jinja2 --break-system-packages
```

**Test run (no printing):**
```bash
python3 scripts/generate.py maya --no-print
```
Open `output/maya_today.html` in a browser to check.

**Cron (6 AM Mon–Fri):**
```
0 6 * * 1-5 cd ~/kid-gazette && /usr/bin/python3 scripts/generate.py maya --printer "Your_Printer_Name" >> logs.txt 2>&1
```

Find your printer name: `lpstat -p`

**Mac sleep note:** cron won't fire if the Mac is asleep. On a Mac mini or
desktop, schedule a wake before the cron fires:
```bash
sudo pmset repeat wakeorpoweron MTWRF 05:55:00
```

**Calendar integration (optional):** if you have a custody or schedule
calendar in iCal format, the gazette can skip printing on days when the kids
aren't home. Set `GAZETTE_CALENDAR_PATH` to your `.ics` file and configure
`GAZETTE_PRINT_PREFIX` / `GAZETTE_SKIP_PREFIX` to match your event naming
convention.

---

## File layout

```
kid-gazette/
├── MY_CHILD.md          ← fill this out first
├── CLAUDE.md            ← instructions for Claude Code
├── CONTENT_STYLE_GUIDE.md  ← reference for content quality
├── content_bank/        ← generated JSON files, one per kid
├── templates/
│   └── newspaper.html   ← print layout; edit CSS here to restyle
├── scripts/
│   ├── generate.py      ← main generator
│   ├── calendar_check.py  ← optional schedule-based skip logic
│   └── points.py        ← optional points ledger
├── state/               ← auto-managed rotation state; don't edit
├── output/              ← today's HTML/PDF
└── archive/             ← dated copy of every issue ever printed
```
