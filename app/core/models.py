"""
Database models.
"""
from django.db import models
from phonenumber_field.modelfields import PhoneNumberField
from django.contrib.auth.models import (
    AbstractBaseUser,
    BaseUserManager,
    PermissionsMixin,
)


class UserManager(BaseUserManager):
    """Manager for users."""

    def create_user(self, email, password=None, **extra_fields):
        """Create, Save and Return new user"""
        if not email:
            raise ValueError('User must have an email address.')
        user = self.model(email=self.normalize_email(email), **extra_fields)
        user.set_password(password)
        user.save(using=self._db)

        return user

    def create_superuser(self, email, password):
        """Create and Return a new superuser."""
        user = self.create_user(email, password)
        user.is_staff = True
        user.is_superuser = True
        user.save(using=self._db)

        return user


class User(AbstractBaseUser, PermissionsMixin):
    """User in the system"""
    email = models.EmailField(max_length=255, unique=True)
    first_name = models.CharField(max_length=255)
    middle_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    extension_name = models.CharField(max_length=5)
    contact = PhoneNumberField(blank=True, max_length=15, region="PH", help_text='Enter a valid phone number (e.g. 09123456789 or +639123456789).', error_messages={"required": "Please enter a valid phone number (e.g. 09123456789 or +639123456789)."})
    is_active = models.BooleanField(default=True, help_text='Designates whether this user should be treated as active. Unselect this instead of deleting accounts.')
    is_staff = models.BooleanField(default=False, help_text='Designates whether the user can log into this admin site.')

    objects = UserManager()

    USERNAME_FIELD = 'email'
