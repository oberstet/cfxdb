Changelog
=========

This document contains a reverse-chronological list of changes to cfxdb.

.. note::

    For detailed release information including artifacts,
    see :doc:`releases`.

Unreleased
----------

*No unreleased changes yet.*

26.6.1 (2026-06-18)
-------------------

**Dependencies**

* Require ``zlmdb >= 26.6.1`` and ``autobahn[all] >= 26.6.1`` for the coordinated WAMP 26.6.1 release (`#117 <https://github.com/crossbario/cfxdb/issues/117>`_)

**Build & CI/CD**

* Bump the shared ``wamp-ai`` (→ ``4669dc8``) and ``wamp-cicd`` (→ ``f77ca2b``) Git submodules to match the rest of the WAMP project group; the ``wamp-cicd`` bump carries the GHSA-6658 shell-injection hardening in the shared ``identifiers.yml`` reusable workflow (`#117 <https://github.com/crossbario/cfxdb/issues/117>`_)
* Converge the GitHub Discussions release announcement onto a single mechanism, matching autobahn-python / txaio: the ``release-post-comment.yml`` workflow now resolves the ``ci-cd`` Discussions category **by name** (case-insensitive) and posts for both nightly and stable releases, and the redundant ``softprops`` ``discussion_category_name`` was removed from the release steps so a release posts exactly one announcement (`#117 <https://github.com/crossbario/cfxdb/issues/117>`_, resolves `#114 <https://github.com/crossbario/cfxdb/issues/114>`_)

25.12.2 (2025-12-15)
--------------------

**New**

* Added ``generate-release-notes`` justfile recipe for documentation integration
* Added ``docs-integrate-github-release`` justfile recipe with chain-of-custody files
* Added ``.github/workflows/README.md`` documenting CI/CD architecture
* Added ``release-post-comment.yml`` workflow for GitHub Discussions notifications

**Fix**

* Fixed autoapi duplicate object warnings by adding suppress_warnings in conf.py (#82)
* Consolidated ``download-github-release`` recipe to use ``/tmp/release-artifacts/<tag>`` path
* Fixed release workflow to properly upload wheels (corrected check-release-fileset parameters)
* Fixed OpenSSL checksum format handling in download-github-release recipe
* Aligned download-github-release recipe with autobahn-python/zlmdb for consistency

**Other**

* Updated dependencies: autobahn[all]>=25.12.2, zlmdb>=25.12.2
* Removed tox from dev dependencies (no longer used)
* Added documentation for WHY both zlmdb and autobahn dependencies are needed (#112)

25.12.1 (2025-12-10)
--------------------

**New**

* Modernized build system: migrated from setup.py to pyproject.toml with hatch backend
* Added comprehensive just recipes for development workflow (create, install-dev, check, test, docs, dist)
* Added uv for fast Python environment management
* Added ruff for code formatting and linting (replaces flake8/black)
* Added ty (Astral) for type checking
* Added Sphinx documentation with MyST Markdown support and furo theme
* Added sphinx-autoapi for automatic API documentation generation
* Modernized CI/CD workflows with chain-of-custody verification using wamp-cicd reusable actions

**Fix**

* Fixed flatbuffers import: now uses zlmdb's vendored flatbuffers via ``from zlmdb import flatbuffers``
* Fixed import sorting (I001) errors across all source files
* Excluded generated code (``src/cfxdb/gen``) from ruff linting

**Other**

* Updated dependencies: autobahn>=25.12.1, zlmdb>=25.12.1
* Added Python 3.11, 3.12, 3.13, 3.14 support in CI
* Dropped Python 3.9, 3.10 support (minimum is now Python 3.11)

..
    Format for entries:

    vX.Y.Z (YYYY-MM-DD)
    -------------------

    **New**

    * Description of new feature (#issue)

    **Fix**

    * Description of bug fix (#issue)

    **Other**

    * Description of other changes (#issue)
