# Domain Docs

Which of this repository's domain documents to read before working in it, and in what order.

## Before exploring, read these

- **`CONTEXT.md`** at the repo root — the glossary.
- **`CONSTITUTION.md`** — the rules every change follows.
- **`docs/adr/`** — architectural decisions, when there are any.

This is a single-context repo. There is no `CONTEXT-MAP.md`.

## File structure

```
/
├── vocabularies/           ← the source files, one vocabulary each, edited by hand
├── scripts/                ← build_vocabularies.py
├── tests/                  ← the checks every vocabulary must pass
├── CONTEXT.md              ← glossary
└── CONSTITUTION.md         ← rules and quality bar
```

## Where a concept's meaning comes from

- **Relation types** take their definitions from the DataCite Metadata Schema 4.4, and
  **organization types** from the Research Organization Registry's data structure. Change one
  only to follow the standard it comes from.
- **Every other vocabulary** describes how FairDM records research metadata. Its definitions are
  settled with the maintainers in an issue, never reworded from inference.

A concept's stored value (`skos:notation`) is what existing FairDM data holds. Never change it,
even to correct its spelling.

## Use the glossary's vocabulary

When your output names a concept from this repository — in an issue title, a pull request or a
test name — use the term as defined in `CONTEXT.md`. If the term you need is not there, either
you are inventing language the project does not use, or there is a gap worth recording.
