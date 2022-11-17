run:
	poetry run python manage.py runserver

locale-make:
	poetry run python manage.py makemessages -l en
	poetry run python manage.py compilemessages

migrate:
	poetry run python manage.py makemigrations
	poetry run python manage.py migrate

createsuperuser:
	poetry run python manage.py createsuperuser

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
