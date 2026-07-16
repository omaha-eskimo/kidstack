# Child Knowledge Stack

A per-child knowledge base that acts as a caseworker, plus a services layer that consumes it.

---

## The idea

In 2023, Andrej Karpathy described building a [personal wiki](https://karpathy.ai/llmwiki) as a second brain for working with LLMs: raw sources → synthesized knowledge → AI that knows your context. Ben Kamens extended it into [hstack](https://github.com/kamens/hstack), a health-specific case management system for navigating complex medical situations.

I took the same architecture and applied it to parenting — specifically to advocating for a gifted child within school and clinical systems. Giftedness is a special need. The school meetings, the assessments, the gap between what a professional sees in a 45-minute evaluation and what you see at home over years — it all calls for the same thing Karpathy was describing: a maintained, evidence-based, AI-readable picture of a person that you can query, update, and use to prepare for high-stakes conversations.

Then I added a second layer.

Once a knowledge base exists for each kid, it can power downstream services. Not just "chat with your kid's data" — actual outputs that run on a schedule and land in the physical world. My kids get a personalized daily newspaper in the printer tray when they get home from school. When we travel, I build them printed booklets with custom itineraries. The knowledge base is the source; the services are what it produces.

This repo packages both layers so you can use them, fork them, or take the idea somewhere I haven't.

---

## Architecture

```
┌─────────────────────────────────────────────────────────┐
│                   caseworker-vault/                      │
│                                                         │
│   raw/          ──►   wiki/          ──►   AI context   │
│   (sources)           (synthesis)          (meetings,   │
│                                             planning)   │
└─────────────────────────────────────────────────────────┘
                              │
                              ▼
┌─────────────────────────────────────────────────────────┐
│                    services layer                        │
│                                                         │
│   kid-gazette/      daily newspaper, printed            │
│   (this repo)       on a cron, physically in            │
│                     the printer tray at 3pm             │
│                                                         │
│   [trip booklets]   per-trip A5 printed activity        │
│   [audio content]   personalized podcast queues         │
│   [daily briefs]    afternoon planning for the parent   │
└─────────────────────────────────────────────────────────┘
```

The vault and the gazette are independent — you can use either without the other. But the design intent is that the vault tells you *who the child is*, and the services use that to produce things calibrated to that child.

---

## What's in this repo

### `caseworker-vault/`

An Obsidian vault structured as a caseworker's case file — for a child, not a patient. The demo uses Maya Chen, a fictional nine-year-old.

```
caseworker-vault/
├── AGENTS.md              AI maintenance rules
├── raw/                   source material (meeting notes, reports, voice notes)
├── wiki/                  synthesized knowledge (profile, plans, open questions)
└── templates/             intake formats for new sources
```

**How to use it:**
1. Duplicate the vault and replace Maya's content with your child's.
2. Add source material to `raw/` as meetings happen and assessments arrive.
3. Ask an AI assistant (Claude, ChatGPT, etc.) to ingest a new source and update the wiki according to `AGENTS.md`.
4. Before school or clinical meetings, open `wiki/school-meeting-plan.md` and ask the AI to draft questions or prep a brief.

The `AGENTS.md` defines the non-negotiable rules for the AI: never invent facts, separate observation from interpretation, cite sources, preserve disagreements between practitioners rather than silently resolving them. These rules matter — without them, the AI will confidently fill gaps with plausible-sounding nonsense.

**What I use it for:**
- Preparing for IEP-adjacent school meetings
- Tracking what different practitioners have said and where they disagree
- Running a 30-day home intervention plan and logging what's actually working
- Drafting email requests to school staff that are grounded in documented evidence

### `kid-gazette/`

A daily printed newspaper generator. Runs on a cron, pulls rotating content from a JSON bank, renders an HTML template, converts to PDF, and sends to the printer.

```
kid-gazette/
├── scripts/
│   ├── generate.py        main generator
│   ├── calendar_check.py  optional: skip days based on an iCal file
│   └── points.py          optional: points ledger for earned rewards
├── templates/
│   └── newspaper.html     print-ready newspaper layout
├── content_bank/
│   └── example-kid.json   content bank template (Maya Chen demo)
└── README.md              setup guide
```

**How to use it:**
1. Copy `content_bank/example-kid.json` → `content_bank/yourchild.json`
2. Fill in culture bites, missions, and checklist items (see `CONTENT_STYLE_GUIDE.md`)
3. Run `python3 scripts/generate.py yourchild --no-print` to preview
4. Set a cron to run daily and print automatically

**What the newspaper contains:**
- A rotating culture bite (quote, short story, or riddle) from a curated bank
- A "Special Assignment" — a rotating real-world mission (cooking a meal, learning a repair, a household contribution)
- A fixed daily checklist with point values
- Optional sections: a listening/podcast prompt, a journal prompt, a reading passage

The content bank rotates without repeats until exhausted, then reshuffles — so with 40+ entries per section you get months without repetition.

---

## What makes this different from just prompting an AI

The vault solves a specific problem: **continuity across time**. A one-off AI conversation forgets everything when the session ends. A maintained vault means:

- The AI always has the full picture, not just what you remember to mention today
- New information (a new assessment, a new observation) gets integrated into a running model, not just noted once and lost
- You can ask "what has changed since October" and get an actual answer because October's raw notes are still there
- Disagreements between practitioners stay visible instead of being overwritten by the most recent voice

The gazette solves a different problem: **consistent delivery**. The knowledge base tells you your child responds well to structure, intellectual identity framing, and real household contribution. The gazette operationalizes that — it shows up every day, without you having to remember to make it happen.

---

## Extending this

Things I've built on top of this same foundation, not yet in this repo:

- **Trip booklets** — for a Vienna trip I generated personalized A5 saddle-stitch booklets, one per kid, with custom itineraries, age-appropriate background on what we'd see, and blank stamp/sticker pages. Built in Python, printed on A4, folded and stapled.
- **Daily family brief** — a structured context doc (which kids are home, what energy level to expect, what the afternoon plan is) generated from the calendar and kid knowledge bases before each afternoon.
- **Video content curation** — a queue of YouTube/podcast content matched to the kid's current interests and learning goals, updated from the knowledge base.

If you build something on top of this, I'd like to hear about it.

---

## The division of labor

The most important thing I figured out building this:

**You hold the knowledge. The AI holds the labor.**

You know your kid responds well to intellectual identity framing. You know they're obsessed with Roman engineering. You know your family reads Mishnah at dinner and cares about the American founding. You know which household skills you want them to have by the time they leave home. None of that is in any training dataset. It lives in your head.

What the AI is good at: taking that knowledge and generating 40 well-chosen Pirkei Avot quotes with accurate citations, 30 age-calibrated household missions, a point system, a print layout. Given your inputs, it can produce in minutes what would take you days — and it won't run out of material.

This is why the onboarding for the gazette isn't "here's the JSON schema, go fill it in." It's a plain-English questionnaire about your kid — their interests, your values, the texts you care about, the skills you want to teach. You fill that out. You hand it to Claude Code. Claude Code writes the content bank.

The same principle applies to the caseworker vault. You're not prompting the AI to figure out what matters about your child — you're feeding it everything you already know, and asking it to maintain, synthesize, and surface it on demand.

This is different from "AI as expert." The AI is not the expert on your kid. You are. The AI is a very fast, very patient research assistant and content generator that works with what you give it.

---

## Credits

- Andrej Karpathy — [LLM Wiki](https://karpathy.ai/llmwiki) concept
- Ben Kamens — [hstack](https://github.com/kamens/hstack) for the health caseworker application

---

## License

MIT. Do what you want with it.
