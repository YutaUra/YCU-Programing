from django.contrib import admin

from django_press.models import FormField, BooleanField, TextField
from polymorphic.admin import StackedPolymorphicInline, PolymorphicInlineSupportMixin


class FormFieldInline(StackedPolymorphicInline):
    class BooleanInline(StackedPolymorphicInline.Child):
        model = BooleanField

    class TextInline(StackedPolymorphicInline.Child):
        model = TextField

    model = FormField
    child_inlines = (
        BooleanInline,
        TextInline,
    )


class FormAdmin(PolymorphicInlineSupportMixin, admin.ModelAdmin):
    inlines = [FormFieldInline, ]
