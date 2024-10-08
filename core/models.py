import uuid

from django.contrib.auth.models import AbstractUser
from django.db import models

# Create your models here.
class User(AbstractUser):
    first_name = models.CharField(max_length=50, blank=True)
    last_name = models.CharField(max_length=50, blank=True)
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=225, blank=True)
    username = None
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []


class UserToken(models.Model):
    user_id = models.IntegerField(unique=True)
    refresh_token = models.CharField(max_length=225)
    created_at = models.DateTimeField(auto_now_add=True)
    expires_at = models.DateTimeField()
