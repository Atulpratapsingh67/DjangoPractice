from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    random = models.CharField(verbose_name="Testing", max_length=256)