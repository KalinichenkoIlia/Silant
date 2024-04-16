from django.shortcuts import render
from django.views.generic import ListView, DetailView, View
from django.contrib.auth.mixins import PermissionRequiredMixin
from .models import Car, Complaints, TechnicalMaintenance
from .filters import CarFilter, TechnicalServiceFilter, ComplaintsFilter
from django.db.models import Q
from references.models import ServiceCompany


class HomePage(ListView):
    template_name = 'home.html'

    def get_queryset(self):

        self.technical_service = TechnicalMaintenance.objects.filter(Q(
            car__client__user=self.request.user.id) | Q(
            service_company__profile__user=self.request.user.id))

        self.car = Car.objects.filter(Q(
            client__user=self.request.user.id) | Q(
            service_company__profile__user=self.request.user.id))

        self.complaints = Complaints.objects.filter(Q(
            car__client__user=self.request.user.id) | Q(
            service_company__profile__user=self.request.user.id))

        if self.request.user.is_authenticated:
            if self.request.user.is_staff:

                self.car = Car.objects.all()
                self.technical_service = TechnicalMaintenance.objects.all()
                self.complaints = Complaints.objects.all()

            self.filter_car = CarFilter(
                self.request.GET,
                queryset=self.car,
                prefix='car')

            self.filter_technical_service = TechnicalServiceFilter(
                self.request.GET,
                queryset=self.technical_service,
                prefix='service')

            self.filter_complaints = ComplaintsFilter(
                self.request.GET,
                queryset=self.complaints)
            return self.filter_car.qs, self.filter_technical_service.qs, self.filter_complaints.qs

        else:
            self.filter_car = CarFilter(
                self.request.GET,
                queryset=Car.objects.all(),
                prefix='car')
            return self.filter_car.qs

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        if self.request.user.is_authenticated:
            context['filter_technical_service'] = self.filter_technical_service
            context['filter_complaints'] = self.filter_complaints

        context['filter_car'] = self.filter_car
        return context


class CarDetail(PermissionRequiredMixin, DetailView):
    permission_required = 'service.view_car'
    model = Car
    template_name = 'car.html'
    context_object_name = 'car'

    def has_permission(self):
        car_id = self.request.GET
        user = self.request.user.id
        print(car_id)

        if not self.request.user.is_staff or user == Car.objects.filter(car=car_id).order_by('user_id'):
            return True





