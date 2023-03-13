from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):   
    is_allowed = models.BooleanField(default=True)

# Create your models here.
