# Generated by Django 2.1 on 2019-12-19 19:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('django_press', '0004_auto_20191220_0400'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contactcontent',
            name='form',
            field=models.CharField(choices=[('Contact', 'django_press.models.Inquiry.contact')], max_length=100),
        ),
    ]
