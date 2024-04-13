from django.shortcuts import render
from django.views.generic import ListView, View
from .models import Car, Complaints, TechnicalMaintenance
from .filters import CarFilter


def home_page(request):
    filter_car = CarFilter(request.GET, queryset=Car.objects.all())
    return render(request, 'home.html', {'filter_car': filter_car})




