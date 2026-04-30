
=======
# GyanUday University — College Management System

A full-stack Django project built as a 7-phase teaching project for 3rd year B.Tech students.

## Tech Stack
- Python 3.13 · Django 4.2 · Django REST Framework · Chart.js · SQLite

## Quick Start

```bash
# 1. Create and activate virtual environment
python -m venv venv
source venv/bin/activate        # Mac/Linux
venv\Scripts\activate           # Windows

# 2. Install dependencies
pip install -r requirements.txt

# 3. Run migrations
python manage.py makemigrations
python manage.py migrate

# 4. Create superuser
python manage.py createsuperuser

# 5. Start server
python manage.py runserver
```

Open http://127.0.0.1:8000

## Rebranding for a different college

```bash
python rebrand.py "Your College Name" "YCN"
```

## Deploy to Render

1. Push to GitHub
2. Go to render.com → New Web Service → connect repo
3. Render auto-detects `render.yaml`
4. Set environment variables: `SECRET_KEY`, `DEBUG=False`, `ALLOWED_HOSTS`
5. Deploy — live in ~3 minutes

## Project Structure

```
accounts/     Custom User model, login, roles
students/     Department, Student, Faculty CRUD
courses/      Course management, Enrollment
attendance/   Attendance tracking, ORM aggregation
fees/         Fee management, Payment tracking
results/      Exams, Marks, Signals, Activity Log
dashboard/    Live dashboard with Chart.js
```
