#!/bin/bash

source venv/bin/activate

cd "$1"
pytest test
