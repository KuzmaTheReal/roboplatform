from django.db import models
from django.contrib.auth.models import AbstractUser


class Teacher(AbstractUser):
    school = models.CharField(verbose_name='школа', max_length=32)

