# Generated by Django 3.1.3 on 2020-11-23 00:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0002_lesson_kit'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='lesson',
            name='kit',
        ),
        migrations.AddField(
            model_name='lesson',
            name='file_path',
            field=models.TextField(blank=True, verbose_name='путь к презентации'),
        ),
    ]
