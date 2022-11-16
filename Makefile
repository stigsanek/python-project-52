run:
	poetry run python manage.py runserver

install:
	poetry install

build:
	poetry build

publish:
	poetry publish --dry-run

package-install:
	python3 -m pip install --user dist/*.whl

lint:
	poetry run flake8 task_manager tests

test:
	poetry run pytest

test-coverage:
	poetry run pytest --cov=task_manager --cov-report xml
