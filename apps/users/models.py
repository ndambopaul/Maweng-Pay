from django.db import models
from django.contrib.auth.models import AbstractUser

from apps.core.models import AbstractBaseModel
from apps.core.constants import UserRole, Gender


# Create your models here.
class User(AbstractUser, AbstractBaseModel):
    role = models.CharField(max_length=255, choices=UserRole.choices())
    phone_number = models.CharField(max_length=255)
    gender = models.CharField(max_length=255, choices=Gender.choices())

    def __str__(self):
        return self.username

    def name(self):
        return f"{self.first_name} {self.last_name}"
