# Task Manager

![GitHub Workflow Status](https://img.shields.io/github/workflow/status/stigsanek/task-manager/python-ci)
![Code Climate maintainability](https://img.shields.io/codeclimate/maintainability/stigsanek/task-manager)
![Code Climate coverage](https://img.shields.io/codeclimate/coverage/stigsanek/task-manager)

## Description

"Task Manager" is a task management system. It allows you to set tasks, assign performers and change their statuses.
Registration and authentication are required to work with the system.

## Install

### Python

Before installing the package, you need to make sure that you have Python version 3.8 or higher installed.

```bash
>> python --version
Python 3.8.0+
```

If you don't have Python installed, you can download and install it
from [the official Python website](https://www.python.org/downloads/).

### Poetry

The project uses the Poetry manager. Poetry is a tool for dependency management and packaging in Python. It allows you
to declare the libraries your project depends on and it will manage (install/update) them for you. You can read more
about this tool on [the official Poetry website](https://python-poetry.org/)

### Dependencies

To work with the package, you need to clone the repository to your computer. This is done using the `git clone` command.
Clone the project on the command line:

```bash
# clone via HTTPS:
>> git clone https://github.com/stigsanek/task-manager.git
# clone via SSH:
>> git@github.com:stigsanek/task-manager.git
```

It remains to move to the directory and install the dependencies:

```bash
>> cd task-manager
>> poetry install
```

### Environment

For the application to work, you need to create a file `.env` in the root of the project.
Then open the file and set any value for the `SECRET_KEY="your_key"`
If you want to enable debug mode, then set for the `DEBUG=True`.

### Migrations

To apply all migrations, run:

```bash
>> poetry run python manage.py makemigrations
>> poetry run python manage.py migrate
```

Finally, we can move on to using the project functionality!

## Usage

```bash
>> poetry run python manage.py runserver

Watching for file changes with StatReloader
Performing system checks...

System check identified no issues (0 silenced).
November 21, 2022 - 23:15:36
Django version 4.1.3, using settings 'task_manager.settings'
Starting development server at http://127.0.0.1:8000/
Quit the server with CTRL-BREAK.
```

Open [http://localhost:8000](http://localhost:8000) in your browser.

## Development

### Useful commands

* `make install` - install all dependencies in the environment.
* `make lint` - checking code with linter.
* `make test` - run tests.
* `make migrate` - create and apply migrations.
