from django.contrib.auth.models import AbstractUser
from django.db import models

# Create your models here.
class CustomUser(AbstractUser):
    profile_picture = models.ImageField(upload_to='user_profiles/', null=True, blank=True)
    is_musician = models.BooleanField(default=False)

    def __str__(self):
        return self.username