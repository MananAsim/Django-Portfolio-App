"""Bio App configuration — registers app within the apps package."""
from django.apps import AppConfig


class BioConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'apps.bio'
    verbose_name = 'Bio & Contact'
