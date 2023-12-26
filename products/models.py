from django.db import models


class AppModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class Category(AppModel):
    category_name = models.CharField(max_length=255)

    def __str__(self):
        return f"{self.id}. {self.category_name}"


class Product(AppModel):
    product_name = models.CharField(max_length=255)
    product_description = models.TextField()
    product_price = models.IntegerField()
    product_stock = models.IntegerField()
    product_image = models.ImageField()
    category_id = models.ForeignKey(Category, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.id}. {self.product_name}"
