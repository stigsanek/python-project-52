# Task Manager

[![Actions Status](https://github.com/stigsanek/python-project-52/workflows/hexlet-check/badge.svg)](https://github.com/stigsanek/python-project-52/actions)

## Description

Task Manager is a task management system. It allows you to set tasks, assign performers and change their statuses.
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

### Package

To work with the package, you need to clone the repository to your computer. This is done using the `git clone` command.
Clone the project on the command line:

```bash
# clone via HTTPS:
>> git clone https://github.com/stigsanek/python-project-52.git
# clone via SSH:
>> git@github.com:stigsanek/python-project-52.git
```

It remains to move to the directory and install the package:

```bash
>> cd python-project-52
>> poetry build
>> python -m pip install --user dist/*.whl
```

Finally, we can move on to using the project functionality!

## Usage


## Development

### Useful commands

* `make install` - install all dependencies in the environment.
* `make build` - build the wheel.
* `make lint` - checking code with linter.
* `make test` - run tests.
