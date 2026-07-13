#!/bin/bash

tmux kill-server
cd "$(dirname "$0")/.."
git fetch && git reset origin/main --hard

python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt

tmux new-session -d -s flask "cd $(pwd) && source .venv/bin/activate && export FLASK_APP=app && flask run"
