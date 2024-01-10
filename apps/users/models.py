from django.db import models
from django.contrib.auth.models import User


class UserProfile(models.Model):
    user = models.OneToOneField(to=User, on_delete=models.CASCADE)
    shipping_address = models.CharField(
        max_length=255,
        blank=False,
        null=False,
    )
