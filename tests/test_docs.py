"""Checks the documentation site builds and lists every vocabulary."""

import contextlib
from pathlib import Path

import pytest
from build_vocabularies import source_files
from sphinx_skos.cli import main

ROOT = Path(__file__).resolve().parent.parent
SOURCES = source_files()


@pytest.fixture(scope="module")
def site(tmp_path_factory):
    output = tmp_path_factory.mktemp("site")
    with contextlib.chdir(ROOT):
        status = main(["build", "-W", "--output", str(output)])
    return status, output


class TestSite:
    def test_builds_without_warnings(self, site):
        status, output = site
        assert status == 0

    @pytest.mark.parametrize("source", SOURCES, ids=[path.stem for path in SOURCES])
    def test_catalogue_page_links_to_the_vocabulary(self, site, source):
        status, output = site
        page = (output / "catalogue" / "index.html").read_text(encoding="utf-8")
        assert f'href="{source.stem}/"' in page
