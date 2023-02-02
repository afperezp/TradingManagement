from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils.translation import gettext as _
from django.contrib.auth import get_user_model

# Create your models here.
from .manager import CustomUserManager


class CustomUser(AbstractUser):
    email = models.EmailField(_('email address'), unique=True)
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ('username',)

    objects = CustomUserManager()

    def __str__(self):
        return self.email


User = get_user_model()

"""
Trader

"""
class Trader(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE,primary_key=True, related_name="user_trader")
    country = models.CharField(max_length=50)
    date_joined = models.DateTimeField(auto_now=True)
    date_updated = models.DateTimeField(auto_now_add=True)

    
    class Meta:
        ordering = ["-date_joined"]
    def __str__(self):
        return self.user.email

"""

Clientes: 

"""


class Clients(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE,primary_key=True, related_name="user_client")
    trader = models.ForeignKey(Trader, on_delete=models.CASCADE, related_name="trader_client")
    address = models.CharField(max_length=50)
    country = models.CharField(max_length=50)
    date_joined = models.DateTimeField(auto_now=True)
    date_updated = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ["-date_joined"]
    def __str__(self):
        return self.user.email



