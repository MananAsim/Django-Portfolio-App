import os
from django.core.wsgi import get_wsgi_application

# Specify the Django settings module
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'portfolio_project.settings')

# Get the WSGI application
app = get_wsgi_application()
