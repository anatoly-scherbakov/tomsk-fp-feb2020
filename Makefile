SHELL:=/usr/bin/env bash

.PHONY: lint
lint:
	mypy tomsk_fp_feb2020 tests/**/*.py
	flake8 .

.PHONY: unit
unit:
	pytest

.PHONY: package
package:
	poetry check
	pip check
	safety check --bare --full-report

.PHONY: test
test: lint unit package
