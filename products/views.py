from inertia import render
from django.views import View


class ProductsIndexView(View):
    def get(self, request):
        props = {}
        return render(request, "Products/Index", props)

    def post(self, request):
        pass
