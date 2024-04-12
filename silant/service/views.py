from django.shortcuts import render
from django.views.generic import ListView
from .models import Car, Complaints, TechnicalMaintenance


class HomePageView(ListView):
    template_name = 'home.html'
    raise_exception = True
