"""
WSGI config for weather_project project.

It exposes the WSGI callable as a module-level variable named ``app``.

For more information on this file, see
https://docs.djangoproject.com/en/5.0/howto/deployment/wsgi/
"""

import os
from django.core.wsgi import get_wsgi_application

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "weather_project.settings")

# Vercel needs this to be named 'app'
app = get_wsgi_application()

# For local development
application = app
