from django.db import models

from products.models import AppModel


class User(AppModel):
    user_username = models.CharField(max_length=50)
    user_email = models.EmailField()
    user_password = models.CharField()
    user_shipping_address = (
        models.CharField()
    )  # TODO: search the compatible field for shipping addresses.

    def __str__(self):
        return f"{self.id}. {self.user_username} | {self.user_email}"
