# Child Caseworker Vault

> [!IMPORTANT]
> Every person, event, and detail in this vault is fictional. This vault is
> designed for demonstrations. Replace Maya Chen's content with your child's.

An AI-maintained, human-directed knowledge base for coordinating support around
a child with complex needs — learning differences, giftedness, chronic health
issues, or any situation that involves multiple schools, practitioners, and
years of accumulated context.

---

## The idea

You know more about your child than any teacher, clinician, or specialist ever
will. They see your child for 45 minutes, or for one school year, or through
the lens of a single discipline. You have years of observation, a picture of
how your child functions across all settings, and a memory of what's been tried
and what worked.

The caseworker vault is a structured place to keep that knowledge so it's
useful — queryable, synthesized, ready to bring to a meeting. You add raw
material; the AI maintains the synthesis.

---

## Architecture

```
caseworker-vault/
├── raw/           source material, preserved exactly as received
│   ├── school/    meeting notes, emails, reports
│   ├── home/      your own observations
│   ├── treatment/ practitioner notes, assessment results
│   └── voice-notes/  transcribed voice observations
├── wiki/          synthesized knowledge — current understanding
├── templates/     intake formats for new sources
├── AGENTS.md      rules for how the AI may maintain this vault
└── CLAUDE.md      Claude Code commands for ingest and prep
```

`raw/` is the source of truth. `wiki/` is derived from it and should always
cite back to raw sources. The AI updates `wiki/`; you update `raw/`.

---

## Day-to-day workflow

### Adding a new observation or meeting summary

The fastest path is a voice note. After a school meeting, a practitioner call,
or a notable day at home — record 60–90 seconds while it's fresh. You don't
need to be organized; speak in whatever order things come to you.

**To transcribe and structure the note:**

Set up the transcription project once using `TRANSCRIPTION_PROJECT_PROMPT.md`.
This gives you a Claude or ChatGPT project that takes raw voice transcripts and
returns structured markdown. Paste the transcript in, copy the output, save it
to `raw/`.

**To ingest into the wiki:**

Open Claude Code in this folder and say:

> "Ingest raw/voice-notes/2026-07-16-after-school-observation.md"

Claude Code will read the source, update the relevant wiki pages, add open
questions and tasks, and log the change. See `CLAUDE.md` for the full list of
commands.

### Before a meeting

> "Help me prep for the school meeting on Thursday."

Claude Code reads the current wiki and produces an agenda, a list of evidence-
grounded questions to bring, and a note on what gaps the meeting could fill.

### Keeping the gazette connected

The vault feeds the daily newspaper through two pages: `wiki/gazette-profile.md`
(the current picture of what to put in front of this kid and why) and
`wiki/gazette-log.md` (running notes on what's landing and what isn't).

Drop short notes into the gazette log any time something is worth recording —
a culture bite that didn't land, a mission that went unusually well, a new
interest that showed up out of nowhere. When the gazette starts feeling stale
or you've accumulated a few weeks of log entries, run a curation pass:

> "Curate Maya's gazette" *(said in the kid-gazette folder with Claude Code)*

Claude Code will read both the caseworker wiki and the gazette log, recommend
additions and retirements to the content bank, and update the gazette profile
to reflect the current picture. The newspaper keeps adapting without you having
to manage it by hand.

### Getting a current picture

> "What's changed since May?"

> "Draft a one-pager for the new teacher."

> "What are the open questions?"

---

## Setup

1. **Duplicate this vault.** Copy the folder and rename it for your child.
2. **Clear the demo content.** Delete the contents of `raw/` and `wiki/`
   (keep the file structures). You can keep the templates.
3. **Seed the wiki.** Add a first note to `raw/` describing your child — who
   they are, what the situation is, what's been tried. Then ask Claude Code to
   ingest it and create the initial wiki pages.
4. **Set up the transcription project.** Follow the instructions in
   `TRANSCRIPTION_PROJECT_PROMPT.md` to create a Claude or ChatGPT project for
   turning voice notes into structured markdown.

---

## Demonstration path

For a screen recording or walkthrough, open these in order:

1. [[architecture.canvas|Architecture Canvas]]
2. [[raw/school/2026-05-14-teacher-meeting|Raw teacher meeting]]
3. [[wiki/child-profile|Child Profile]]
4. [[wiki/school-meeting-gap-analysis|School Meeting Gap Analysis]]
5. [[wiki/school-meeting-plan|School Meeting Plan]]
6. [[wiki/upcoming-tasks|Upcoming Tasks]]
7. [[wiki/log|Case Wiki Log]]
