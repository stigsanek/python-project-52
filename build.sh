#!/usr/bin/env bash
# exit on error
set -o errexit

pip install poetry -U

# install dependencies
poetry install --only main
poetry add psycopg2-binary gunicorn

# migrations
poetry run python manage.py migrate
