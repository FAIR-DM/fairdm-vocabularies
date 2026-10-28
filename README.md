# FairDM Vocabularies

[![Checks](https://github.com/FAIR-DM/fairdm-vocabularies/actions/workflows/checks.yml/badge.svg)](https://github.com/FAIR-DM/fairdm-vocabularies/actions/workflows/checks.yml)
[![Vocabularies: CC BY 4.0](https://img.shields.io/badge/vocabularies-CC%20BY%204.0-lightgrey.svg)](https://github.com/FAIR-DM/fairdm-vocabularies/blob/main/LICENSE-CC-BY-4.0)

The FairDM Vocabularies are the controlled terms that [FairDM](https://github.com/FAIR-DM/fairdm)
research data portals use for the metadata they store on projects, datasets, samples,
measurements and contributors: the kinds of identifier, description and date a record can carry,
the roles people and organizations play, and the status of a project or a sample.

Each vocabulary is a SKOS (Simple Knowledge Organization System) concept scheme written in RDF
Turtle. Keeping the vocabularies here, rather than inside the FairDM code, means:

- **A stored value explains itself.** A portal's database stores the concept's URI, and anyone
  can follow that URI to see what the concept means.
- **Every concept carries its own metadata.** Each concept has a label and a definition.
  Translations are further language-tagged labels on the same concept, so they never change its
  URI. Where another vocabulary publishes the same concept at a URI of its own, the concept links
  to it with `skos:exactMatch` or `skos:closeMatch`.
- **Concepts change without a software release.** A new or corrected concept reaches a portal
  when the portal re-imports the vocabulary with the `sync_vocabularies` command of
  [django-controlled-vocabularies](https://github.com/FAIR-DM/django-controlled-vocabularies).
  No FairDM release is needed.

Every vocabulary and concept has a URI under `https://w3id.org/fairdm/vocabularies/`. The Turtle
files are edited directly and checked automatically on every change. Each versioned release
publishes them, with copies in RDF/XML, JSON-LD and N-Triples. The vocabularies are released
under the Creative Commons Attribution 4.0 International licence (CC BY 4.0).

## Vocabularies

### Contributor roles

- **Name:** `contributor-roles`
- **URI:** <https://w3id.org/fairdm/vocabularies/contributor-roles>
- **Source:** <https://github.com/FAIR-DM/fairdm-vocabularies/blob/main/vocabularies/contributor-roles.ttl>

Roles a person or organization can have in a project, dataset, sample or measurement.

### Date types

- **Name:** `date-types`
- **URI:** <https://w3id.org/fairdm/vocabularies/date-types>
- **Source:** <https://github.com/FAIR-DM/fairdm-vocabularies/blob/main/vocabularies/date-types.ttl>

Kinds of date recorded for projects, datasets, samples and measurements, such as when a dataset was published or a sample was collected.

### Description types

- **Name:** `description-types`
- **URI:** <https://w3id.org/fairdm/vocabularies/description-types>
- **Source:** <https://github.com/FAIR-DM/fairdm-vocabularies/blob/main/vocabularies/description-types.ttl>

Kinds of description recorded for projects, datasets, samples and measurements, such as an abstract or the methods used.

### Identifier types

- **Name:** `identifier-types`
- **URI:** <https://w3id.org/fairdm/vocabularies/identifier-types>
- **Source:** <https://github.com/FAIR-DM/fairdm-vocabularies/blob/main/vocabularies/identifier-types.ttl>

Kinds of persistent identifier recorded for projects, datasets, samples, measurements, people and organizations.

### Organization types

- **Name:** `organization-types`
- **URI:** <https://w3id.org/fairdm/vocabularies/organization-types>
- **Source:** <https://github.com/FAIR-DM/fairdm-vocabularies/blob/main/vocabularies/organization-types.ttl>

The kind of institution an organization is, from the organization types of the Research Organization Registry (ROR).

### Project status

- **Name:** `project-status`
- **URI:** <https://w3id.org/fairdm/vocabularies/project-status>
- **Source:** <https://github.com/FAIR-DM/fairdm-vocabularies/blob/main/vocabularies/project-status.ttl>

The stages a research project moves through, from first idea to completion.

### Relation types

- **Name:** `relation-types`
- **URI:** <https://w3id.org/fairdm/vocabularies/relation-types>
- **Source:** <https://github.com/FAIR-DM/fairdm-vocabularies/blob/main/vocabularies/relation-types.ttl>

How a resource relates to another resource, from the relation types of the DataCite Metadata Schema. In each definition, A is the resource being described and B is the related resource.

### Sample relation types

- **Name:** `sample-relation-types`
- **URI:** <https://w3id.org/fairdm/vocabularies/sample-relation-types>
- **Source:** <https://github.com/FAIR-DM/fairdm-vocabularies/blob/main/vocabularies/sample-relation-types.ttl>

How one physical sample relates to another.

### Sample status

- **Name:** `sample-status`
- **URI:** <https://w3id.org/fairdm/vocabularies/sample-status>
- **Source:** <https://github.com/FAIR-DM/fairdm-vocabularies/blob/main/vocabularies/sample-status.ttl>

The custody state of a physical sample: whether it is available, in use, stored, destroyed or unknown.

## Using the vocabularies

Each [release](https://github.com/FAIR-DM/fairdm-vocabularies/releases) carries every vocabulary
in four formats, as separate files that differ only by extension:

| Format | Extension |
| --- | --- |
| Turtle | `.ttl` |
| RDF/XML | `.rdf` |
| JSON-LD | `.jsonld` |
| N-Triples | `.nt` |

A link with `latest` always returns the file from the newest release:

```text
https://github.com/FAIR-DM/fairdm-vocabularies/releases/latest/download/contributor-roles.ttl
```

Each release also carries `vocabularies-full.zip`: every vocabulary in every format, with this
README, the changelog and the licence, in a folder named after the version.

Any RDF library can read the files. For example, with [rdflib](https://rdflib.readthedocs.io):

```python
from rdflib import Graph

url = "https://github.com/FAIR-DM/fairdm-vocabularies/releases/latest/download/contributor-roles.ttl"
graph = Graph().parse(url, format="turtle")
```

### Collections

Most vocabularies offer a different selection of their concepts to each kind of record. A
dataset can have a DOI, for example, and a person an ORCID iD. Each selection is a
`skos:OrderedCollection` in the vocabulary, named after the kind of record
(`https://w3id.org/fairdm/vocabularies/identifier-types/dataset`), and lists its concepts in the
order a portal shows them.

### Stored values

Before these vocabularies, FairDM stored a short code for each concept rather than its URI.
Each concept records that code as its `skos:notation`, so a portal can convert the values it
already holds into URIs.

A concept's URI never changes once it is published. A concept that is withdrawn stays in its
vocabulary, marked as deprecated, so data that refers to it keeps resolving.

## Repository structure

```text
vocabularies/          the vocabularies, one Turtle file each: the only files edited
scripts/
  build_vocabularies.py  rewrites the Turtle files in their fixed layout, and exports them
tests/                 the checks every vocabulary must pass
docs/                  the documentation site: its settings and its own pages
.github/workflows/
  checks.yml           runs the checks on every pull request
  publish.yml          creates a release and attaches its files
CHANGELOG.md           what changed in each release
CONSTITUTION.md        the rules every change follows
CONTEXT.md             the words used for the parts of a vocabulary
```

### How the vocabularies are maintained

The Turtle files in `vocabularies/` are the vocabularies. There is no other source and no
generated copy in the repository. A change is made by editing a file directly, in a pull request:

```bash
uv sync
uv run python scripts/build_vocabularies.py
uv run pytest
```

The build script rewrites every file in one fixed layout, so a diff shows only what changed in
meaning. The checks run on every pull request and confirm that every file parses and that:

- each file holds one vocabulary, named after the file, with an English label and description
- each vocabulary names its creator, publisher and licence, and cites any source its concepts come from
- every concept belongs to its vocabulary and has one English label, one stored value in `skos:notation`, and a URI under the vocabulary's URI
- no two concepts offered together share a label, within one collection or within a vocabulary that has no collections
- every label and definition has a language tag and is not empty
- every concept a collection or relationship names exists, and an ordered collection lists each concept once
- `skos:broader`, `skos:narrower` and `skos:related` are stated in both directions, and the top concepts are exactly those with no broader concept
- stored values in `skos:notation` are unique within a vocabulary
- every vocabulary can be written in every release format without losing anything
- the documentation site builds without warnings and its front page lists every vocabulary

The rules behind these checks are in
[`CONSTITUTION.md`](https://github.com/FAIR-DM/fairdm-vocabularies/blob/main/CONSTITUTION.md), and
the words used for the parts of a vocabulary are in
[`CONTEXT.md`](https://github.com/FAIR-DM/fairdm-vocabularies/blob/main/CONTEXT.md).

### How the documentation site is built

The site in `docs/` is built with [Sphinx](https://www.sphinx-doc.org/) and
[sphinx-skos](https://github.com/FAIR-DM/sphinx-skos), which writes a page for every
vocabulary, concept and collection, at its URI with `https://w3id.org/fairdm/vocabularies/`
removed, and its RDF beside it. Those pages are written on every build and are not committed.
The front page and the how-to guides are the only pages kept in `docs/`. A new vocabulary is
added to the list on the front page, `docs/index.rst`, and its two generated paths to
`.gitignore`.

```bash
uv run sphinx-build -W -b dirhtml docs docs/_build/dirhtml
```

### How releases are made

A maintainer runs the **Publish** workflow from the repository's Actions tab, on `main`. It runs
the checks, works out the next version from the current year and the last release (`v2026.1`,
`v2026.2`, then `v2027.1` in a new year), and creates the release with the `[Unreleased]` notes
from `CHANGELOG.md`. It then exports every vocabulary into every format and attaches the files and
the release archive.

What changed in each release is recorded in
[`CHANGELOG.md`](https://github.com/FAIR-DM/fairdm-vocabularies/blob/main/CHANGELOG.md).
Changes waiting for the next release are listed under `[Unreleased]`.

## Contributing

Suggestions and corrections are welcome. Please open an
[issue](https://github.com/FAIR-DM/fairdm-vocabularies/issues) to discuss a change before opening
a pull request.

## Scope & philosophy

**What this is.** The single published source of the vocabularies FairDM portals store values
from. FairDM and the portals built on it import these files rather than keeping their own copies.

**What this is not.** It is not software. There is no package to install, and the only code is
the script that checks and exports the files. It does not hold the vocabularies of one research
field, such as the measurement methods of a discipline: the portal for that field publishes
those itself.

**When in doubt:**

- The Turtle file is the truth. Every other format is derived from it.
- Data that already refers to a concept matters more than tidiness. Correct a label or a
  definition, but never change what a published URI means.
- A translation is another language-tagged label on the same concept, never a separate file.
- Link to another vocabulary only where it publishes the concept at a URI of its own.

## License

The vocabularies, in `vocabularies/` and in every release archive, are licensed under the
[Creative Commons Attribution 4.0 International License](https://github.com/FAIR-DM/fairdm-vocabularies/blob/main/LICENSE-CC-BY-4.0).
The script and tests are licensed under the
[MIT License](https://github.com/FAIR-DM/fairdm-vocabularies/blob/main/LICENSE).
