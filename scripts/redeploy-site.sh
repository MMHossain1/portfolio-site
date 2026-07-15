#!/bin/bash

tmux kill-server
cd "$(dirname "$0")/.."
git fetch && git reset origin/main --hard

python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt

tmux new -s new-sever
flask run --host=0.0.0.0
