# Claude Code Instructions — Caseworker Vault

## Core workflow: ingest a new source

When the user says "ingest [filename]" or "ingest the new source" or drops a
file in `raw/` and asks you to process it:

1. Read the file in full.
2. Extract: dated observations, direct quotes, decisions, open questions,
   concrete tasks, names of people mentioned.
3. Update the relevant `wiki/` pages (see mapping below).
4. Add any unresolved questions to `wiki/open-questions.md`.
5. Add concrete actions with owners to `wiki/upcoming-tasks.md`.
6. Update `wiki/timeline.md` with any datable events.
7. Append a change entry to `wiki/log.md` (format: `## YYYY-MM-DD | ingest | source name`).
8. If the source is already in `raw/`, leave it untouched. If the user pasted
   text directly, save it to `raw/` in the appropriate subfolder before
   processing.

**Source → wiki page mapping:**
- School observations → `child-profile`, `strengths-and-needs`, `school-support-plan`
- Home observations → `child-profile`, `home-environment-plan`, `timeline`
- Practitioner calls/reports → `strengths-and-needs`, `school-support-plan`, `open-questions`
- Voice notes / brain dumps → treat as home observation unless it references a
  specific meeting or practitioner
- Meeting notes → `school-meeting-ground-truth`, `school-meeting-plan`,
  `upcoming-tasks`, `people-and-roles`

## Voice note workflow

The user records voice observations and meeting summaries on their phone,
transcribes them with an AI assistant (Claude, ChatGPT, or similar), and
pastes or saves the result here for ingestion.

When the user pastes a raw transcript directly into the conversation:
1. Clean up transcription artifacts (filler words, run-ons) without changing
   the meaning.
2. Format it using the structure in `templates/voice-note-intake.md`.
3. Save it to `raw/voice-notes/YYYY-MM-DD-[short-title].md`.
4. Then proceed with the standard ingest workflow above.

When the user pastes an already-formatted summary (pre-processed by another AI):
1. Save it to the appropriate `raw/` subfolder.
2. Proceed with the standard ingest workflow.

## Meeting prep

When the user says "prep for [meeting type]" or "help me prepare for [date]":

1. Read `wiki/child-profile.md`, `wiki/strengths-and-needs.md`, and
   `wiki/open-questions.md`.
2. Read any relevant existing meeting plans (e.g. `wiki/school-meeting-plan.md`).
3. Identify what evidence exists vs. what is still a working hypothesis.
4. Identify the open questions most relevant to this meeting.
5. Draft an agenda and a list of questions to bring, grounded only in what is
   documented in the wiki.
6. Note what evidence gaps the meeting could fill.

## Synthesis commands

**"Update the child profile"** — re-read all `raw/` sources added since the
last log entry and refresh `wiki/child-profile.md` and
`wiki/strengths-and-needs.md` to reflect the current picture.

**"What's changed since [date]"** — scan `wiki/log.md` and the relevant
`raw/` files to summarize what's been added or updated.

**"Draft a one-pager for [person]"** — produce a concise, professional summary
of the child's current picture suitable for sharing with a teacher, clinician,
or administrator. Ground every claim in documented sources. Mark anything that
is a working hypothesis rather than confirmed fact.

**"What are the open questions"** — read `wiki/open-questions.md` and group by
theme (school, home, clinical, relational).

## Non-negotiable rules (from AGENTS.md)

- Never invent events, diagnoses, quotations, or professional recommendations.
- Separate observation from interpretation — use explicit language ("parent
  observed", "teacher reported", "working hypothesis").
- Mark uncertainty explicitly. Preserve disagreements between sources.
- Cite the raw source supporting every wiki claim.
- Keep the parent as the final decision-maker. Do not give clinical, legal, or
  educational advice — give organized information.
