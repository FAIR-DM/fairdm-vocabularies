FairDM Vocabularies
===================

The FairDM Vocabularies are the controlled terms that `FairDM
<https://github.com/FAIR-DM/fairdm>`_ research data portals use for the metadata they store
on projects, datasets, samples, measurements and contributors: the kinds of identifier,
description and date a record can carry, the roles people and organizations play, and the
status of a project or a sample.

Each vocabulary is a SKOS concept scheme. Every vocabulary, concept and collection has a URI
under ``https://w3id.org/fairdm/vocabularies/`` and a page on this site, with its RDF in
Turtle, JSON-LD, RDF/XML and N-Triples beside it. The vocabularies are released under the
`Creative Commons Attribution 4.0 International licence
<https://creativecommons.org/licenses/by/4.0/>`_.

The source files, the release downloads and the changelog are in the `GitHub repository
<https://github.com/FAIR-DM/fairdm-vocabularies>`_.

How to cite
-----------
Cite a vocabulary when your data, software or paper uses its terms. The licence, CC BY 4.0,
asks for credit wherever the vocabularies are reused.

1. Find the version you used. Versions are the `releases
   <https://github.com/FAIR-DM/fairdm-vocabularies/releases>`_ of the repository, numbered
   ``<year>.<release>``, such as ``2026.1``.

2. Cite the vocabulary by its name, its version and its URI:

   .. code-block:: text

      FairDM (2026). Date types. FairDM Vocabularies, version 2026.1.
      https://w3id.org/fairdm/vocabularies/date-types

3. To point at one concept, give the concept's URI as well. The URI never changes, and a
   withdrawn concept keeps its page, so the reference keeps resolving:

   .. code-block:: text

      https://w3id.org/fairdm/vocabularies/date-types/available

.. toctree::
   :hidden:

   Home <self>
   vocabularies/index
