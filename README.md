# FastAPI Base Project

**Description:** This project serves as a base template for building FastAPI applications. It provides a ready-to-use structure with database integration and development tools like Alembic for migrations and pre-commit hooks for code formatting. Use this as a starting point to quickly set up new FastAPI projects.

## Project Setup Instructions

1. **Create a new project directory and navigate into it:**
```bash
mkdir project-name
cd project-name
```

2. **Clone the repository:**
```bash
git clone git@github.com:osha890/fastapi-base.git .
```

3. **Remove the default git remote:**
```bash
git remote remove origin
```

4. **Rename the project:**
Edit the `pyproject.toml` file and update the project name:
```toml
[project]
name = "project-name"
```

5. **Install dependencies using Poetry:**
```bash
poetry install
```

6. **Activate the virtual environment:**
```bash
poetry env activate
```

7. **Set Python interpreter in IDE (optional):**

Get the Python interpreter path:
```bash
poetry run which python
```
Then in your IDE:  
File → Settings → Project → Python Interpreter → ⚙️ → Add Interpreter → Add Local Interpreter → Select existing → Paste the provided path

8. **Configure your database environment variables:**
```bash
DB__NAME=<your_db_name>
DB__USER=<your_db_user>
DB__PASSWORD=<your_db_password>
```
> **Note:** If there is no `.env` file, the variables will be taken from `.env.template`

9. **Install pre-commit hook:**
```bash
pre-commit install
```

## Running the Database

1. **Start the database and Adminer using Docker:**
```bash
docker compose up -d
```

2. **Default ports:**
- PostgreSQL: `5432`
- Adminer: `8080`

## Working with Models

1. Add new models in the `db.models` package.
2. Include the new models in `db.models.__init__.py` so Alembic can detect them.
3. All models should inherit from `Base`.
4. To use an integer primary key for the `id` field, inherit from `IdIntPkMixin`.

## Database Migrations

1. **Create migrations:**
```bash
alembic revision --autogenerate -m "create some table"
```

2. **Apply migrations:**
```bash
alembic upgrade head
```

3. **Rollback migrations:**
- Rollback the last migration:
```bash
alembic downgrade -1
```
- Rollback all migrations to the base state:
```bash
alembic downgrade base
```

## Project Structure

1. Create new routers inside the `api` package and include them in the main API router in `api.__init__.py`.
2. Create new schemas inside the `schema` package.
3. Implement CRUD functions inside the `db.repositories` package.

## Pre-commit Setup

1. The project uses `black` and `isort` for code formatting.
2. If you add a new package in the root project, add it to `known_first_party` in `pyproject.toml`.
3. To run pre-commit manually:
```bash
pre-commit run --all-files
```

---

Follow these instructions to set up, develop, and maintain the FastAPI base project efficiently.
