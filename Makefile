
.PHONY: all clean test dev venv install \
	test-p2pit lint-p2pit

all: test

test: test-p2pit test-example

lint: lint-p2pit lint-example

test-p2pit: install
	build-scripts/test.sh p2pit

lint-p2pit: install
	build-scripts/linter.sh p2pit

test-example: install
	build-scripts/test.sh example-chat

lint-example: install
	build-scripts/linter.sh example-chat


clean:
	build-scripts/clean.sh

install: venv/.installed

venv: venv/bin/activate

dev: venv install ./.git/hooks/pre-commit



# note: non-phony requirements can't rely on phony ones

venv/.installed: venv/bin/activate */pyproject.toml build-scripts/install.sh
	build-scripts/install.sh
	touch venv/.installed

venv/bin/activate: build-scripts/venv.sh
	build-scripts/venv.sh

.git/hooks/pre-commit: build-scripts/pre-commit-hook.sh build-scripts/install-pre-commit-hook.sh
	build-scripts/install-pre-commit-hook.sh
