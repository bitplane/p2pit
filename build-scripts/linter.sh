#!/bin/bash

source venv/bin/activate

flake8 "$1"/"$1" "$1"/test
