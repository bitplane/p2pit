#!/bin/bash

source venv/bin/activate


for toml in */pyproject.toml; do
	project=$(dirname $toml)
    ./build-scripts/auto-format.sh "$project" || exit 1
    ./build-scripts/linter.sh "$project" || exit 1
done
