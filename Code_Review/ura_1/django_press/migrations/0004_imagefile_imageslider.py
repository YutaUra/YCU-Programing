# Generated by Django 2.1 on 2019-12-08 01:29

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('django_press', '0003_auto_20191208_0239'),
    ]

    operations = [
        migrations.CreateModel(
            name='ImageFile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('file', models.ImageField(upload_to='images')),
                ('name', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='ImageSlider',
            fields=[
                ('pagecontent_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='django_press.PageContent')),
                ('height', models.CharField(default='30%', help_text='デフォルトは30%です。', max_length=20, verbose_name='画像の高さ')),
                ('content', models.ManyToManyField(to='django_press.ImageFile', verbose_name='画像')),
            ],
            options={
                'abstract': False,
                'base_manager_name': 'objects',
            },
            bases=('django_press.pagecontent',),
        ),
    ]
