#!/bin/bash

# activate venv
source venv/bin/activate

# install all projects into the venv

for reqs in */pyproject.toml; do
	project=$(dirname "$reqs")
    python3 -m pip install -e "$project"[dev] || exit 1
done
