from django.db import models


class Lesson(models.Model):
    name = models.CharField(verbose_name = 'урок', max_length=64, unique=True)
    description = models.TextField(verbose_name='описание', blank=True)
    file_path = models.TextField(verbose_name='путь к презентации', blank=True)
