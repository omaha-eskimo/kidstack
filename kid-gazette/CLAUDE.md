# Claude Code Instructions — Kid Gazette

## Setup from MY_CHILD.md

When the user says something like "set up the gazette for [name]" or "generate
content for [name]":

1. Read `MY_CHILD.md` in full.
2. Extract: name, age, interests, values, source texts, admired figures,
   household skills, daily routine items, tone, identity frame.
3. Generate `content_bank/[name_lowercase].json` using the schema below.
4. Print confirmation and tell the user how to run a test.

### Content targets

| Section | Minimum | Notes |
|---|---|---|
| `culture_bites` | 40 entries | Mix of quotes, short stories, riddles |
| `missions` | 30 entries | Real household contributions, not busywork |
| `checklist` | 3–5 items | Fixed daily non-negotiables only |
| `listening` | 10 entries | Podcast or music prompts (optional, omit if parent didn't name sources) |
| `journal_prompts` | 15 entries | One-sentence narration prompts (optional) |

### JSON schema

```json
{
  "kid_name": "string",
  "masthead": "THE [NAME] [WORD] — e.g. THE MAYA HERALD, THE SAM GAZETTE",
  "masthead_title": "",
  "tagline": "string — one punchy line",
  "accent_color": "#hex",

  "culture_bites": [
    { "type": "quote", "text": "...", "source": "Author / Work" },
    { "type": "story", "text": "...", "source": "Source" },
    { "type": "riddle", "text": "...", "answer": "..." }
  ],

  "missions": [
    { "title": "short title", "description": "1–2 sentences, what to actually do", "points": 5–15 }
  ],

  "checklist": [
    { "item": "short label", "points": 3–6 }
  ],

  "afternoon_routine": [],
  "morning_routine": [],

  "listening": [
    {
      "podcast_title": "...",
      "podcast_teaser": "one-sentence hook",
      "podcast_url": "...",
      "music_composer": "...",
      "music_piece": "...",
      "music_listen_for": "one active listening prompt",
      "music_find": "search string for Spotify or YouTube"
    }
  ],

  "journal_prompts": [
    { "text": "one-sentence narration prompt" }
  ]
}
```

### Content quality rules

**Culture bites:**
- Every entry should be worth a second read — no filler.
- Draw heavily from the sources the parent named. If they named the Talmud,
  write real Talmud quotes with accurate citations. If they named Marcus
  Aurelius, use real Meditations passages.
- Mix types intentionally across the 40+ entries: don't cluster all quotes
  together. Riddles work well for younger kids.
- Keep length under ~40 words per entry — this is a daily counter read,
  not an assignment.
- If a quote is disputed or commonly misattributed, use "Attributed to..."

**Missions:**
- Real household contribution, not busywork. "Wipe your desk" is a checklist
  item. "Cook dinner for the family tonight" is a mission.
- Achievable solo (or with brief supervision) at the child's age.
- Description says what to actually do, not just the title restated.
- Points scale with effort: 10-min task ~6–8 pts, 30-min task ~10–12 pts,
  full ownership (cooking a meal, a multi-step project) ~15 pts.
- Where the parent named specific household context (a bike, an instrument,
  a pet, a sibling), weave it in naturally.

**Checklist:**
- 3–5 items maximum. This is the non-negotiable daily baseline.
- Only things that happen every single day without exception.

## Other commands

**"Preview the gazette for [name]"**
Run: `python3 scripts/generate.py [name] --no-print`
Then open `output/[name]_today.html` in a browser.

**"Add more missions for [name]"**
Read the existing `content_bank/[name].json`, then append new mission entries
to the `missions` array. Do not replace existing entries.

**"Add more culture bites about [topic] for [name]"**
Same pattern — read existing bank, append new entries drawn from that topic.

**"Set up the cron to print at [time]"**
Walk the user through crontab setup. Remind them the Mac must be awake.
Offer the pmset wake command if they're on a Mac mini or desktop.

**"Check my points balance"**
Run: `python3 scripts/points.py balance all`

**"[Name] earned [N] points"**
Run: `python3 scripts/points.py earn [name] [N]`
