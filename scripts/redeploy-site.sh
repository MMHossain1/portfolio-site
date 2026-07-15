#!/bin/bash

tmux kill-server
cd "$(dirname "$0")/.."
git fetch && git reset origin/main --hard

python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt

if [ ! -f .env ]; then
	echo ".env not found. Run: cp example.env .env and fill MYSQL_* values"
	exit 1
fi

set -a
source .env
set +a

if [ -z "${MYSQL_HOST:-}" ] || [ -z "${MYSQL_USER:-}" ] || [ -z "${MYSQL_PASSWORD:-}" ] || [ -z "${MYSQL_DATABASE:-}" ]; then
	echo "Missing required MYSQL_* values in .env"
	exit 1
fi

tmux new -d -s new-server "cd $(pwd) && source .venv/bin/activate && set -a && source .env && set +a && export FLASK_APP=app && flask run --host=0.0.0.0 --port=5000"
echo "Flask started in tmux session: new-server"
