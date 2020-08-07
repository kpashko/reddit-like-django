import os
from django.core.wsgi import get_wsgi_application
from whitenoise.django import DjangoWhiteNoise
from dotenv import load_dotenv
from django.core.wsgi import get_wsgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'djangoProject.settings')

project_folder = os.path.expanduser('~/djangoProject')  # adjust as appropriate
load_dotenv(os.path.join(project_folder, '.env'))

application = get_wsgi_application()
application = DjangoWhiteNoise(application)
