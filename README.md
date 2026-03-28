# Project Catalogue

A Django web app for managing **projects**, **to-do lists**, and **tasks**, with user authentication. Each user can create projects, attach files, write notes, and organize work into todolists and tasks.

## Features

- Custom user model (email-based login)
- Authentication:
  - Sign up, log in, log out
- Project management:
  - Create / edit / delete projects
  - Upload project files
  - Add notes to projects (view/edit/delete)
- Project organization:
  - Todolists under a project
  - Tasks under a todolist (mark as done)

## Tech stack

- Python + Django (server-rendered templates)
- SQLite (default local database)
- AWS deployment tooling (repo includes):
  - `.ebextensions/` (Elastic Beanstalk config directory)
  - `.ebignore` (Elastic Beanstalk ignore file)
  - `buildspec.yml` / `buildspec2.yml` (AWS CodeBuild build specs)

## ⚠ Version note (important)

`requirements.txt` pins **Django==2.2**, but `projectcatalogue/settings.py` includes a header indicating Django **5.0.4**.

If you intend to run this project on Django 5.x, you should update `requirements.txt` accordingly. If you intend to keep Django 2.2, you’ll want to ensure the codebase matches Django 2.2 conventions and dependencies.

## Project structure (high level)

- `projectcatalogue/` – Django project settings + root URLConf
- `user/` – custom user model + login/signup/logout
- `project/` – projects + project files + project notes
- `todolist/` – todolists under a project
- `task/` – tasks under a todolist
- `core/` – landing pages (index/about/contact)
- `manage.py` – Django management entry point
- `requirements.txt` – Python dependencies

## Routes (main)

- `/` – home
- `/about/` – about
- `/contact/` – contact
- `/signup/` – create an account
- `/login/` – log in
- `/logout/` – log out
- `/projects/` – list your projects
- `/projects/<project_id>/` – project detail (and project-level actions)
- `/projects/<project_id>/<todolist_id>/` – todolist detail
- `/projects/<project_id>/<todolist_id>/<task_id>/` – task detail

## Local development

### 1) Create and activate a virtualenv (recommended)

```bash
python -m venv .venv
# macOS/Linux
source .venv/bin/activate
# Windows (PowerShell)
# .venv\Scripts\Activate.ps1
```

### 2) Install dependencies

```bash
pip install -r requirements.txt
```

### 3) Run migrations

```bash
python manage.py makemigrations
python manage.py migrate
```

### 4) Create an admin user (optional)

```bash
python manage.py createsuperuser
```

### 5) Start the dev server

```bash
python manage.py runserver
```

Open: `http://127.0.0.1:8000/`

## Deployment

### Elastic Beanstalk (AWS)

This repository includes Elastic Beanstalk configuration via:

- `.ebextensions/`
- `.ebignore`

General EB workflow (one common approach):

1. Create an Elastic Beanstalk application + environment (Python platform).
2. Configure environment variables in EB (recommended for secrets and production flags).
3. Deploy the application code (EB will build and run it on the instances).

**ALLOWED_HOSTS**: `projectcatalogue/settings.py` currently includes an Elastic Beanstalk host in `ALLOWED_HOSTS`, along with localhost. If you deploy to a new EB environment, you may need to add its hostname/domain.

### Static & media files

- Static: `STATIC_URL = 'static/'`
- Media uploads:
  - `MEDIA_URL = 'media/'`
  - `MEDIA_ROOT = BASE_DIR / 'media/'`

In production, you may want to serve static/media via S3 + CloudFront (rather than from the instance filesystem), depending on your needs.

## CI / CodeBuild

This repo includes AWS CodeBuild build specs:

### `buildspec.yml` (Python build + migrations)
Installs Python 3.11, installs dependencies, runs pylint (non-blocking), then runs:

- `python manage.py makemigrations`
- `python manage.py migrate`

### `buildspec2.yml` (SonarCloud analysis)
Includes Java + Maven + Sonar Scanner steps to run SonarCloud analysis.

> Security note: `buildspec2.yml` appears to include a Sonar token inline. In general, tokens should be stored in AWS Secrets Manager / SSM Parameter Store and injected as environment variables in CodeBuild, not committed to the repo.

## Notes / configuration

- Default DB is SQLite (`db.sqlite3`).
- The custom user model is configured via:
  - `AUTH_USER_MODEL = 'user.User'`
