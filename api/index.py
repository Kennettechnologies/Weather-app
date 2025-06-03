import os
from django.core.wsgi import get_wsgi_application

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "weather_project.settings")

# This is the variable that Vercel looks for
handler = get_wsgi_application()

def lambda_handler(event, context):
    return handler(event, context) 