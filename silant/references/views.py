from django.contrib.auth.mixins import PermissionRequiredMixin
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView, TemplateView
from service.mixins import CustomPermissionRequiredMixin
import references.forms as form
import references.models as model


class References(PermissionRequiredMixin, TemplateView):
    permission_required = 'references.view_references'
    template_name = 'references/references.html'


class ModelTechniqueList(PermissionRequiredMixin, ListView):
    permission_required = 'references.view_modelTechnique'
    model = model.ModelTechnique
    template_name = 'references/model_technique/model_technique_list.html'
    context_object_name = 'model_technique_list'


class ModelTechniqueCreate(PermissionRequiredMixin, CreateView):
    permission_required = 'references.add_model_modelTechnique'
    model = model.ModelTechnique
    form_class = form.CreateModelTechnique
    template_name = 'references/model_technique/model_technique_create.html'
    context_object_name = 'model_technique_create'


class ModelTechniqueUpdate(PermissionRequiredMixin, UpdateView):
    permission_required = 'references.change_modelTechnique'
    form_class = form.CreateModelTechnique
    template_name = 'references/model_technique/model_technique_create.html'
    model = model.ModelTechnique


class ModelTechniqueDelete(PermissionRequiredMixin, DeleteView):
    permission_required = 'references.delete_modelTechnique'
    model = model.ModelTechnique
    template_name = 'references/model_technique/model_technique_delete.html'
    success_url = reverse_lazy('/', )


class EngineModelList(PermissionRequiredMixin, ListView):
    permission_required = 'references.view_engineModel'
    model = model.EngineModel
    template_name = 'references/engine_model/engine_model_list.html'
    context_object_name = 'engine_model_list'


class EngineModelCreate(PermissionRequiredMixin, CreateView):
    permission_required = 'references.add_engineModel'
    model = model.EngineModel
    form_class = form.CreateEngineModel
    template_name = 'references/engine_model/engine_model_create.html'
    context_object_name = 'engine_model_create'


class EngineModelUpdate(PermissionRequiredMixin, UpdateView):
    permission_required = 'references.change_engineModel'
    form_class = form.CreateEngineModel
    template_name = 'references/engine_model/engine_model_create.html'
    model = model.EngineModel


class EngineModelDelete(PermissionRequiredMixin, DeleteView):
    permission_required = 'references.delete_engineModel'
    model = model.EngineModel
    template_name = 'references/engine_model/engine_model_delete.html'
    success_url = reverse_lazy('/', )


class TransmissionModelList(PermissionRequiredMixin, ListView):
    permission_required = 'references.view_transmissionModel'
    model = model.TransmissionModel
    template_name = 'references/transmission_model/transmission_model_list.html'
    context_object_name = 'transmission_model_list'


class TransmissionModelCreate(PermissionRequiredMixin, CreateView):
    permission_required = 'references.add_transmissionModel'
    model = model.TransmissionModel
    form_class = form.CreateTransmissionModel
    template_name = 'references/transmission_model/transmission_model_create.html'
    context_object_name = 'transmission_model_create'


class TransmissionModelUpdate(PermissionRequiredMixin, UpdateView):
    permission_required = 'references.change_transmissionModel'
    form_class = form.CreateTransmissionModel
    template_name = 'references/transmission_model/transmission_model_create.html'
    model = model.TransmissionModel


class TransmissionModelDelete(PermissionRequiredMixin, DeleteView):
    permission_required = 'references.delete_transmissionModel'
    model = model.TransmissionModel
    template_name = 'references/transmission_model/transmission_model_delete.html'
    success_url = reverse_lazy('/', )


class ModelDriveBridgeList(PermissionRequiredMixin, ListView):
    permission_required = 'references.view_modelDriveBridge'
    model = model.ModelDriveBridge
    template_name = 'references/model_drive_bridge/model_drive_bridge_list.html'
    context_object_name = 'model_drive_bridge_list'


