# Apex Construction

Apex Construction Limited is a Django-based website for a construction company. The project includes:

- Services, projects, team members, testimonials, and machine hire models
- A contact page with message and consultation forms
- Dynamic templates powered by Django views and models
- Static assets for CSS and JavaScript

## Setup

1. Create and activate a Python virtual environment:
   ```powershell
   python -m venv venv
   .\venv\Scripts\Activate.ps1
   ```

2. Install dependencies:
   ```powershell
   pip install -r requirements.txt/requirements.txt
   ```

3. Apply database migrations:
   ```powershell
   $env:DJANGO_SETTINGS_MODULE='config.settings'
   .\venv\Scripts\python.exe manage.py migrate
   ```

4. Run the development server:
   ```powershell
   $env:DJANGO_SETTINGS_MODULE='config.settings'
   .\venv\Scripts\python.exe manage.py runserver
   ```

5. Open the site in your browser at `http://127.0.0.1:8000/`.

## App structure

- `apex/` - main Django app with models, views, forms, templates, and URLs
- `config/` - Django project configuration (settings, URLs, WSGI, ASGI)
- `static/` - CSS, JavaScript, and image assets
- `media/` - uploaded media files

## Notes

- The project uses Django 5.2 and Whitenoise for static file handling.
- Sample data can be loaded with Django fixtures if available.
