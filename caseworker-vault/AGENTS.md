# AI Maintenance Rules

## Purpose

Maintain a useful, humane, evidence-based working model of this fictional child's needs across school, home, and support settings.

## Core Architecture

1. `raw/` contains direct source material and is the source of truth.
2. `wiki/` contains synthesis, comparisons, plans, and current understanding.
3. `templates/` contains reusable capture formats.

## Non-Negotiable Rules

- Never invent events, diagnoses, quotations, or professional recommendations.
- Separate observation from interpretation.
- Mark uncertainty explicitly.
- Preserve disagreements between sources instead of silently resolving them.
- Keep historical information unless asked to remove it.
- Cite the raw notes supporting every important synthesis.
- Use neutral, non-pathologizing language.
- Do not provide clinical, legal, or educational advice.
- Keep the parent or responsible adult as the final decision-maker.

## Ingestion Workflow

When a new source is added:

1. Preserve it in `raw/`.
2. Extract dated observations, decisions, questions, and tasks.
3. Update the relevant `wiki/` pages.
4. Add unresolved questions to [[wiki/open-questions]].
5. Add concrete actions to [[wiki/upcoming-tasks]].
6. Append a change entry to [[wiki/log]].

## Preferred Distinctions

- fact vs interpretation
- need vs strategy
- strategy vs evidence that it worked
- one-time event vs recurring pattern
- school observation vs home observation
- confirmed information vs working hypothesis

## Standard Page Structure

Substantive wiki pages should include:

- `## Summary`
- `## Current Understanding`
- `## Sources`
- `## Open Questions` when uncertainty remains
