from django.contrib.auth.mixins import PermissionRequiredMixin
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView

import references.forms as form
from .models import ModelTechnique, EngineModel, TransmissionModel, ModelDriveBridge, \
    ControlledBridgeModel, TypeMaintenance, FailureNode, RecoveryMethod, \
    ServiceCompany, OrganizationMaintenance


class ReferencesList(ListView):
    template_name = 'references.html'


class ModelTechniqueList(PermissionRequiredMixin, ListView):
    model = ModelTechnique
    template_name = 'references/model_technique/model_technique_list.html'
    context_object_name = 'model_technique_list'


class ModelTechniqueCreate(PermissionRequiredMixin, CreateView):
    model = ModelTechnique
    form_class = form.CreateModelTechnique
    template_name = 'references/model_technique/model_technique_create.html'
    context_object_name = 'model_technique_create'


class ModelTechniqueUpdate(PermissionRequiredMixin, UpdateView):
    form_class = form.CreateModelTechnique
    template_name = 'references/model_technique/model_technique_create.html'
    model = ModelTechnique


class ModelTechniqueDelete(PermissionRequiredMixin, DeleteView):
    model = ModelTechnique
    template_name = 'references/model_technique/model_technique_delete.html'
    success_url = reverse_lazy('/', )


class EngineModelList(PermissionRequiredMixin, ListView):
    model = EngineModel
    template_name = 'references/engine_model/engine_model_list.html'
    context_object_name = 'engine_model_list'


class EngineModelCreate(PermissionRequiredMixin, CreateView):
    model = EngineModel
    form_class = form.CreateEngineModel
    template_name = 'references/engine_model/engine_model_create.html'
    context_object_name = 'engine_model_create'


class EngineModelUpdate(PermissionRequiredMixin, UpdateView):
    form_class = form.CreateEngineModel
    template_name = 'references/engine_model/engine_model_create.html'
    model = EngineModel


class EngineModelDelete(PermissionRequiredMixin, DeleteView):
    model = EngineModel
    template_name = 'references/engine_model/engine_model_delete.html'
    success_url = reverse_lazy('/', )


class TransmissionModelList(PermissionRequiredMixin, ListView):
    model = TransmissionModel
    template_name = 'references/transmission_model/transmission_model_list.html'
    context_object_name = 'transmission_model_list'


class TransmissionModelCreate(PermissionRequiredMixin, CreateView):
    model = TransmissionModel
    form_class = form.CreateTransmissionModel
    template_name = 'references/transmission_model/transmission_model_create.html'
    context_object_name = 'transmission_model_create'


class TransmissionModelUpdate(PermissionRequiredMixin, UpdateView):
    form_class = form.CreateTransmissionModel
    template_name = 'references/transmission_model/transmission_model_create.html'
    model = TransmissionModel


class TransmissionModelDelete(PermissionRequiredMixin, DeleteView):
    model = TransmissionModel
    template_name = 'references/transmission_model/transmission_model_delete.html'
    success_url = reverse_lazy('/', )


class ModelDriveBridgeList(PermissionRequiredMixin, ListView):
    model = ModelDriveBridge
    template_name = 'references/model_drive_bridge/model_drive_bridge_list.html'
    context_object_name = 'model_drive_bridge_list'


class ModelDriveBridgeCreate(PermissionRequiredMixin, CreateView):
    model = ModelDriveBridge
    form_class = form.CreateModelDriveBridge
    template_name = 'references/model_drive_bridge/model_drive_bridge_create.html'
    context_object_name = 'model_drive_bridge_create'


class ModelDriveBridgeUpdate(PermissionRequiredMixin, UpdateView):
    form_class = form.CreateModelDriveBridge
    template_name = 'references/model_drive_bridge/model_drive_bridge_create.html'
    model = ModelDriveBridge


class ModelDriveBridgeDelete(PermissionRequiredMixin, DeleteView):
    model = ModelDriveBridge
    template_name = 'references/model_drive_bridge/model_drive_bridge_delete.html'
    success_url = reverse_lazy('/', )


class ControlledBridgeModelList(PermissionRequiredMixin, ListView):
    model = ControlledBridgeModel
    template_name = 'references/controlled_bridge_model/controlled_bridge_model_list.html'
    context_object_name = 'controlled_bridge_model_list'


class ControlledBridgeModelCreate(PermissionRequiredMixin, CreateView):
    model = ControlledBridgeModel
    form_class = form.CreateControlledBridgeModel
    template_name = 'references/controlled_bridge_model/controlled_bridge_model_create.html'
    context_object_name = 'controlled_bridge_model_create'


class ControlledBridgeModelUpdate(PermissionRequiredMixin, UpdateView):
    form_class = form.CreateControlledBridgeModel
    template_name = 'references/controlled_bridge_model/controlled_bridge_model_create.html'
    model = ControlledBridgeModel


