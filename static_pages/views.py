from django.views.generic.base import TemplateView
# from django.contrib.auth.decorators import login_required


class HomePageView(TemplateView):
    template_name = "static_pages/home.html"


class ProtectedView(TemplateView):
    template_name = "static_pages/protected.html"
