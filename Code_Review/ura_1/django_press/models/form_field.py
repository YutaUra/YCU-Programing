from django.db import models
from django import forms
from polymorphic.models import PolymorphicModel

from django_press.models.forms import Form


class FormField(PolymorphicModel):
    form = models.ForeignKey(
        to=Form,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
    )
    required = models.BooleanField(
        verbose_name='必須項目でなければチェックを外してください',
        default=True,
    )
    label = models.CharField(
        verbose_name='ラベル',
        max_length=100,
        default='',
        blank=True,
    )
    label_suffix = models.CharField(
        verbose_name='ラベルの接尾辞',
        max_length=30,
        default='',
        blank=True,
    )
    initial = models.CharField(
        verbose_name='初期値',
        max_length=100,
        default='',
        blank=True,
    )

    # TODO: widget
    # ref: https://docs.djangoproject.com/en/2.2/ref/forms/fields/#widget

    help_text = models.CharField(
        verbose_name='説明',
        max_length=200,
        default='',
        blank=True,
    )

    # TODO: error_message
    # ref: https://docs.djangoproject.com/en/2.2/ref/forms/fields/#error-messages

    # TODO: validator
    # TODO: localize
    # TODO: disabled
    # TODO: validator

    def get_field(self, *args, **kwargs):
        if hasattr(self, 'field') and issubclass(self.field, forms.Field):
            field = self.field(
                required=self.required,
                label=self.label,
                label_suffix=self.label_suffix,
                initial=self.initial,
                help_text=self.help_text,
                **kwargs
            )
            return field
        else:
            raise NotImplementedError()

    def __str__(self):
        return self.label


class BooleanField(FormField):
    field = forms.BooleanField

    @property
    def get_field(self):
        return super().get_field()


class TextField(FormField):
    field = forms.CharField
    max_length = models.PositiveSmallIntegerField(
        verbose_name='最大文字数',
        default=300,
    )
    min_length = models.PositiveSmallIntegerField(
        verbose_name='最小文字数',
        default=0,
    )
    strip = models.BooleanField(
        verbose_name='前後の空白を除く',
        default=True,
    )
    empty_value = models.CharField(
        verbose_name='空を表す文字',
        max_length=30,
        default='',
        blank=True,
    )

    @property
    def get_field(self):
        return super().get_field(
            max_length=self.max_length,
            min_length=self.min_length,
            strip=self.strip,
            empty_value=self.empty_value
        )

    class Meta:
        verbose_name = 'テキスト'
