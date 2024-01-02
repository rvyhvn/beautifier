from django.http import JsonResponse
from django.shortcuts import get_object_or_404
from inertia import render
from django.views import View

from .models import Product
from .serializers import ProductSchema


class ProductsIndexView(View):
    def get(self, request, *args, **kwargs):
        products = Product.objects.all()
        product_schema = ProductSchema(many=True)
        props = {"products": product_schema.dump(products)}
        return render(request, "Products/Index", props)

    def post(self, request):
        pass


class ProductsShowView(View):
    def get(self, request, pk, *args, **kwargs):
        product_detail = Product.objects.get(pk=pk)
        props = {"product_detail": product_detail}
        return render(request, "Products/Show", props)

    # OLD
    # def get(self, request, *args, **kwargs):
    #     product_id = kwargs.get("product_id")
    #     print(product_id)
    #     product = get_object_or_404(
    #         Product,
    #         id=product_id,
    #     )
    #     print(product)
    #     props = {
    #         "id": product.id,
    #         "product_name": product.product_name,
    #     }
    #     return render(request, "Products/Show", props)

    def post(self, request, *args, **kwargs):
        pass


class ProductsCreateView(View):
    pass


class ProductsEditView(View):
    pass
