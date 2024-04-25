from django.forms import ModelForm, CharField, Select, ModelChoiceField, TextInput, \
    DateField, DateInput, IntegerField, NumberInput, Textarea
from accounts.models import Profile
from .models import ModelTechnique, EngineModel, TransmissionModel, ModelDriveBridge, \
    ControlledBridgeModel, TypeMaintenance, FailureNode, RecoveryMethod, \
    ServiceCompany, OrganizationMaintenance


class CreateModelTechnique(ModelForm):
    title = CharField(
        label='Название',
        min_length=3,
        max_length=128,
        widget=TextInput(
            attrs={'class': 'form-control'})
    )
    description = CharField(
        label='Описание',
        widget=Textarea(
            attrs={'class': 'form-control'})
    )

    class Meta:
        model = ModelTechnique
        fields = [
            'title', 'description'
        ]


class CreateEngineModel(ModelForm):
    title = CharField(
        label='Название',
        min_length=3,
        max_length=128,
        widget=TextInput(
            attrs={'class': 'form-control'})
    )
    description = CharField(
        label='Описание',
        widget=Textarea(
            attrs={'class': 'form-control'})
    )

    class Meta:
        model = EngineModel
        fields = [
            'title', 'description'
        ]


class CreateTransmissionModel(ModelForm):
    title = CharField(
        label='Название',
        min_length=3,
        max_length=128,
        widget=TextInput(
            attrs={'class': 'form-control'})
    )
    description = CharField(
        label='Описание',
        widget=Textarea(
            attrs={'class': 'form-control'})
    )

    class Meta:
        model = TransmissionModel
        fields = [
            'title', 'description'
        ]


class CreateModelDriveBridge(ModelForm):
    title = CharField(
        label='Название',
        min_length=3,
        max_length=128,
        widget=TextInput(
            attrs={'class': 'form-control'})
    )
    description = CharField(
        label='Описание',
        widget=Textarea(
            attrs={'class': 'form-control'})
    )

    class Meta:
        model = ModelDriveBridge
        fields = [
            'title', 'description'
        ]


class CreateControlledBridgeModel(ModelForm):
    title = CharField(
        label='Название',
        min_length=3,
        max_length=128,
        widget=TextInput(
            attrs={'class': 'form-control'})
    )
    description = CharField(
        label='Описание',
        widget=Textarea(
            attrs={'class': 'form-control'})
    )

    class Meta:
        model = ControlledBridgeModel
        fields = [
            'title', 'description'
        ]


class CreateTypeMaintenance(ModelForm):
    title = CharField(
        label='Название',
        min_length=3,
        max_length=128,
        widget=TextInput(
            attrs={'class': 'form-control'})
    )
    description = CharField(
        label='Описание',
        widget=Textarea(
            attrs={'class': 'form-control'})
    )

    class Meta:
        model = TypeMaintenance
        fields = [
            'title', 'description'
        ]


class CreateFailureNode(ModelForm):
    title = CharField(
        label='Название',
        min_length=3,
        max_length=128,
        widget=TextInput(
            attrs={'class': 'form-control'})
    )
    description = CharField(
        label='Описание',
        widget=Textarea(
            attrs={'class': 'form-control'})
    )

    class Meta:
        model = FailureNode
        fields = [
            'title', 'description'
        ]


class CreateRecoveryMethod(ModelForm):

    title = CharField(
        label='Название',
        min_length=3,
        max_length=128,
        widget=TextInput(
            attrs={'class': 'form-control'})
    )
    description = CharField(
        label='Описание',
        widget=Textarea(
            attrs={'class': 'form-control'})
    )

    class Meta:
        model = RecoveryMethod
        fields = [
            'title', 'description'
        ]


class CreateServiceCompany(ModelForm):
    profile = ModelChoiceField(
        label='Профиль сервисной компании',
        queryset=Profile.objects.all(),
        widget=Select(
            attrs={'class': 'form-control'})
    )
    title = CharField(
        label='Название',
        min_length=3,
        max_length=128,
        widget=TextInput(
            attrs={'class': 'form-control'})
    )
    description = CharField(
        label='Описание',
        widget=Textarea(
            attrs={'class': 'form-control'})
    )

    class Meta:
        model = ServiceCompany
        fields = [
            'title', 'description'
        ]


class CreateOrganizationMaintenance(ModelForm):
    title = CharField(
        label='Название',
        min_length=3,
        max_length=128,
        widget=TextInput(
            attrs={'class': 'form-control'})
    )
    description = CharField(
        label='Описание',
        widget=Textarea(
            attrs={'class': 'form-control'})
    )

    class Meta:
        model = OrganizationMaintenance
        fields = [
            'title', 'description'
        ]

