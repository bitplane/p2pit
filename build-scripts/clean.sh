#!/bin/bash

rm -r venv
find . -name '*.pyc' -delete
find . -name '__pycache__' -delete
find . -name '*.egg-info' -delete

echo Cleaned project
