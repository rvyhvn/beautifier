from django.views import View
from inertia import render
from apps.products.models import Product


class AppView(View):
    def get(self, request):
        products = Product.objects.all()
        props = {"title": "Halaman Utama"}
        return render(request, "App", props)

    def post(self, request):
        pass
