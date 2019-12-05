from django.contrib import admin
from markdownx.admin import MarkdownxModelAdmin
from .models import Page, PageContent


class PageContentInline(admin.StackedInline):
    model = PageContent


class PageAdmin(MarkdownxModelAdmin):
    inlines = [PageContentInline, ]


admin.site.register(Page, PageAdmin)
