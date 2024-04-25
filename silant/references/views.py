from django.contrib.auth.mixins import PermissionRequiredMixin
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView

import references.forms as form
import references.models as model


class ReferencesList(ListView):
    template_name = 'references.html'


class ModelTechniqueList(PermissionRequiredMixin, ListView):
    model = model.ModelTechnique
    template_name = 'references/model_technique/model_technique_list.html'
    context_object_name = 'model_technique_list'


class ModelTechniqueCreate(PermissionRequiredMixin, CreateView):
    model = model.ModelTechnique
    form_class = form.CreateModelTechnique
    template_name = 'references/model_technique/model_technique_create.html'
    context_object_name = 'model_technique_create'


class ModelTechniqueUpdate(PermissionRequiredMixin, UpdateView):
    form_class = form.CreateModelTechnique
    template_name = 'references/model_technique/model_technique_create.html'
    model = model.ModelTechnique


class ModelTechniqueDelete(PermissionRequiredMixin, DeleteView):
    model = model.ModelTechnique
    template_name = 'references/model_technique/model_technique_delete.html'
    success_url = reverse_lazy('/', )


class EngineModelList(PermissionRequiredMixin, ListView):
    model = model.EngineModel
    template_name = 'references/engine_model/engine_model_list.html'
    context_object_name = 'engine_model_list'


class EngineModelCreate(PermissionRequiredMixin, CreateView):
    model = model.EngineModel
    form_class = form.CreateEngineModel
    template_name = 'references/engine_model/engine_model_create.html'
    context_object_name = 'engine_model_create'


class EngineModelUpdate(PermissionRequiredMixin, UpdateView):
    form_class = form.CreateEngineModel
    template_name = 'references/engine_model/engine_model_create.html'
    model = model.EngineModel


class EngineModelDelete(PermissionRequiredMixin, DeleteView):
    model = model.EngineModel
    template_name = 'references/engine_model/engine_model_delete.html'
    success_url = reverse_lazy('/', )


class TransmissionModelList(PermissionRequiredMixin, ListView):
    model = model.TransmissionModel
    template_name = 'references/transmission_model/transmission_model_list.html'
    context_object_name = 'transmission_model_list'


class TransmissionModelCreate(PermissionRequiredMixin, CreateView):
    model = model.TransmissionModel
    form_class = form.CreateTransmissionModel
    template_name = 'references/transmission_model/transmission_model_create.html'
    context_object_name = 'transmission_model_create'


class TransmissionModelUpdate(PermissionRequiredMixin, UpdateView):
    form_class = form.CreateTransmissionModel
    template_name = 'references/transmission_model/transmission_model_create.html'
    model = model.TransmissionModel


class TransmissionModelDelete(PermissionRequiredMixin, DeleteView):
    model = model.TransmissionModel
    template_name = 'references/transmission_model/transmission_model_delete.html'
    success_url = reverse_lazy('/', )


class ModelDriveBridgeList(PermissionRequiredMixin, ListView):
    model = model.ModelDriveBridge
    template_name = 'references/model_drive_bridge/model_drive_bridge_list.html'
    context_object_name = 'model_drive_bridge_list'


class ModelDriveBridgeCreate(PermissionRequiredMixin, CreateView):
    model = model.ModelDriveBridge
    form_class = form.CreateModelDriveBridge
    template_name = 'references/model_drive_bridge/model_drive_bridge_create.html'
    context_object_name = 'model_drive_bridge_create'


class ModelDriveBridgeUpdate(PermissionRequiredMixin, UpdateView):
    form_class = form.CreateModelDriveBridge
    template_name = 'references/model_drive_bridge/model_drive_bridge_create.html'
    model = model.ModelDriveBridge


class ModelDriveBridgeDelete(PermissionRequiredMixin, DeleteView):
    model = model.ModelDriveBridge
    template_name = 'references/model_drive_bridge/model_drive_bridge_delete.html'
    success_url = reverse_lazy('/', )


class ControlledBridgeModelList(PermissionRequiredMixin, ListView):
    model = model.ControlledBridgeModel
    template_name = 'references/controlled_bridge_model/controlled_bridge_model_list.html'
    context_object_name = 'controlled_bridge_model_list'


class ControlledBridgeModelCreate(PermissionRequiredMixin, CreateView):
    model = model.ControlledBridgeModel
    form_class = form.CreateControlledBridgeModel
    template_name = 'references/controlled_bridge_model/controlled_bridge_model_create.html'
    context_object_name = 'controlled_bridge_model_create'


class ControlledBridgeModelUpdate(PermissionRequiredMixin, UpdateView):
    form_class = form.CreateControlledBridgeModel
    template_name = 'references/controlled_bridge_model/controlled_bridge_model_create.html'
    model = model.ControlledBridgeModel


