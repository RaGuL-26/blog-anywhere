# Generated by Django 5.0.4 on 2024-04-29 18:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0003_remove_postblog_update_time_alter_postblog_slug'),
    ]

    operations = [
        migrations.AddField(
            model_name='postblog',
            name='update_time',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AlterField(
            model_name='postblog',
            name='slug',
            field=models.SlugField(unique=True),
        ),
    ]
