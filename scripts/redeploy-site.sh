#!/bin/bash

git fetch && git reset origin/main --hard

python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt

systemctl restart myportfolio
systemctl status myportfolio