class ModelDriveBridgeCreate(PermissionRequiredMixin, CreateView):
    permission_required = 'references.add_modelDriveBridge'
    model = model.ModelDriveBridge
    form_class = form.CreateModelDriveBridge
    template_name = 'references/model_drive_bridge/model_drive_bridge_create.html'
    context_object_name = 'model_drive_bridge_create'


class ModelDriveBridgeUpdate(PermissionRequiredMixin, UpdateView):
    permission_required = 'references.change_modelDriveBridge'
    form_class = form.CreateModelDriveBridge
    template_name = 'references/model_drive_bridge/model_drive_bridge_create.html'
    model = model.ModelDriveBridge


class ModelDriveBridgeDelete(PermissionRequiredMixin, DeleteView):
    permission_required = 'references.delete_modelDriveBridge'
    model = model.ModelDriveBridge
    template_name = 'references/model_drive_bridge/model_drive_bridge_delete.html'
    success_url = reverse_lazy('/', )


class ControlledBridgeModelList(PermissionRequiredMixin, ListView):
    permission_required = 'references.view_controlledBridgeModel'
    model = model.ControlledBridgeModel
    template_name = 'references/controlled_bridge_model/controlled_bridge_model_list.html'
    context_object_name = 'controlled_bridge_model_list'


class ControlledBridgeModelCreate(PermissionRequiredMixin, CreateView):
    permission_required = 'references.add_controlledBridgeModel'
    model = model.ControlledBridgeModel
    form_class = form.CreateControlledBridgeModel
    template_name = 'references/controlled_bridge_model/controlled_bridge_model_create.html'
    context_object_name = 'controlled_bridge_model_create'


class ControlledBridgeModelUpdate(PermissionRequiredMixin, UpdateView):
    permission_required = 'references.change_controlledBridgeModel'
    form_class = form.CreateControlledBridgeModel
    template_name = 'references/controlled_bridge_model/controlled_bridge_model_create.html'
    model = model.ControlledBridgeModel


class ControlledBridgeModelDelete(PermissionRequiredMixin, DeleteView):
    permission_required = 'references.delete_controlledBridgeModel'
    model = model.ControlledBridgeModel
    template_name = 'references/controlled_bridge_model/controlled_bridge_model_delete.html'
    success_url = reverse_lazy('/', )


class TypeMaintenanceList(PermissionRequiredMixin, ListView):
    permission_required = 'references.view_typeMaintenance'
    model = model.TypeMaintenance
    template_name = 'references/type_maintenance/type_maintenance_list.html'
    context_object_name = 'type_maintenance_list'


class TypeMaintenanceCreate(PermissionRequiredMixin, CreateView):
    permission_required = 'references.add_typeMaintenance'
    model = model.TypeMaintenance
    form_class = form.CreateTypeMaintenance
    template_name = 'references/type_maintenance/type_maintenance_create.html'
    context_object_name = 'type_maintenance_create'


class TypeMaintenanceUpdate(PermissionRequiredMixin, UpdateView):
    permission_required = 'references.change_typeMaintenance'
    form_class = form.CreateTypeMaintenance
    template_name = 'references/type_maintenance/type_maintenance_create.html'
    model = model.TypeMaintenance


class TypeMaintenanceDelete(PermissionRequiredMixin, DeleteView):
    permission_required = 'references.delete_typeMaintenance'
    model = model.TypeMaintenance
    template_name = 'references/type_maintenance/type_maintenance_delete.html'
    success_url = reverse_lazy('/', )


class FailureNodeList(PermissionRequiredMixin, ListView):
    permission_required = 'references.view_failureNode'
    model = model.FailureNode
    template_name = 'references/failure_node/failure_node_list.html'
    context_object_name = 'failure_node_list'


class FailureNodeCreate(PermissionRequiredMixin, CreateView):
    permission_required = 'references.add_failureNode'
    model = model.FailureNode
    form_class = form.CreateFailureNode
    template_name = 'references/failure_node/failure_node_create.html'
    context_object_name = 'failure_node_create'


