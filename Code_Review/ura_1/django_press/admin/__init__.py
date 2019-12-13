from django.contrib import admin
from django.contrib.admin import ModelAdmin

from .context import ContextAdmin
from .page import PageAdmin
from .form import FormAdmin
from django_press.models import Page, Context, Form
from django_press.models.page.componets.files import ImageFile
from django_press.models.page.componets.service import Product
from django_press.models.page.componets.tab import TabElement

admin.site.register(TabElement, ModelAdmin)
admin.site.register(Product, ModelAdmin)
admin.site.register(ImageFile, ModelAdmin)
admin.site.register(Page, PageAdmin)
admin.site.register(Context, ContextAdmin)
admin.site.register(Form, FormAdmin)
