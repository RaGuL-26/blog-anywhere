# Generated by Django 5.0.4 on 2024-04-29 18:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0002_postblog_update_time_alter_postblog_slug'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='postblog',
            name='update_time',
        ),
        migrations.AlterField(
            model_name='postblog',
            name='slug',
            field=models.SlugField(),
        ),
    ]
