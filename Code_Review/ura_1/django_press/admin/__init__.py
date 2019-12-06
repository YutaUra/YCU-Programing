from django.contrib import admin
from .context import ContextAdmin
from .page import PageAdmin
from django_press.models import Page, Context

admin.site.register(Page, PageAdmin)
admin.site.register(Context, ContextAdmin)
