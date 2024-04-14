from django.shortcuts import render
from django.views.generic import ListView, View
from .models import Car, Complaints, TechnicalMaintenance
from .filters import CarFilter, TechnicalServiceFilter


def home_page(request):
    filter_car = CarFilter(request.GET, queryset=Car.objects.all(), prefix='form_car')
    filter_technical_service = TechnicalServiceFilter(request.GET, queryset=TechnicalMaintenance.objects.all(), prefix='form_service')
    return render(request, 'home.html', {'filter_car': filter_car, 'filter_technical': filter_technical_service})




