from django.shortcuts import render
from django.views.generic import TemplateView


class LoginPageView(TemplateView):
    template_name = 'accounts/login.html'
