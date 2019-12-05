from django.db import models
from markdownx.models import MarkdownxField


class Page(models.Model):
    title = models.CharField(max_length=100)
    in_nav = models.BooleanField(default=False)
    path = models.CharField(max_length=100, unique=True, blank=True)

    def __str__(self):
        return self.title


class PageContent(models.Model):
    page = models.OneToOneField(to=Page, on_delete=models.CASCADE)
    text = MarkdownxField('本文', help_text='Markdown形式で書いてください。')


def create_initial_pages(sender, **kwargs):
    top = Page.objects.get_or_create(title='top', path='')
    top_content = PageContent.objects.get_or_create(page=top[0])
    about = Page.objects.get_or_create(title='about', path='about')
    about_content = PageContent.objects.get_or_create(page=about[0])
