from django.shortcuts import render
from django.views.generic import ListView, View
from django.db.models import Exists, OuterRef
from accounts.models import Profile
from .models import Car, Complaints, TechnicalMaintenance
from .filters import CarFilter, TechnicalServiceFilter, ComplaintsFilter
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import PermissionRequiredMixin


class HomePage(ListView):
    template_name = 'home.html'
    model = Car


    def get_queryset(self):

        queryset = super().get_queryset()
        if self.request.method == 'GET':

            self.filter_car = CarFilter(
                self.request.GET,
                queryset=queryset.filter(client__user=self.request.user),
                prefix='car')

        self.filter_technical_service = TechnicalServiceFilter(
            self.request.GET,
            queryset=TechnicalMaintenance.objects.all(),
            prefix='service')

        self.filter_complaints = ComplaintsFilter(
            self.request.GET,
            queryset=Complaints.objects.all(),
            prefix='complaints')

        return self.filter_car.qs, self.filter_technical_service.qs, self.filter_complaints.qs

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        context['filter_car'] = self.filter_car
        context['filter_technical_service'] = self.filter_technical_service
        context['filter_complaints'] = self.filter_complaints

        return context
