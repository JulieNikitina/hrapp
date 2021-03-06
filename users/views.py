from django.shortcuts import render
from django.contrib.auth.views import LogoutView, SuccessURLAllowedHostsMixin
from django.views.generic import TemplateView

from django.urls import reverse_lazy
from django.views.generic import CreateView

from django.contrib.auth import logout


def logout_view(request):
    logout(request)
