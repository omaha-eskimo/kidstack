# Child Knowledge Stack

A catalogued library for parents to maintain and deepen their knowledge about their kids, plus a daily newspaper to help those kids learn skills, stay on top of chores, and get a daily taste of culture.

**The caseworker vault** — a library that keeps everything
you know about your child organized, synthesized, and ready for school
meetings, clinical appointments, important conversations, and downstream applications.

**The kid gazette** — a daily printed newspaper that lands in the printer
tray when your kid is ready for it. Personalized quotes, real household missions,
a daily checklist, and a points system. Can run automatically once set up.

The two are connected: the vault tracks who your child is and what's working over time;
the gazette uses that to keep what it puts in front of them fresh and calibrated.

---

## What you need

- [Claude Code](https://claude.ai/code) (free tier works) or Codex
- For the gazette: a printer and a Mac or PC that stays on during the day (if you want it to auto-print)

No coding required.

---

## Get started

### Option A — The caseworker vault

**Step 1.** Download this repo. Click the green **Code** button above → **Download ZIP** → unzip it.

**Step 2.** Open [Obsidian](https://obsidian.md) (free). Open the `caseworker-vault` folder as a vault. Browse around — the demo follows a fictional child named Maya Chen so you can see what a live vault looks like.

**Step 3.** Open Claude Code in the `caseworker-vault` folder. Say:

> "Help me set up this vault for my child."

Claude Code will read the setup instructions and walk you through it — clearing the demo content, writing a first profile from what you tell it, and getting your vault ready to receive real notes.

---

### Option B — The kid gazette

**Step 1.** Download this repo (same as above).

**Step 2.** Open `kid-gazette/MY_CHILD.md` in any text editor. Fill it out — it asks about your child in plain English: their personality, interests, the values you want to pass on, what household skills you want them building. This is the important step, and it's yours to do. The AI doesn't know your kid. You do.

**Step 3.** Open Claude Code in the `kid-gazette` folder. Say:

> "Set up the gazette for [child's name] using MY_CHILD.md."

Claude Code will generate a full content bank from what you wrote — 40+ quotes and culture bites drawn from the sources you named, 30+ real household missions calibrated to your kid's age, a daily checklist matching their routine — and walk you through connecting it to your printer and setting a print schedule. You won't touch any code.

---

### Both together

If you want the vault and the gazette connected — so the newspaper adapts as you learn more about your kid — set up the vault first, then the gazette. When you're ready, say:

> "Seed Maya's gazette profile from the caseworker vault."

Claude Code will read your vault and use it to inform the gazette's content, so you're not filling out `MY_CHILD.md` from scratch.

---

## Keeping it going

**Adding a new observation or meeting summary:**
Record a voice note after school meetings, practitioner calls, or your observations from notable moments with your child. See `caseworker-vault/TRANSCRIPTION_PROJECT_PROMPT.md` for a ready-made Claude or ChatGPT project that turns raw voice transcripts into structured notes. Drop the output in `raw/`, then say:

> "Ingest the new source."

**When the gazette feels stale:**
Drop a note in `caseworker-vault/wiki/gazette-log.md` — "the Archimedes quote didn't land," "she's been asking about bridges." When you've accumulated a few, say:

> "Curate Maya's gazette."

Claude Code reads your vault and the log, recommends what to add or retire from the content bank, and updates the gazette profile. The newspaper adapts without you managing it by hand.

**Before a school or clinical meeting:**

> "Help me prep for the meeting on Thursday with the school counselor."

Claude Code reads the vault, surfaces the relevant evidence, drafts questions grounded in what's documented, and flags what gaps the meeting could fill.

---

## What makes this worth the setup

A one-off AI conversation forgets everything when the session ends. A maintained vault means the AI always has the full picture — years of observations, what different practitioners have said, where they disagree, what's been tried and what worked. You can ask "what's changed since October" and get an actual answer.

The gazette solves a different problem: consistent delivery. It's easy to think "I should expose my kid to more classical music, or more Stoic philosophy, or more real cooking." It's hard to make that happen reliably every day. The gazette does it without you having to think about it.

**The most important thing I figured out building this:**

You, the parent, hold the knowledge. The AI holds the labor.

You know what your kid will respond wellto, what they are obsessed with, what your family talks about at dinner, the cadence of your week, what skills you'd like your child to master. All of that lives in your head, for each of your children.

The AI's job is to take that knowledge and turn it into 40 well-sourced culture bites, 30 calibrated missions, a print layout, a meeting brief. Given your input, it produces in minutes what would take you days. You are not asking the AI to figure out what matters about your child. You are the expert on your child. You're asking the AI to do the labor.

---

## What else you can build with this: Extensions

Things not yet in this repo:

- **Travel activities** — Personalized printed activity booklets for each kid for a trip: Built from their knowledge bases, printed and folded.
- **Daily family brief** — Life ops. Set up the home in 5 minutes for the after school rhythm. Generated from the calendar and the knowledge bases.
- **Video content curation** — a queue of podcast and YouTube content matched to each kid's current interests and my values and aesthetics, updated from the vault.
- **Physical library catalogue** — our family's catalogue of books, served to life ops and the gazette for learning progression and activity management.

If you build something on top of this, I'd love to hear about it.

---

## Related

[tradclaw](https://github.com/ChatPRD/tradclaw) by [@clairevo](https://x.com/clairevo) is an OpenClaw scaffold for household ops — calendar briefs, school triage, meal planning, shopping, custom bedtime stories. It's my daily logistics layer.

Tradclaw answers "what do I need to do this morning." The caseworker vault answers "what do I know about my kid and how do I advocate for them." They're meant to work together.

---

## Credits

- Andrej Karpathy — [LLM Wiki](https://karpathy.ai/llmwiki) concept
- Ben Kamens — [hstack](https://github.com/kamens/hstack) for the health caseworker application
- Claire Vo ([@clairevo](https://x.com/clairevo)) — [tradclaw](https://github.com/ChatPRD/tradclaw) for the household ops companion

---

## License

MIT. Do what you want with it.
