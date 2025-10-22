# Agent Guidelines for SXT 2023 API

## Commands
- **Format**: `make format` or `poetry run python -m black .` and `poetry run python -m isort .`
- **Run server**: `poetry run python manage.py runserver`
- **Run tests**: `poetry run python manage.py test` (Django's test framework)
- **Run single test**: `poetry run python manage.py test sxt_2023.apps.app_name.tests.TestClassName.test_method_name`
- **Migrations**: `poetry run python manage.py makemigrations` and `poetry run python manage.py migrate`
- **Shell**: `poetry run python manage.py shell` (IPython available)
- **Collect static**: `poetry run python manage.py collectstatic --noinput`

## Architecture
- **Python 3.13** with **Django 5.2** REST API using **DRF** and **drf-spectacular** for OpenAPI docs at `/back/api/schema/redoc/`
- **PostgreSQL 18.0** with `psqlextra.backend`, configured via env vars (DB_NAME, DB_USER, DB_PASSWORD, DB_HOST, DB_PORT)
- **Apps**: `people` (custom User model + auth), `sxt2023_api` (main API with brands fixtures)
- **Email**: django-wailer for templated emails (registration, raffleconfirmation types)
- All URLs prefixed with `/back`, static files served from `staticfiles/` in DEBUG mode

## Code Style
- **Formatter**: Black + isort (profile="black", known_first_party="sxt_2023")
- **Imports**: Use absolute imports from `sxt_2023` (e.g., `from sxt_2023.apps.people.models import User`)
- **Auth**: Custom User model at `people.User` (AUTH_USER_MODEL)
- **Settings**: Environment-based config (DEBUG, SECRET_KEY, ALLOWED_HOSTS from env vars)
- **Note**: dj-database-url is NOT installed, DATABASE_URL parsing is disabled
