from django.urls import path

from .views import ProductsIndexView

app_name = "products"
urlpatterns = [
    path("", ProductsIndexView.as_view(), name="products-index"),
]
