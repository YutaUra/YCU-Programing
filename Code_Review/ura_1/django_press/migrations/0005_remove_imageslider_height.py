# Generated by Django 2.1 on 2019-12-08 18:06

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('django_press', '0004_imagefile_imageslider'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='imageslider',
            name='height',
        ),
    ]