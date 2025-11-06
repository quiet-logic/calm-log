PYTHON ?= python3
PKG_DIR := name_format_pkg

.PHONY: test install dev-install reinstall uninstall cli clean clean-pyc

## Run the test suite
test:
	$(PYTHON) -m pytest -q

## One-time install (wheel)
install:
	cd $(PKG_DIR) && $(PYTHON) -m pip install .

## Editable install (recommended while developing)
dev-install:
	cd $(PKG_DIR) && $(PYTHON) -m pip install -e . --no-build-isolation

## Reinstall editable (force refresh)
reinstall:
	-$(PYTHON) -m pip uninstall -y name-format
	$(MAKE) dev-install

## Quick CLI smoke run (module form; ignores PATH)
cli:
	$(PYTHON) -m name_format.cli "ó brien"

## Clean Python junk
clean-pyc:
	find . -name "__pycache__" -type d -prune -exec rm -rf {} +
	find . -name "*.pyc" -delete -o -name "*.pyo" -delete

## Clean build + test artifacts
clean: clean-pyc
	rm -rf .pytest_cache *.egg-info build dist

## Format with Black
fmt:
	$(PYTHON) -m black name_format_pkg tests


## Lint with Ruff
lint:
	$(PYTHON) -m ruff check name_format_pkg tests


## Bump version patch
bump-patch:
	$(PYTHON) tools/bump_version.py patch


bump-minor:
	$(PYTHON) tools/bump_version.py minor


bump-major:
	$(PYTHON) tools/bump_version.py major


## Build package
build:
	cd name_format_pkg && $(PYTHON) -m build

