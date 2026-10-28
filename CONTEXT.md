# Glossary

The words this repository uses for its own concepts. Issues, pull requests, tests and
documentation use these terms as defined here.

| Term | Definition | Avoid |
| --- | --- | --- |
| **Vocabulary** | One SKOS concept scheme, held in one file under `vocabularies/`. The file name is the last part of the vocabulary's address (`date-types.ttl` is `https://w3id.org/fairdm/vocabularies/date-types`). | "list", "choices", "enum" |
| **Concept** | One entry in a vocabulary (`skos:Concept`). It has a label, a definition and a stored value. | "option", "choice", "value" |
| **Collection** | The selection of a vocabulary's concepts that one kind of record may use, such as the identifier types a dataset can have (`skos:OrderedCollection`). It lists its concepts in the order a portal shows them. A collection groups concepts and is not itself one. | "subset", "category" |
| **Record type** | The kind of FairDM record a collection is for: project, dataset, sample, measurement, person, organization or contributor. Each collection is named after one. | "model", "entity" |
| **Address** | The URI that identifies a vocabulary, concept or collection. A concept's address is its vocabulary's address, a slash, and its identifier. Once published, an address is permanent. | "URL", "ID" |
| **Base address** | The part every address starts with, today `https://w3id.org/fairdm/vocabularies/`. It is set once, as `BASE_URL` in `scripts/build_vocabularies.py`, and appears in a source file only in its `PREFIX` lines. | "namespace", for this |
| **Identifier** | The last part of a concept's address (`rights-holder` in `…/contributor-roles/rights-holder`): lower case, words joined by hyphens. | "slug", "key" |
| **Stored value** | The code FairDM stored for a concept before the concept had an address (`RightsHolder`, `IsCitedBy`, `0`), kept as the concept's `skos:notation`. A portal matches on it to convert its existing data to addresses, so it never changes. | "key", "code", "choice value" |
| **Label** | The name of a concept as people read it (`skos:prefLabel`). One per language. | "name", "title" |
| **Description** | The sentence that says what a vocabulary covers (`dcterms:description` on the concept scheme). | "definition", for a vocabulary |
| **Definition** | The sentence that says what a concept means (`skos:definition`). One per language. | "description" |
| **Translation** | A label or definition in a language other than English, stored on the same concept with its language tag (`"Rechteinhaber"@de`). | — |
| **Match** | A link from a concept to the same or a nearly identical concept in another vocabulary, at that vocabulary's own URI (`skos:exactMatch`, `skos:closeMatch`). | "mapping", "equivalent" |
| **Source file** | A Turtle file in `vocabularies/`. Source files are the only files anyone edits. | "input" |
| **Export** | A copy of a vocabulary in another RDF format (RDF/XML, JSON-LD, N-Triples), generated from its source file and attached to a release. Exports are never committed or edited by hand. | "build", "output" |
| **Fixed layout** | The exact Turtle text rdflib writes for a vocabulary (its `longturtle` format), with two prefixes: `fairdm:` for the base address, so a vocabulary reads `fairdm:date-types`, and the empty prefix for the vocabulary's own namespace, so its concepts read `:available`. Records come in a fixed order: the publications, then the organizations, then the vocabulary, then its collections, then its concepts, each group sorted by address. A collection's `skos:memberList` is written inside the collection's record. Every source file is kept in it, so a diff shows only what changed in meaning. | "formatting" |
