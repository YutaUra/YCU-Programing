from django.db import models
from markdownx.models import MarkdownxField
from polymorphic.models import PolymorphicModel

from django_press.models.page.files import ImageFile
from django_press.models.page.page import Page


class PageContent(PolymorphicModel):
    page = models.ForeignKey(to=Page, on_delete=models.CASCADE, related_name='contents')
    priority = models.PositiveSmallIntegerField(
        verbose_name='ページ内の表示順(昇順)',
        default=1,
        help_text='同じページ内では数値の重複を避けてください。\n'
                  '0~32767の整数値で入力してください。\n'
                  '小さい数字ほど上に来ます'
    )

    class Meta:
        ordering = ('priority',)


class PageText(PageContent):
    content = MarkdownxField(
        verbose_name='本文',
        help_text='Markdown、HTMLでの記述が可能です。ドラッグアンドドロップで画像の配置もできます。'
    )


class ImageSlider(PageContent):
    content = models.ManyToManyField(
        to=ImageFile,
        verbose_name='画像',
    )
    height = models.CharField(
        verbose_name='画像の高さ',
        help_text='デフォルトは30%です。',
        default='30%',
    )
