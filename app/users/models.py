from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    USERNAME_FIELD = 'username'
    # REQUIRED_FIELDS = ('email',)
