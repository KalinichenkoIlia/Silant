from django.core.exceptions import PermissionDenied
from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import PermissionRequiredMixin, AccessMixin
from .models import Car, Complaints, TechnicalMaintenance
from .filters import CarFilter, TechnicalServiceFilter, ComplaintsFilter
from django.db.models import Q
from references.models import ServiceCompany
from rest_framework import permissions
from django.http import HttpResponse, HttpResponseForbidden
from .mixins import CustomPermissionRequiredMixin
from django.urls import reverse_lazy
from .forms import CreateCarForm, CreateTechnicalMaintenanceForm, CreateComplaints


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


class CarDetail(CustomPermissionRequiredMixin, DetailView):
    permission_required = 'service.view_car'
    model = Car
    template_name = 'car.html'
    context_object_name = 'car'


class CarCreate(PermissionRequiredMixin, CreateView):
    permission_required = 'service.add_car'
    model = Car
    form_class = CreateCarForm
    template_name = 'car_create.html'
    context_object_name = 'car_create.html'


class CarUpdate(PermissionRequiredMixin, UpdateView):
    permission_required = 'service.change_car'
    form_class = CreateCarForm
    template_name = 'car_create.html'
    model = Car


class CarDelete(PermissionRequiredMixin, DeleteView):
    permission_required = 'service.delete_car'
    model = Car
    template_name = 'car_delete.html'
    success_url = reverse_lazy('/', )


class TechnicalMaintenanceDetail(PermissionRequiredMixin, DetailView):
    permission_required = 'service.view_technical_service'
    model = TechnicalMaintenance
    template_name = 'technical_service.html'
    context_object_name = 'technical_service'


class TechnicalMaintenanceCreate(PermissionRequiredMixin, CreateView):
    permission_required = 'service.add_technical_service'
    model = TechnicalMaintenance
    form_class = CreateTechnicalMaintenanceForm
    template_name = 'technical_service_create.html'
    context_object_name = 'technical_service_create'


class TechnicalMaintenanceUpdate(PermissionRequiredMixin, UpdateView):
    permission_required = 'service.change_technical_service'
    template_name = 'create_technical_service.html'
    form_class = CreateTechnicalMaintenanceForm
    model = TechnicalMaintenance


class TechnicalMaintenanceDelete(PermissionRequiredMixin, DeleteView):
    permission_required = 'service.delete_technical_service'
    model = TechnicalMaintenance
    template_name = 'technical_service_delete.html'
    success_url = reverse_lazy('/', )


class ComplaintsDetail(PermissionRequiredMixin, DetailView):
    permission_required = 'service.view_complaints'
    model = Complaints
    template_name = 'complaints.html'
    context_object_name = 'complaints'


class ComplaintsCreate(PermissionRequiredMixin, CreateView):
    permission_required = 'service.add_complaints'
    model = Complaints
    form_class = CreateComplaints
    template_name = 'complaints_create.html'
    context_object_name = 'complaints_create'


class ComplaintsUpdate(PermissionRequiredMixin, UpdateView):
    permission_required = 'service.change_complaints'
    template_name = 'complaints_create.html'
    form_class = CreateComplaints
    model = Complaints


class ComplaintsDelete(PermissionRequiredMixin, DeleteView):
    permission_required = 'service.delete_complaints'
    model = Complaints
    template_name = 'complaints_delete.html'
    success_url = reverse_lazy('/', )

