from django.apps import AppConfig
from django.db.models.signals import post_migrate


class CoreConfig(AppConfig):
    name = 'core'

    def ready(self):
        from .models import create_initial_settings
        post_migrate.connect(create_initial_settings, sender=self)
