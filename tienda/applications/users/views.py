from django.shortcuts import render
from django.views.generic import TemplateView

# Create your views here.


class LoginUser(TemplateView):
    template_name = 'users/login.html'