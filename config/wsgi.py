import os
from django.core.wsgi import get_wsgi_application
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings')

# Ensure database migrations are applied on startup for deployed environments.
try:
    from django.core.management import call_command
    call_command('migrate', interactive=False)
except Exception:
    # If migration fails during startup, continue to allow the app to start and
    # handle database errors gracefully in views.
    pass

application = get_wsgi_application()