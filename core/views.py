from django.views import View
from inertia import render
from products.views import Product


class AppView(View):
    def get(self, request):
        products = Product.objects.all()
        props = {"products": products}
        return render(request, "App", props)

    def post(self, request):
        pass
