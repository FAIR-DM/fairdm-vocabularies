# Changelog

All notable changes to the vocabularies are recorded here. Versions are calendar versions,
`<year>.<release>`.

## [Unreleased]

### Added

- Nine vocabularies, with 127 concepts:
  - contributor roles (29), date types (17), description types (17), identifier types (10) and
    sample status (5), carried across from FairDM with every label and definition unchanged,
    and the selection each record type is offered as an ordered collection;
  - organization types (9), with definitions from the Research Organization Registry (ROR);
  - project status (5);
  - relation types (34), with definitions from the DataCite Metadata Schema 4.4;
  - sample relation types (1).
- Every concept records the value FairDM stored for it as its `skos:notation`.
- Identifier types link to the identifier schemes of the DataCite Ontology
  (`http://purl.org/spar/datacite/`).
- Checks that run on every pull request, and a Publish workflow that attaches every vocabulary
  in Turtle, RDF/XML, JSON-LD and N-Triples to each release.
