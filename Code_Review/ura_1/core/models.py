from django.db import models


class Setting(models.Model):
    key = models.CharField(max_length=500, unique=True, blank=False, null=False)
    value = models.CharField(max_length=500, blank=True, null=True)

    def __str__(self):
        return f'{self.key}: {self.value}'


def create_initial_settings(sender, **kwargs):
    Setting.objects.get_or_create(key='site_name')
