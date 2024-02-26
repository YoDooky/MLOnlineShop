from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    image = models.ImageField(upload_to='users_images', blank=True, null=True, verbose_name='Avatar')

    class Meta:
        verbose_name = 'user'
        verbose_name_plural = 'Users'

    def __str__(self):
        return self.username
