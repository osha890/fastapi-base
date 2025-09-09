# Project Setup and Development Guide

## Environment

1. Create a `.env` file using `.env.template` as a reference.
2. If you plan to run the database using Docker, set the following variables in your `.env` file according to `docker-compose.yml`:

```
DB__NAME=<your_db_name>
DB__USER=<your_db_user>
DB__PASSWORD=<your_db_password>
```

## Running the Database

1. Start the database and Adminer with Docker:

```bash
docker compose up -d
```

2. Default ports:

- PostgreSQL: `5432`
- Adminer: `8080`

## Working with Models

1. Add new models in `core.models`.
2. Make sure to include them in `core.models.__init__.py` so Alembic can detect them.
3. All models should inherit from `Base`.
4. If you want the `id` field to be an integer primary key, inherit from `IdIntPkMixin`.

## Database Migrations

1. Create migrations:

```bash
alembic revision --autogenerate -m "create some table"
```

2. Apply migrations:

```bash
alembic upgrade head
```

3. Cancel migrations:

- Rollback the last migration:
```bash
alembic downgrade -1
```
- Rollback all migrations to base:
```bash
alembic downgrade base
```

## API Apps

1. Create new apps inside the `api` package.
2. App should contain:
   - `schemas`
   - `crud`
   - `views`  
   etc.
3. Include the app's router in the main API router in `api.__init__.py`.

## Pre-commit Setup

1. We use `black` and `isort` for code formatting.
2. If you add a new package in the root project, make sure to add it to `known_first_party` in `pyproject.toml`.
3. To run pre-commit manually:

```bash
pre-commit run --all-files
```

## Poetry Usage

1. Rename the project
- Open `pyproject.toml` and change the project name:
```toml
[project]
name = "new-project-name"
```

2. Remove old virtual environment (if it exists):
```bash
poetry env remove python
```

3. Disable keyring (to avoid errors on Linux):
- For current terminal session:
```bash
export PYTHON_KEYRING_BACKEND=keyring.backends.null.Keyring
```
- Or permanently for the project:
```bash
poetry config keyring.disable true --local
```

4. Install dependencies

- To create a new virtual environment and install dependencies:
```bash
poetry install
```

5. Add a new package:

```bash
poetry add <package_name>
```

6. Remove a package:

    ```bash
    poetry remove <package_name>
    ```
   
## Git
---

Follow these steps for a smooth development workflow.
