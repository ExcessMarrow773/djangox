from django.views.generic import TemplateView
from verify_email.email_handler import send_verification_email


class HomePageView(TemplateView):
    template_name = "pages/home.html"


class AboutPageView(TemplateView):
    template_name = "pages/about.html"
