# Generated by Django 2.1 on 2020-01-08 07:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('django_press', '0008_tab_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='page',
            name='publish',
            field=models.BooleanField(default=True, verbose_name='公開設定'),
        ),
    ]
