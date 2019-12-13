# Generated by Django 2.1 on 2019-12-13 05:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('django_press', '0012_auto_20191209_1027'),
    ]

    operations = [
        migrations.AlterField(
            model_name='formfield',
            name='help_text',
            field=models.CharField(blank=True, default='', max_length=200, verbose_name='説明'),
        ),
        migrations.AlterField(
            model_name='formfield',
            name='initial',
            field=models.CharField(blank=True, default='', max_length=100, verbose_name='初期値'),
        ),
        migrations.AlterField(
            model_name='formfield',
            name='label',
            field=models.CharField(blank=True, default='', max_length=100, verbose_name='ラベル'),
        ),
        migrations.AlterField(
            model_name='formfield',
            name='label_suffix',
            field=models.CharField(blank=True, default='', max_length=30, verbose_name='ラベルの接尾辞'),
        ),
        migrations.AlterField(
            model_name='textfield',
            name='empty_value',
            field=models.CharField(blank=True, default='', max_length=30, verbose_name='空を表す文字'),
        ),
    ]