class ControlledBridgeModelDelete(PermissionRequiredMixin, DeleteView):
    model = model.ControlledBridgeModel
    template_name = 'references/controlled_bridge_model/controlled_bridge_model_delete.html'
    success_url = reverse_lazy('/', )


class TypeMaintenanceList(PermissionRequiredMixin, ListView):
    model = model.TypeMaintenance
    template_name = 'references/type_maintenance/type_maintenance_list.html'
    context_object_name = 'type_maintenance_list'


class TypeMaintenanceCreate(PermissionRequiredMixin, CreateView):
    model = model.TypeMaintenance
    form_class = form.CreateTypeMaintenance
    template_name = 'references/type_maintenance/type_maintenance_create.html'
    context_object_name = 'type_maintenance_create'


class TypeMaintenanceUpdate(PermissionRequiredMixin, UpdateView):
    form_class = form.CreateTypeMaintenance
    template_name = 'references/type_maintenance/type_maintenance_create.html'
    model = model.TypeMaintenance


class TypeMaintenanceDelete(PermissionRequiredMixin, DeleteView):
    model = model.TypeMaintenance
    template_name = 'references/type_maintenance/type_maintenance_delete.html'
    success_url = reverse_lazy('/', )


class FailureNodeList(PermissionRequiredMixin, ListView):
    model = model.FailureNode
    template_name = 'references/failure_node/failure_node_list.html'
    context_object_name = 'failure_node_list'


class FailureNodeCreate(PermissionRequiredMixin, CreateView):
    model = model.FailureNode
    form_class = form.CreateFailureNode
    template_name = 'references/failure_node/failure_node_create.html'
    context_object_name = 'failure_node_create'


class FailureNodeUpdate(PermissionRequiredMixin, UpdateView):
    form_class = form.CreateFailureNode
    template_name = 'references/failure_node/failure_node_create.html'
    model = model.FailureNode


class FailureNodeDelete(PermissionRequiredMixin, DeleteView):
    model = model.FailureNode
    template_name = 'references/failure_node/failure_node_delete.html'
    success_url = reverse_lazy('/', )


class RecoveryMethodList(PermissionRequiredMixin, ListView):
    model = model.RecoveryMethod
    template_name = 'references/recovery_method/recovery_method_list.html'
    context_object_name = 'recovery_method_list'


class RecoveryMethodCreate(PermissionRequiredMixin, CreateView):
    model = model.RecoveryMethod
    form_class = form.CreateRecoveryMethod
    template_name = 'references/recovery_method/recovery_method_create.html'
    context_object_name = 'recovery_method_create'


class RecoveryMethodUpdate(PermissionRequiredMixin, UpdateView):
    form_class = form.CreateRecoveryMethod
    template_name = 'references/recovery_method/recovery_method_create.html'
    model = model.RecoveryMethod


class RecoveryMethodDelete(PermissionRequiredMixin, DeleteView):
    model = model.RecoveryMethod
    template_name = 'references/recovery_method/recovery_method_delete.html'
    success_url = reverse_lazy('/', )


class ServiceCompanyList(PermissionRequiredMixin, ListView):
    model = model.ServiceCompany
    template_name = 'references/service_company/service_company_list.html'
    context_object_name = 'service_company_list'


class ServiceCompanyCreate(PermissionRequiredMixin, CreateView):
    model = model.ServiceCompany
    form_class = form.CreateServiceCompany
    template_name = 'references/service_company/service_company_create.html'
    context_object_name = 'service_company_create'


class ServiceCompanyUpdate(PermissionRequiredMixin, UpdateView):
    form_class = form.CreateServiceCompany
    template_name = 'references/service_company/service_company_create.html'
    model = model.ServiceCompany


class ServiceCompanyDelete(PermissionRequiredMixin, DeleteView):
    model = model.ServiceCompany
    template_name = 'references/service_company/service_company_delete.html'
    success_url = reverse_lazy('/', )


class OrganizationMaintenanceList(PermissionRequiredMixin, ListView):
    model = model.OrganizationMaintenance
    template_name = 'references/organization_maintenance/organization_maintenance_list.html'
    context_object_name = 'organization_maintenance_list'


class OrganizationMaintenanceCreate(PermissionRequiredMixin, CreateView):
    model = model.OrganizationMaintenance
    form_class = form.CreateOrganizationMaintenance
    template_name = 'references/organization_maintenance/organization_maintenance_create.html'
    context_object_name = 'organization_maintenance_create'


class OrganizationMaintenanceUpdate(PermissionRequiredMixin, UpdateView):
    form_class = form.CreateOrganizationMaintenance
    template_name = 'references/organization_maintenance/organization_maintenance_create.html'
    model = model.OrganizationMaintenance


class OrganizationMaintenanceDelete(PermissionRequiredMixin, DeleteView):
    model = model.OrganizationMaintenance
    template_name = 'references/organization_maintenance/organization_maintenance_delete.html'
    success_url = reverse_lazy('/', )
