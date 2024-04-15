from django.forms import TextInput, Select, DateInput
from .models import Car, TechnicalMaintenance
from references import models
import django_filters


class CarFilter(django_filters.FilterSet):
    factory_number = django_filters.CharFilter(
        field_name="factory_number",
        label="Зав.номер машины",
        widget=TextInput(attrs={'class': 'form-control'}),
    )
    model_technique = django_filters.ModelChoiceFilter(
        field_name="model_technique",
        label='Модель техники',
        widget=Select(attrs={'class': 'form-select'}),
        queryset=models.ModelTechnique.objects.all()
    )
    engine_model = django_filters.ModelChoiceFilter(
        field_name='engine_model',
        label='Модель двигателя',
        widget=Select(attrs={'class': 'form-select'}),
        queryset=models.EngineModel.objects.all()
    )
    transmission_model = django_filters.ModelChoiceFilter(
        field_name='transmission_model',
        label='Модель трансмиссии',
        widget=Select(attrs={'class': 'form-select'}),
        queryset=models.TransmissionModel.objects.all()
    )
    model_drive_bridge = django_filters.ModelChoiceFilter(
        field_name='model_drive_bridge',
        label='Модель ведущего моста',
        widget=Select(attrs={'class': 'form-select'}),
        queryset=models.ModelDriveBridge.objects.all()
    )
    controlled_bridge_model = django_filters.ModelChoiceFilter(
        field_name='controlled_bridge_model',
        label='Модель управляемого моста',
        widget=Select(attrs={'class': 'form-select'}),
        queryset=models.ControlledBridgeModel.objects.all()
    )


class TechnicalServiceFilter(django_filters.FilterSet):
    factory_number = django_filters.CharFilter(
        field_name="car__factory_number",
        label="Зав.номер машины",
        widget=TextInput(attrs={'class': 'form-control'}),
    )
    type_maintenance = django_filters.ModelChoiceFilter(
        field_name='type_maintenance',
        label='Вид ТО',
        widget=Select(attrs={'class': 'form-select'}),
        queryset=models.TypeMaintenance.objects.all(),
    )
    date_event = django_filters.DateTimeFilter(
        field_name='date_event',
        label='Дата проведения ТО',
        widget=DateInput(format='%Y-%m-%d', attrs={'class': 'form-control', 'type': 'date'})
    )
    order_number = django_filters.CharFilter(
        field_name='order_number',
        label='№ заказ-наряда',
        widget=TextInput(attrs={'class': 'form-control'}),
    )
    date_order = django_filters.DateTimeFilter(
        field_name='date_order',
        label='Дата заказ-наряда',
        widget=DateInput(format='%Y-%m-%d', attrs={'class': 'form-control', 'type': 'date'})
    )
    organization_maintenance = django_filters.ModelChoiceFilter(
        field_name='organization_maintenance',
        label='Организация, проводившая ТО',
        widget=Select(attrs={'class': 'form-select'}),
        queryset=models.OrganizationMaintenance.objects.all(),
    )
    service_company = django_filters.ModelChoiceFilter(
        field_name='service_company',
        label='Сервисная компания',
        widget=Select(attrs={'class': 'form-select'}),
        queryset=models.ServiceCompany.objects.all(),
    )


class ComplaintsFilter(django_filters.FilterSet):
    car = django_filters.CharFilter(
        field_name="car__factory_number",
        label="Зав.номер машины",
        widget=TextInput(attrs={'class': 'form-control'}),
    )
    date_refusal = django_filters.DateTimeFilter(
        field_name='date_refusal',
        label='Дата отказа',
        widget=DateInput(format='%Y-%m-%d', attrs={'class': 'form-control', 'type': 'date'})
    )
    date_restoration = django_filters.DateTimeFilter(
        field_name='date_restoration',
        label='Дата восстановления',
        widget=DateInput(format='%Y-%m-%d', attrs={'class': 'form-control', 'type': 'date'})
    )
    recovery_method = django_filters.CharFilter(
        field_name='recovery_method__title',
        label='Способ восстановления',
        widget=TextInput(attrs={'class': 'form-control'}),
    )
    service_company = django_filters.ModelChoiceFilter(
        field_name='service_company',
        label='Сервисная компания',
        widget=Select(attrs={'class': 'form-select'}),
        queryset=models.ServiceCompany.objects.all(),
    )



