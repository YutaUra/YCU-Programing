from collections import OrderedDict
from django.db import models
from django import forms


class Form(models.Model):
    name = models.CharField(
        max_length=50,
        verbose_name='フォーム名',
        blank=True,
        null=True,
    )

    def __str__(self):
        return self.name

    @property
    def form_class(self):
        class FormClass(forms.Form):
            def __init__(self, *args, **kwargs):
                super().__init__(*args, **kwargs)
                for _field in self.fields.values():
                    _field.widget.attrs.update({'field': _field})

        declared_fields = OrderedDict()
        for i, field in enumerate(self.formfield_set.all()):
            declared_fields.update({f'field_{i}': field.get_field})

        FormClass.base_fields = declared_fields
        FormClass.declared_fields = declared_fields

        return FormClass()
