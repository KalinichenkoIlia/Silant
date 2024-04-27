from django.contrib.auth.mixins import PermissionRequiredMixin
from django.db.models import Q
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView

from .filters import CarFilter, TechnicalServiceFilter, ComplaintsFilter
from .forms import CreateCarForm, CreateTechnicalMaintenanceForm, CreateComplaints
from .helper import check_data
from .mixins import CustomPermissionRequiredMixin
from .models import Car, Complaints, TechnicalMaintenance


class HomePage(ListView):
    template_name = 'home.html'

    def get_queryset(self):

        if self.request.user.is_authenticated:

            """
                   фильтрация и получение объектов моделей по связям
                   пользователя с моделью
            """

            self.technical_service = TechnicalMaintenance.objects.filter(Q(
                car__client__user=self.request.user.id) | Q(
                service_company__profile__user=self.request.user.id))

            self.car = Car.objects.filter(Q(
                client__user=self.request.user.id) | Q(
                service_company__profile__user=self.request.user.id))

            self.complaints = Complaints.objects.filter(Q(
                car__client__user=self.request.user.id) | Q(
                service_company__profile__user=self.request.user.id))

            if self.request.user.is_staff or self.request.user.profile.position == 'MG':
                """
                    только для менеджера или администратора 
                    объекты модели будут все 

                """
                self.car = Car.objects.all()
                self.technical_service = TechnicalMaintenance.objects.all()
                self.complaints = Complaints.objects.all()

            ######################################################################

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
                queryset=self.complaints,
                prefix='complaints'
            )

            return self.filter_car.qs, self.filter_technical_service.qs, self.filter_complaints.qs

        else:
            self.filter_car = CarFilter(  # фильтр для неавторизованных
                self.request.GET,
                queryset=Car.objects.all(),
                prefix='car')
            return self.filter_car.qs

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        if self.request.user.is_authenticated:  # сонтекст доступный только для авторизованных
            context['filter_technical_service'] = self.filter_technical_service
            context['filter_complaints'] = self.filter_complaints
        context['filter_car'] = self.filter_car

        context['not_found_car'] = not self.filter_car.qs and not check_data(self.filter_car.data, 'car-factory_number')
        context['not_found_service'] = not self.filter_car.qs and not check_data(self.filter_car.data,
                                                                                 'car-factory_number')
        context['not_found_complaints'] = not self.filter_car.qs and not check_data(self.filter_car.data,
                                                                                    'complaints-car')

        return context


class CarDetail(CustomPermissionRequiredMixin, DetailView):
    permission_required = 'service.view_car'
    model = Car
    template_name = 'service/car/car.html'
    context_object_name = 'car'


class CarCreate(PermissionRequiredMixin, CreateView):
    permission_required = 'service.add_car'
    model = Car
    form_class = CreateCarForm
    template_name = 'service/car/car_create.html'
    context_object_name = 'car_create'


class CarUpdate(PermissionRequiredMixin, UpdateView):
    permission_required = 'service.change_car'
    form_class = CreateCarForm
    template_name = 'service/car/car_create.html'
    model = Car


class CarDelete(PermissionRequiredMixin, DeleteView):
    permission_required = 'service.delete_car'
    model = Car
    template_name = 'service/car/car_delete.html'
    success_url = reverse_lazy('/', )


class TechnicalMaintenanceDetail(CustomPermissionRequiredMixin, DetailView):
    permission_required = 'service.view_technical_service'
    model = TechnicalMaintenance
    template_name = 'service/technical_service/technical_service.html'
    context_object_name = 'technical_service'


class TechnicalMaintenanceCreate(PermissionRequiredMixin, CreateView):
    permission_required = 'service.add_technicalmaintenance'
    model = TechnicalMaintenance
    form_class = CreateTechnicalMaintenanceForm
    template_name = 'service/technical_service/technical_service_create.html'
    context_object_name = 'technical_create'

    def get_form_kwargs(self):
        # передача текущего пользователя в форму
        kwargs = super().get_form_kwargs()
        kwargs.update({'user': self.request.user})
        return kwargs

    def form_valid(self, form):
        return super().form_valid(form)


class TechnicalMaintenanceUpdate(CustomPermissionRequiredMixin, UpdateView):
    permission_required = 'service.change_technicalMaintenance'
    template_name = 'service/technical_service/technical_service_create.html'
    form_class = CreateTechnicalMaintenanceForm
    model = TechnicalMaintenance

    def get_form_kwargs(self):
        # передача текущего пользователя в форму
        kwargs = super().get_form_kwargs()
        kwargs.update({'user': self.request.user})
        return kwargs


class TechnicalMaintenanceDelete(PermissionRequiredMixin, DeleteView):
    permission_required = 'service.delete_technicalMaintenance'
    model = TechnicalMaintenance
    template_name = 'service/technical_service/technical_service_delete.html'
    success_url = reverse_lazy('/', )


class ComplaintsDetail(CustomPermissionRequiredMixin, DetailView):
    permission_required = 'service.view_complaints'
    model = Complaints
    template_name = 'service/complaints/complaints.html'
    context_object_name = 'complaints'


class ComplaintsCreate(PermissionRequiredMixin, CreateView):
    permission_required = 'service.add_complaints'
    model = Complaints
    form_class = CreateComplaints
    template_name = 'service/complaints/complaints_create.html'
    context_object_name = 'complaints_create'

    def get_form_kwargs(self):
        # передача текущего пользователя в форму
        kwargs = super().get_form_kwargs()
        kwargs.update({'user': self.request.user})
        return kwargs


class ComplaintsUpdate(CustomPermissionRequiredMixin, UpdateView):
    permission_required = 'service.change_complaints'
    template_name = 'service/complaints/complaints_create.html'
    form_class = CreateComplaints
    model = Complaints

    def get_form_kwargs(self):
        # передача текущего пользователя в форму
        kwargs = super().get_form_kwargs()
        kwargs.update({'user': self.request.user})
        return kwargs


class ComplaintsDelete(PermissionRequiredMixin, DeleteView):
    permission_required = 'service.delete_complaints'
    model = Complaints
    template_name = 'service/complaints/complaints_delete.html'
    success_url = reverse_lazy('/', )
