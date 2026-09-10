#!/usr/bin/env bash
# Script de build usado no deploy (Render).
set -o errexit

pip install -r requirements.txt
python manage.py collectstatic --no-input
python manage.py migrate
