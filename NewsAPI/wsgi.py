import os

from django.core.wsgi import get_wsgi_application

from NewsAPI.settings.env import env

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "NewsAPI.settings." + env("ENVIRONMENT"))
application = get_wsgi_application()
