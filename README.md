# Task Manager

![GitHub Workflow Status](https://img.shields.io/github/actions/workflow/status/stigsanek/task-manager/pyci.yml?branch=main)
![Code Climate maintainability](https://img.shields.io/codeclimate/maintainability/stigsanek/task-manager)
![Code Climate coverage](https://img.shields.io/codeclimate/coverage/stigsanek/task-manager)

## Description

"Task Manager" is a task management system. It allows you to set tasks, assign performers and change their statuses.
Registration and authentication are required to work with the system.

## Usage

You can deploy the project locally or via Docker.

### 1. Locally

#### Python

Before installing the package, you need to make sure that you have Python version 3.8 or higher installed.

```bash
>> python --version
Python 3.8.0+
```

If you don't have Python installed, you can download and install it
from [the official Python website](https://www.python.org/downloads/).

#### Poetry

The project uses the Poetry manager. Poetry is a tool for dependency management and packaging in Python. It allows you
to declare the libraries your project depends on and it will manage (install/update) them for you. You can read more
about this tool on [the official Poetry website](https://python-poetry.org/)

#### Dependencies

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
>> poetry install --no-root
```

#### Environment

For the application to work, you need to create a file `.env` in the root of the project:

```
SECRET_KEY="your_key"
DATABASE_URL=sqlite:///db.sqlite3
ALLOWED_HOSTS=127.0.0.1,localhost

# If you want to enable debug mode
DEBUG=True
```

#### Run

* Run database migrations:

```bash
>> python manage.py migrate

 ...
 ...
 ...
 Applying statuses.0001_initial... OK
 Applying tasks.0001_initial... OK
 Applying tasks.0002_initial... OK
```

* Run application:

```bash
>> python manage.py runserver

Watching for file changes with StatReloader
Performing system checks...

System check identified no issues (0 silenced).
December 12, 2022 - 18:07:21
Django version 4.1.3, using settings 'task_manager.settings'
Starting development server at http://127.0.0.1:8000/
Quit the server with CTRL-BREAK.
```

* Open [http://127.0.0.1:8000](http://127.0.0.1:8000) in your browser.

### 2. Docker

Docker is a platform designed to help developers build, share, and run modern applications.
You can read more about this tool on [the official Docker website](https://www.docker.com/).
You need to [install Docker Desktop](https://www.docker.com/products/docker-desktop/).
Docker Desktop is an application for the building and sharing of containerized applications and microservices.

#### Environment

Depending on the application mode, different environment files are used.
For development mode, the `.env.dev` file with basic settings has already been created.
For production mode, you need to create an `.env.prod` file:

```
# Database environment
POSTGRES_DB=task_manager
POSTGRES_USER=user
POSTGRES_PASSWORD=password
POSTGRES_HOST=db
POSTGRES_PORT=5432

# App environment
SECRET_KEY=prod
ALLOWED_HOSTS=127.0.0.1
DATABASE_URL=postgres://${POSTGRES_USER}:${POSTGRES_PASSWORD}@${POSTGRES_HOST}:${POSTGRES_PORT}/${POSTGRES_DB}
```

#### Run development mode

```bash
>> docker-compose -f compose.dev.yml up -d

 ...
 ...
 ...
 Creating task-manager_db_1 ... done
 Creating task-manager_web_1 ... done
```

Open [http://127.0.0.1:8000](http://127.0.0.1:8000) in your browser.

#### Run production mode

```bash
>> docker-compose -f compose.prod.yml up -d

 ...
 ...
 ...
 Creating task-manager_db_1 ... done
 Creating task-manager_web_1 ... done
```

Open [http://127.0.0.1:8000](http://127.0.0.1:8000) in your browser.
