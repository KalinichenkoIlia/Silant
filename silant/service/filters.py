from django.forms import TextInput, Select
from .models import Car
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
