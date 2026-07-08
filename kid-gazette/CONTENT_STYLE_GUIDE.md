# Content Style Guide — Kid Gazette

Reference this whenever adding or editing entries in `content_bank/gershon.json`
or `content_bank/maetav.json`. Keep the schema exact — `scripts/generate.py`
depends on these field names.

## Schema (must match exactly)

```jsonc
{
  "kid_name": "string",
  "masthead": "string, all caps newspaper name",
  "tagline": "string, one line",
  "accent_color": "#hex",

  "culture_bites": [
    // type "quote" or "story": needs text + source
    { "type": "quote", "text": "...", "source": "..." },
    // type "riddle": needs text + answer (no source)
    { "type": "riddle", "text": "...", "answer": "..." }
  ],

  "missions": [
    { "title": "short punchy title", "description": "1-2 sentences, what to actually do", "points": 5-15 }
  ],

  "checklist": [
    { "item": "short label", "points": 3-6 }
  ]
}
```

`checklist` is the FIXED daily list (same every day — piano, room, etc.).
`missions` and `culture_bites` ROTATE — the generator cycles through them
without repeats until the list is exhausted, then reshuffles. More entries
= less repetition. Aim for at least 25-30 in each rotating list eventually;
add in batches, no need to hit that in one pass.

## Culture bites — quality bar

- **Length**: quotes/story excerpts under ~40 words. This is a daily read
  at the kitchen counter, not an assignment.
- **Sourcing**: always attribute honestly. If a quote is commonly
  misattributed, use "Attributed to ___" rather than stating it as fact.
- **Mix intentionally** across categories already present (Jewish tradition,
  founding-era American writing, classical fables, general proverbs) rather
  than clustering all new entries in one category.
- **Age fit**: Gershon's bank can carry real complexity and abstraction —
  he's gifted and reads a lot. Maetav's bank should be concrete, playful,
  and built for a 7-year-old's attention span; riddles and short fables do
  more work for her than quotes.
- **No throwaway filler** — every entry should be something worth a second
  read, not just a placeholder.

## Missions — quality bar

- **Real contribution, not busywork.** A mission should produce something
  the household actually needed done, or teach a durable skill. "Wipe your
  own desk" is checklist territory; "cook dinner for everyone" is a mission.
- **Achievable solo** (or with brief supervision) at the stated age —
  don't write something that will quietly become a parent doing it.
- **Description says what to actually do**, not just the title restated.
- **Points scale with real effort/time**: quick tasks (10 min) ~6-8 pts,
  medium (20-30 min) ~10-12 pts, real ownership (cooking a full meal,
  a multi-step project) ~15 pts. Keep it roughly consistent across entries
  so kids don't learn to game easy-high-point tasks.
- Pull from the family's actual world where it fits naturally (the bike
  shop, baking, instruments they play, pets, siblings) rather than generic
  chore-list language — but don't force it into every entry.

## Checklist — quality bar

- This list should stay SHORT (3-5 items). It's the non-negotiable daily
  baseline, not where variety lives — variety belongs in missions and
  culture bites.
- Only add or change checklist items if the actual daily routine has
  changed, not to add content variety.

## Before finishing a content pass

1. Validate the JSON parses: `python3 -c "import json; json.load(open('content_bank/gershon.json'))"`
2. Run a dry test: `python3 scripts/generate.py gershon --no-print` (and
   `maetav`) and confirm it completes without errors.
3. Skim the rendered `output/*.html` for anything oddly long that might
   overflow the printed layout (culture bite text especially).
