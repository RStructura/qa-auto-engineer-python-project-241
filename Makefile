install:
	uv sync

run:
	uv run gendiff file1.json file2.json

test:
	uv run pytest

test-coverage:
	uv run pytest --cov=gendiff --cov-report xml

lint:
	uv run ruff check

check:
	test lint

build:
	uv build

.PHONY:
	install test lint selfcheck check build
