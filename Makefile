locale-make:
	django-admin makemessages -l en

locale-build:
	django-admin compilemessages

migrate:
	poetry run python manage.py migrate

run:
	poetry run python manage.py runserver

install:
	poetry install

build:
	poetry build

publish:
	poetry publish --dry-run

lint:
	poetry run flake8 task_manager

test:
	poetry run pytest

test-coverage:
	poetry run pytest --cov=task_manager --cov-report xml
