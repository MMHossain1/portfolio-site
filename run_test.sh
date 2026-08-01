#!/bin/bash

if [ -x "$PWD/.venv/bin/python" ]; then
	"$PWD/.venv/bin/python" -m unittest discover -v tests/
elif command -v python3 >/dev/null 2>&1; then
	python3 -m unittest discover -v tests/
else
	python -m unittest discover -v tests/
fi