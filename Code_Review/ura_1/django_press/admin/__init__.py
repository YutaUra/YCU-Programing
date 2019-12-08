from django.contrib import admin
from django.contrib.admin import ModelAdmin

from .context import ContextAdmin
from .page import PageAdmin
from django_press.models import Page, Context
from django_press.models.page.files import ImageFile
from django_press.models.page.service import Product

admin.site.register(Product, ModelAdmin)
admin.site.register(ImageFile, ModelAdmin)
admin.site.register(Page, PageAdmin)
admin.site.register(Context, ContextAdmin)
