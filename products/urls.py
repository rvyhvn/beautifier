from django.urls import path

from .views import (
    ProductsCreateView,
    ProductsEditView,
    ProductsIndexView,
    ProductsShowView,
)

app_name = "products"
urlpatterns = [
    path("", ProductsIndexView.as_view(), name="products-index"),
    path("show/<int:product_id>", ProductsShowView.as_view(), name="products-show"),
    path("new/", ProductsCreateView.as_view(), name="products-create"),
    path("edit/<int:pk>", ProductsEditView.as_view(), name="products-edit"),
]
