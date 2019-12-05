from django.apps import AppConfig
from django.db.models.signals import post_migrate


class SitePageConfig(AppConfig):
    name = 'site_page'

    def ready(self):
        from .models import create_initial_pages
        post_migrate.connect(create_initial_pages, self)