class ControlledBridgeModelDelete(PermissionRequiredMixin, DeleteView):
    model = ControlledBridgeModel
    template_name = 'references/controlled_bridge_model/controlled_bridge_model_delete.html'
    success_url = reverse_lazy('/', )


class TypeMaintenanceList(PermissionRequiredMixin, ListView):
    model = TypeMaintenance
    template_name = 'references/type_maintenance/type_maintenance_list.html'
    context_object_name = 'type_maintenance_list'


class TypeMaintenanceCreate(PermissionRequiredMixin, CreateView):
    model = TypeMaintenance
    form_class = form.CreateTypeMaintenance
    template_name = 'references/type_maintenance/type_maintenance_create.html'
    context_object_name = 'type_maintenance_create'


class TypeMaintenanceUpdate(PermissionRequiredMixin, UpdateView):
    form_class = form.CreateTypeMaintenance
    template_name = 'references/type_maintenance/type_maintenance_create.html'
    model = TypeMaintenance


class TypeMaintenanceDelete(PermissionRequiredMixin, DeleteView):
    model = TypeMaintenance
    template_name = 'references/type_maintenance/type_maintenance_delete.html'
    success_url = reverse_lazy('/', )


class FailureNodeList(PermissionRequiredMixin, ListView):
    model = FailureNode
    template_name = 'references/failure_node/failure_node_list.html'
    context_object_name = 'failure_node_list'


class FailureNodeCreate(PermissionRequiredMixin, CreateView):
    model = FailureNode
    form_class = form.CreateFailureNode
    template_name = 'references/failure_node/failure_node_create.html'
    context_object_name = 'failure_node_create'


class FailureNodeUpdate(PermissionRequiredMixin, UpdateView):
    form_class = form.CreateFailureNode
    template_name = 'references/failure_node/failure_node_create.html'
    model = FailureNode


class FailureNodeDelete(PermissionRequiredMixin, DeleteView):
    model = FailureNode
    template_name = 'references/failure_node/failure_node_delete.html'
    success_url = reverse_lazy('/', )


class RecoveryMethodList(PermissionRequiredMixin, ListView):
    model = RecoveryMethod
    template_name = 'references/recovery_method/recovery_method_list.html'
    context_object_name = 'recovery_method_list'


class RecoveryMethodCreate(PermissionRequiredMixin, CreateView):
    model = RecoveryMethod
    form_class = form.CreateRecoveryMethod
    template_name = 'references/recovery_method/recovery_method_create.html'
    context_object_name = 'recovery_method_create'


class RecoveryMethodUpdate(PermissionRequiredMixin, UpdateView):
    form_class = form.CreateRecoveryMethod
    template_name = 'references/recovery_method/recovery_method_create.html'
    model = RecoveryMethod


class RecoveryMethodDelete(PermissionRequiredMixin, DeleteView):
    model = RecoveryMethod
    template_name = 'references/recovery_method/recovery_method_delete.html'
    success_url = reverse_lazy('/', )


class ServiceCompanyList(PermissionRequiredMixin, ListView):
    model = ServiceCompany
    template_name = 'references/service_company/service_company_list.html'
    context_object_name = 'service_company_list'


class ServiceCompanyCreate(PermissionRequiredMixin, CreateView):
    model = ServiceCompany
    form_class = form.CreateServiceCompany
    template_name = 'references/service_company/service_company_create.html'
    context_object_name = 'service_company_create'


class ServiceCompanyUpdate(PermissionRequiredMixin, UpdateView):
    form_class = form.CreateServiceCompany
    template_name = 'references/service_company/service_company_create.html'
    model = ServiceCompany


class ServiceCompanyDelete(PermissionRequiredMixin, DeleteView):
    model = ServiceCompany
    template_name = 'references/service_company/service_company_delete.html'
    success_url = reverse_lazy('/', )


class OrganizationMaintenanceList(PermissionRequiredMixin, ListView):
    model = OrganizationMaintenance
    template_name = 'references/organization_maintenance/organization_maintenance_list.html'
    context_object_name = 'organization_maintenance_list'


class OrganizationMaintenanceCreate(PermissionRequiredMixin, CreateView):
    model = OrganizationMaintenance
    form_class = form.CreateOrganizationMaintenance
    template_name = 'references/organization_maintenance/organization_maintenance_create.html'
    context_object_name = 'organization_maintenance_create'


class OrganizationMaintenanceUpdate(PermissionRequiredMixin, UpdateView):
    form_class = form.CreateOrganizationMaintenance
    template_name = 'references/organization_maintenance/organization_maintenance_create.html'
    model = OrganizationMaintenance


class OrganizationMaintenanceDelete(PermissionRequiredMixin, DeleteView):
    model = OrganizationMaintenance
    template_name = 'references/organization_maintenance/organization_maintenance_delete.html'
    success_url = reverse_lazy('/', )
