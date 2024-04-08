'''from django.db import models
from django.contrib.auth.models import AbstractUser

class User(models.Model):
    name = models.CharField(max_length=255)
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=255)
    referral_code = models.CharField(max_length=255, unique=True, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
class CustomUser(AbstractUser):

    token = models.CharField(max_length=255, unique=True, null=True, blank=True)'''

from django.db import models
from django.contrib.auth.models import AbstractUser
class CustomUser(AbstractUser):

    token = models.CharField(max_length=255, unique=True, null=True, blank=True)


