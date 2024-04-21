from django.forms import ModelForm, CharField, Select, Textarea, ModelChoiceField, TextInput,\
    ChoiceField, DateField, DateInput, IntegerField
from references import models
from accounts.models import Profile
from .models import Car, TechnicalMaintenance, Complaints


class CreateCarForm(ModelForm):
    factory_number = CharField(
        label='Заводской номер',
        widget=TextInput(
            attrs={'class': 'form-control'})
    )
    model_technique = ModelChoiceField(
        queryset=models.ModelTechnique.objects.all(),
        label='Модель техники',
        widget=Select(
            attrs={'class': 'form-control'}
        ))
    engine_model = ModelChoiceField(
        queryset=models.EngineModel.objects.all(),
        label='Модель двигателя',
        widget=Select(
            attrs={'class': 'form-control'}
        ))
    engine_serial_number = CharField(
        label='Зав. № двигателя',
        min_length=3,
        max_length=128,
        widget=TextInput(
            attrs={'class': 'form-control'})
    )
    transmission_model = ModelChoiceField(
        queryset=models.TransmissionModel.objects.all(),
        label='Модель трансмиссии',
        widget=Select(
            attrs={'class': 'form-control'}
        ))
    transmission_serial_numbers = CharField(
        label='Зав. № трансмиссии',
        min_length=3,
        max_length=128,
        widget=TextInput(
            attrs={'class': 'form-control'})
    )
    model_drive_bridge = ModelChoiceField(
        queryset=models.ModelDriveBridge.objects.all(),
        label='Модель ведущего моста',
        widget=Select(
            attrs={'class': 'form-control'})
    )
    factory_number_drive_bridge = CharField(
        label='Зав. № ведущего моста',
        min_length=3,
        max_length=128,
        widget=TextInput(
            attrs={'class': 'form-control'})
    )
    controlled_bridge_model = ModelChoiceField(
        queryset=models.ControlledBridgeModel.objects.all(),
        label='Модель управляемого моста',
        widget=Select(
            attrs={'class': 'form-control'}
    ))
    factory_number_controlled_bridge = CharField(
        label='Зав. № управляемого моста',
        min_length=3,
        max_length=128,
        widget=TextInput(
            attrs={'class': 'form-control'})
    )
    delivery_agreement = CharField(
        label='Договор поставки №, дата',
        widget=TextInput(
            attrs={'class': 'form-control'})
    )
    factory_shipment_date = DateField(
        label='Дата отгрузки с завода',
        widget=DateInput(
            attrs={'class': 'form-control'})
    )
    consignee = CharField(
        label='Грузополучатель',
        widget=TextInput(
            attrs={'class': 'form-control'})
    )
    delivery_address = CharField(
        label='Адрес поставки',
        widget=TextInput(
            attrs={'class': 'form-control'})
    )
    equipment = CharField(
        label='Комплектация (доп. опции)',
        widget=TextInput(
            attrs={'class': 'form-control'})
    )
    client = ModelChoiceField(
        label='Клиент',
        queryset=Profile.objects.all(),
        widget=Select(
            attrs={'class': 'form-control'})
    )
    service_company = ModelChoiceField(
        label='Сервисная компания',
        queryset=models.ServiceCompany.objects.all(),
        widget=Select(
            attrs={'class': 'form-control'})
    )

    class Meta:
        model = Car
        fields = ['factory_number', 'model_technique', 'engine_model', 'engine_serial_number',
                  'transmission_model', 'transmission_serial_numbers', 'model_drive_bridge',
                  'factory_number_drive_bridge', 'controlled_bridge_model', 'factory_number_controlled_bridge',
                  'delivery_agreement', 'factory_shipment_date', 'consignee', 'delivery_address',
                  'equipment', 'client', 'service_company'
                  ]


class CreateTechnicalMaintenanceForm(ModelForm):

    def __init__(self, *args, **kwargs):

        self.user = kwargs.pop('user', None)
        super().__init__(*args, **kwargs)

        if not self.user.profile.position == 'MG' and not self.user.is_staff:
            service_company = self.fields['service_company']
            car = self.fields['car']
            car.disabled = True
            service_company.disabled = True

    type_maintenance = ModelChoiceField(
        queryset=models.TypeMaintenance.objects.all(),
        label='Вид ТО',
        widget=Select(
            attrs={'class': 'form-control'})
    )
    date_event = DateField(
        label='Дата проведения ТО',
        widget=DateInput(
            attrs={'class': 'form-control'})
    )
    operating_time = IntegerField(
        label='Наработка, м/час',
    )
    order_number = CharField(
        max_length=128,
        min_length=1,
        label='№ заказ-наряда'
    )
    date_order = DateField(
        label='Дата заказ-наряда',
        widget=DateInput(
            attrs={'class': 'form-control'})
    )
    organization_maintenance = ModelChoiceField(
        queryset=models.OrganizationMaintenance.objects.all(),
        label='Организация, проводившая ТО',
        widget=Select(
            attrs={'class': 'form-control'})

    )
    car = ModelChoiceField(
        queryset=Car.objects.all(),
        label='Машина',
        widget=Select(
            attrs={'class': 'form-control'})
    )
    service_company = ModelChoiceField(
        queryset=models.ServiceCompany.objects.all(),
        label='Сервисная компания',
        widget=Select(
            attrs={'class': 'form-control'})
    )

    class Meta:
        model = TechnicalMaintenance
        fields = [
            'type_maintenance', 'date_event', 'operating_time', 'order_number', 'date_order',
            'organization_maintenance', 'car', 'service_company'
        ]


class CreateComplaints(ModelForm):
    class Meta:
        model = Complaints
        fields = [
            'date_refusal', 'operating_time', 'failure_node', 'description_failure',
            'recovery_method', 'list_spare_parts', 'date_restoration', 'car', 'service_company'
        ]
