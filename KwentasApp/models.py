# KwentasApp/models.py
from django.contrib.auth.models import AbstractUser
from django.db import models

class CustomUser(AbstractUser):
    department = models.CharField(max_length=255)
