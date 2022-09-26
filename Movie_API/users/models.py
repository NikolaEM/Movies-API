from django.db import models
from django.contrib.auth.base_user import BaseUserManager
from django.contrib.auth.models import AbstractUser
from django.utils.translation import gettext_lazy as _

class CustomUserManager(BaseUserManager):
    
    def create_user(self, email, password, name):
        
        if not email:
            raise ValueError(_('The Email must be set'))
        email = self.normalize_email(email)
        user = self.model(email=email, name=name)
        user.set_password(password)
        user.save()
        return user

class CustomUser(AbstractUser):
    username = None
    first_name = None
    last_name = None
    name = models.CharField(_("name"), max_length=150, blank=False, null=False, default='user')
    password = models.CharField(_("password"), max_length=128, blank=False, null=False)
    email = models.EmailField(_('email address'), blank=False, unique=True, null=False)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    objects = CustomUserManager()

    def __str__(self):
        return self.email


