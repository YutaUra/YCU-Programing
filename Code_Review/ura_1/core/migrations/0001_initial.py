# Generated by Django 3.0 on 2019-12-04 08:05

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Setting',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('key', models.CharField(max_length=500, unique=True)),
                ('value', models.CharField(max_length=500)),
            ],
        ),
    ]
