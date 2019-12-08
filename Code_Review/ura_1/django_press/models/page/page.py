from django.db import models


class Page(models.Model):
    title = models.CharField(max_length=100)
    in_nav = models.BooleanField(default=False)
    path = models.CharField(max_length=100, unique=True, blank=True)

    class Meta:
        verbose_name = 'Webページ'
        verbose_name_plural = 'Webページ'

    def __str__(self):
        return self.title

    def save(self, force_insert=False, force_update=False, using=None,
             update_fields=None):
        if self.path is None:
            self.path = self.title
        super().save(force_insert, force_update, using, update_fields)

    @property
    def url(self):
        return '/' + self.path
