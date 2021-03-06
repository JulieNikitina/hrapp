from django.db import models
from django.contrib.auth.models import AbstractUser

from users.managers import CustomUserManager


class User(AbstractUser):
    USERNAME_FIELD = 'email'
    username = models.CharField(max_length=40, unique=False, default='')
    last_name = models.CharField(
        verbose_name='Фамилия',
        max_length=20,
        blank=True
    )
    first_name = models.CharField(
        verbose_name='Имя',
        max_length=20,
        blank=True
    )
    middle_name = models.CharField(
        verbose_name='Отчество',
        max_length=20,
        blank=True
    )
    email = models.EmailField(
        verbose_name='Адрес электронной\nпочты',
        unique=True,
    )
    REQUIRED_FIELDS = []

    objects = CustomUserManager()

    def get_full_name(self):
        full_name = '%s %s %s' % (self.last_name, self.first_name, self.middle_name)
        return full_name.strip()

    def __str__(self):
        return self.get_full_name()


