# Generated by Django 2.1 on 2019-12-08 23:25

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('django_press', '0007_auto_20191209_0730'),
    ]

    operations = [
        migrations.AddField(
            model_name='page',
            name='parent_page',
            field=models.ForeignKey(blank=True, help_text='パンくずリストの作成、SEO対策となります。', null=True, on_delete=django.db.models.deletion.SET_NULL, to='django_press.Page', verbose_name='このページに親となるページ'),
        ),
    ]
