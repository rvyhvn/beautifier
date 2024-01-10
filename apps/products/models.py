from django.db import models

from core.models import AppModel


class Category(AppModel):
    name = models.CharField(
        max_length=255,
    )

    def __str__(self):
        return f"{self.id}. {self.name}"


class Product(AppModel):
    name = models.CharField(
        max_length=255,
    )
    description = models.TextField()
    price = models.IntegerField(null=True, blank=True)
    stock = models.IntegerField(null=True, blank=True)
    # image = models.ImageField(null=True, blank=True)
    category_id = models.ForeignKey(
        Category,
        null=True,
        on_delete=models.SET_NULL,
    )

    def __str__(self):
        return f"{self.id}. {self.name}"