class FailureNodeUpdate(PermissionRequiredMixin, UpdateView):
    permission_required = 'references.change_failureNode'
    form_class = form.CreateFailureNode
    template_name = 'references/failure_node/failure_node_create.html'
    model = model.FailureNode


class FailureNodeDelete(PermissionRequiredMixin, DeleteView):
    permission_required = 'references.delete_failureNode'
    model = model.FailureNode
    template_name = 'references/failure_node/failure_node_delete.html'
    success_url = reverse_lazy('/', )


class RecoveryMethodList(PermissionRequiredMixin, ListView):
    permission_required = 'references.view_recoveryMethod'
    model = model.RecoveryMethod
    template_name = 'references/recovery_method/recovery_method_list.html'
    context_object_name = 'recovery_method_list'


class RecoveryMethodCreate(PermissionRequiredMixin, CreateView):
    permission_required = 'references.add_recoveryMethod'
    model = model.RecoveryMethod
    form_class = form.CreateRecoveryMethod
    template_name = 'references/recovery_method/recovery_method_create.html'
    context_object_name = 'recovery_method_create'


class RecoveryMethodUpdate(PermissionRequiredMixin, UpdateView):
    permission_required = 'references.change_recoveryMethod'
    form_class = form.CreateRecoveryMethod
    template_name = 'references/recovery_method/recovery_method_create.html'
    model = model.RecoveryMethod


class RecoveryMethodDelete(PermissionRequiredMixin, DeleteView):
    permission_required = 'references.delete_recoveryMethod'
    model = model.RecoveryMethod
    template_name = 'references/recovery_method/recovery_method_delete.html'
    success_url = reverse_lazy('/', )


class ServiceCompanyList(PermissionRequiredMixin, ListView):
    permission_required = 'references.view_serviceCompany'
    model = model.ServiceCompany
    template_name = 'references/service_company/service_company_list.html'
    context_object_name = 'service_company_list'


class ServiceCompanyCreate(PermissionRequiredMixin, CreateView):
    permission_required = 'references.add_serviceCompany'
    model = model.ServiceCompany
    form_class = form.CreateServiceCompany
    template_name = 'references/service_company/service_company_create.html'
    context_object_name = 'service_company_create'


class ServiceCompanyUpdate(PermissionRequiredMixin, UpdateView):
    permission_required = 'references.change_serviceCompany'
    form_class = form.CreateServiceCompany
    template_name = 'references/service_company/service_company_create.html'
    model = model.ServiceCompany


class ServiceCompanyDelete(PermissionRequiredMixin, DeleteView):
    permission_required = 'references.delete_serviceCompany'
    model = model.ServiceCompany
    template_name = 'references/service_company/service_company_delete.html'
    success_url = reverse_lazy('/', )


class OrganizationMaintenanceList(PermissionRequiredMixin, ListView):
    permission_required = 'references.view_organizationMaintenance'
    model = model.OrganizationMaintenance
    template_name = 'references/organization_maintenance/organization_maintenance_list.html'
    context_object_name = 'organization_maintenance_list'


class OrganizationMaintenanceCreate(PermissionRequiredMixin, CreateView):
    permission_required = 'references.add_organizationMaintenance'
    model = model.OrganizationMaintenance
    form_class = form.CreateOrganizationMaintenance
    template_name = 'references/organization_maintenance/organization_maintenance_create.html'
    context_object_name = 'organization_maintenance_create'


class OrganizationMaintenanceUpdate(PermissionRequiredMixin, UpdateView):
    permission_required = 'references.change_organizationMaintenance'
    form_class = form.CreateOrganizationMaintenance
    template_name = 'references/organization_maintenance/organization_maintenance_create.html'
    model = model.OrganizationMaintenance


class OrganizationMaintenanceDelete(PermissionRequiredMixin, DeleteView):
    permission_required = 'references.delete_organizationMaintenance'
    model = model.OrganizationMaintenance
    template_name = 'references/organization_maintenance/organization_maintenance_delete.html'
    success_url = reverse_lazy('/', )
