from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    last_name = models.CharField(verbose_name='Фамилия', max_length=20, blank=True)
    first_name = models.CharField(verbose_name='Имя', max_length=20, blank=True)
    middle_name = models.CharField(verbose_name='Отчество', max_length=20, blank=True)
    email = models.EmailField(verbose_name='Адрес электронной\nпочты', unique=True)

    def get_full_name(self):
        full_name = '%s %s %s' % (self.last_name, self.first_name, self.middle_name)
        return full_name.strip()