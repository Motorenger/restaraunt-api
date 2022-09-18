from django.contrib.auth.base_user import BaseUserManager

from django.utils import timezone


class CustomUserManager(BaseUserManager):

    def _create_user(self, email, password, is_staff, is_superuser, restaurant, **extra_fields):
        if not email:
            raise ValueError('Users must have an email address')
        now = timezone.now()
        email = self.normalize_email(email)
        user = self.model(
            email=email,
            name=email.split('@')[0],
            is_staff=is_staff,
            is_active=True,
            is_superuser=is_superuser,
            last_login=now,
            date_joined=now,
            restaurant=restaurant,
            **extra_fields
        )
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_user(self, email, password, restaurant, **extra_fields):
        return self._create_user(email, password, False, False, restaurant=None, **extra_fields)

    def create_superuser(self, email, password, **extra_fields):
        user = self._create_user(email, password, True, True, **extra_fields)
        return user