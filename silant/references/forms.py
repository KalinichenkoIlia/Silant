from django.forms import ModelForm, CharField, Select, ModelChoiceField, TextInput, Textarea

import references.models as model
from accounts.models import Profile


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
        model = model.ModelTechnique
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
        model = model.EngineModel
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
        model = model.TransmissionModel
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
        model = model.ModelDriveBridge
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
        model = model.ControlledBridgeModel
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
        model = model.TypeMaintenance
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
        model = model.FailureNode
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
        model = model.RecoveryMethod
        fields = [
            'title', 'description'
        ]


class CreateServiceCompany(ModelForm):
    profile = ModelChoiceField(
        label='Профиль сервисной компании',
        queryset=Profile.objects.filter(position='SC'),
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
        model = model.ServiceCompany
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
        model = model.OrganizationMaintenance
        fields = [
            'title', 'description'
        ]
