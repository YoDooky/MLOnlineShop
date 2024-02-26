from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    image = models.ImageField(upload_to='users_images', default=None, blank=True, null=True)

    class Meta:
        verbose_name = 'user'
        verbose_name_plural = 'Users'

    def __str__(self):
        return self.username
