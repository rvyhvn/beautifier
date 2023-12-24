from django.views import View
from inertia import render


class AppView(View):
    def get(self, request):
        props = {}
        return render(request, "App", props)

    def post(self, request):
        pass
