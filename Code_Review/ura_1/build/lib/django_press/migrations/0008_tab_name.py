# Generated by Django 2.1 on 2019-12-20 02:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('django_press', '0007_contactcontent_success_page'),
    ]

    operations = [
        migrations.AddField(
            model_name='tab',
            name='name',
            field=models.CharField(max_length=50, null=True),
        ),
    ]