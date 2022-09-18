from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin

from .managers import CustomUserManager
from restaurants.models import Restaurant

class CustomUser(AbstractBaseUser, PermissionsMixin):

    email = models.EmailField(max_length=254, unique=True)
    name = models.CharField(max_length=254, null=True, blank=True)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    last_login = models.DateTimeField(null=True, blank=True)
    date_joined = models.DateTimeField(auto_now_add=True)

    restaurant = models.ForeignKey(Restaurant, on_delete=models.CASCADE,
                                   null=True, blank=True,
                                   related_name='employees', )

    USERNAME_FIELD = 'email'

    EMAIL_FIELD = 'email'

    objects = CustomUserManager()

    def __str__(self):
        return str(self.name)
