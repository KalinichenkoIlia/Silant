from django.contrib.auth.mixins import PermissionRequiredMixin
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView, TemplateView
from service.mixins import ManagerMixin
import references.forms as form
import references.models as model


class References(ManagerMixin, TemplateView):
    permission_required = 'references.view_references'
    template_name = 'references/references.html'


class ModelTechniqueList(PermissionRequiredMixin, ListView):
    permission_required = 'references.view_modeltechnique'
    model = model.ModelTechnique
    template_name = 'references/model_technique/model_technique_list.html'
    context_object_name = 'model_technique_list'


class ModelTechniqueCreate(PermissionRequiredMixin, CreateView):
    permission_required = 'references.add_modeltechnique'
    model = model.ModelTechnique
    form_class = form.CreateModelTechnique
    template_name = 'references/references_create.html'
    context_object_name = 'model_technique_create'


class ModelTechniqueUpdate(PermissionRequiredMixin, UpdateView):
    permission_required = 'references.change_modeltechnique'
    form_class = form.CreateModelTechnique
    template_name = 'references/references_create.html'
    model = model.ModelTechnique


class ModelTechniqueDelete(PermissionRequiredMixin, DeleteView):
    permission_required = 'references.delete_modeltechnique'
    model = model.ModelTechnique
    template_name = 'references/model_technique/model_technique_delete.html'
    success_url = reverse_lazy('/', )


class EngineModelList(PermissionRequiredMixin, ListView):
    permission_required = 'references.view_enginemodel'
    model = model.EngineModel
    template_name = 'references/engine_model/engine_model_list.html'
    context_object_name = 'engine_model_list'


class EngineModelCreate(PermissionRequiredMixin, CreateView):
    permission_required = 'references.add_enginemodel'
    model = model.EngineModel
    form_class = form.CreateEngineModel
    template_name = 'references/references_create.html'
    context_object_name = 'engine_model_create'


class EngineModelUpdate(PermissionRequiredMixin, UpdateView):
    permission_required = 'references.change_enginemodel'
    form_class = form.CreateEngineModel
    template_name = 'references/references_create.html'
    model = model.EngineModel


class EngineModelDelete(PermissionRequiredMixin, DeleteView):
    permission_required = 'references.delete_enginemodel'
    model = model.EngineModel
    template_name = 'references/engine_model/engine_model_delete.html'
    success_url = reverse_lazy('/', )


class TransmissionModelList(PermissionRequiredMixin, ListView):
    permission_required = 'references.view_transmissionmodel'
    model = model.TransmissionModel
    template_name = 'references/transmission_model/transmission_model_list.html'
    context_object_name = 'transmission_model_list'


class TransmissionModelCreate(PermissionRequiredMixin, CreateView):
    permission_required = 'references.add_transmissionmodel'
    model = model.TransmissionModel
    form_class = form.CreateTransmissionModel
    template_name = 'references/references_create.html'
    context_object_name = 'transmission_model_create'


class TransmissionModelUpdate(PermissionRequiredMixin, UpdateView):
    permission_required = 'references.change_transmissionmodel'
    form_class = form.CreateTransmissionModel
    template_name = 'references/references_create.html'
    model = model.TransmissionModel


class TransmissionModelDelete(PermissionRequiredMixin, DeleteView):
    permission_required = 'references.delete_transmissionmodel'
    model = model.TransmissionModel
    template_name = 'references/transmission_model/transmission_model_delete.html'
    success_url = reverse_lazy('/', )


class ModelDriveBridgeList(PermissionRequiredMixin, ListView):
    permission_required = 'references.view_modeldrivebridge'
    model = model.ModelDriveBridge
    template_name = 'references/model_drive_bridge/model_drive_bridge_list.html'
    context_object_name = 'model_drive_bridge_list'


class ModelDriveBridgeCreate(PermissionRequiredMixin, CreateView):
    permission_required = 'references.add_modeldrivebridge'
    model = model.ModelDriveBridge
    form_class = form.CreateModelDriveBridge
    template_name = 'references/references_create.html'
    context_object_name = 'model_drive_bridge_create'


class ModelDriveBridgeUpdate(PermissionRequiredMixin, UpdateView):
    permission_required = 'references.change_modeldrivebridge'
    form_class = form.CreateModelDriveBridge
    template_name = 'references/references_create.html'
    model = model.ModelDriveBridge


class ModelDriveBridgeDelete(PermissionRequiredMixin, DeleteView):
    permission_required = 'references.delete_modeldrivebridge'
    model = model.ModelDriveBridge
    template_name = 'references/model_drive_bridge/model_drive_bridge_delete.html'
    success_url = reverse_lazy('/', )


class ControlledBridgeModelList(PermissionRequiredMixin, ListView):
    permission_required = 'references.view_controlledbridgemodel'
    model = model.ControlledBridgeModel
    template_name = 'references/controlled_bridge_model/controlled_bridge_model_list.html'
    context_object_name = 'controlled_bridge_model_list'


class ControlledBridgeModelCreate(PermissionRequiredMixin, CreateView):
    permission_required = 'references.add_controlledbridgemodel'
    model = model.ControlledBridgeModel
    form_class = form.CreateControlledBridgeModel
    template_name = 'references/references_create.html'
    context_object_name = 'controlled_bridge_model_create'


class ControlledBridgeModelUpdate(PermissionRequiredMixin, UpdateView):
    permission_required = 'references.change_controlledbridgemodel'
    form_class = form.CreateControlledBridgeModel
    template_name = 'references/references_create.html'
    model = model.ControlledBridgeModel


class ControlledBridgeModelDelete(PermissionRequiredMixin, DeleteView):
    permission_required = 'references.delete_controlledbridgemodel'
    model = model.ControlledBridgeModel
    template_name = 'references/controlled_bridge_model/controlled_bridge_model_delete.html'
    success_url = reverse_lazy('/', )


class TypeMaintenanceList(PermissionRequiredMixin, ListView):
    permission_required = 'references.view_typemaintenance'
    model = model.TypeMaintenance
    template_name = 'references/type_maintenance/type_maintenance_list.html'
    context_object_name = 'type_maintenance_list'


class TypeMaintenanceCreate(PermissionRequiredMixin, CreateView):
    permission_required = 'references.add_typemaintenance'
    model = model.TypeMaintenance
    form_class = form.CreateTypeMaintenance
    template_name = 'references/references_create.html'
    context_object_name = 'type_maintenance_create'


class TypeMaintenanceUpdate(PermissionRequiredMixin, UpdateView):
    permission_required = 'references.change_typemaintenance'
    form_class = form.CreateTypeMaintenance
    template_name = 'references/references_create.html'
    model = model.TypeMaintenance


class TypeMaintenanceDelete(PermissionRequiredMixin, DeleteView):
    permission_required = 'references.delete_typemaintenance'
    model = model.TypeMaintenance
    template_name = 'references/type_maintenance/type_maintenance_delete.html'
    success_url = reverse_lazy('/', )


class FailureNodeList(PermissionRequiredMixin, ListView):
    permission_required = 'references.view_failurenode'
    model = model.FailureNode
    template_name = 'references/failure_node/failure_node_list.html'
    context_object_name = 'failure_node_list'


class FailureNodeCreate(PermissionRequiredMixin, CreateView):
    permission_required = 'references.add_failurenode'
    model = model.FailureNode
    form_class = form.CreateFailureNode
    template_name = 'references/references_create.html'
    context_object_name = 'failure_node_create'


class FailureNodeUpdate(PermissionRequiredMixin, UpdateView):
    permission_required = 'references.change_failurenode'
    form_class = form.CreateFailureNode
    template_name = 'references/references_create.html'
    model = model.FailureNode


class FailureNodeDelete(PermissionRequiredMixin, DeleteView):
    permission_required = 'references.delete_failurenode'
    model = model.FailureNode
    template_name = 'references/failure_node/failure_node_delete.html'
    success_url = reverse_lazy('/', )


class RecoveryMethodList(PermissionRequiredMixin, ListView):
    permission_required = 'references.view_recoverymethod'
    model = model.RecoveryMethod
    template_name = 'references/recovery_method/recovery_method_list.html'
    context_object_name = 'recovery_method_list'


class RecoveryMethodCreate(PermissionRequiredMixin, CreateView):
    permission_required = 'references.add_recoverymethod'
    model = model.RecoveryMethod
    form_class = form.CreateRecoveryMethod
    template_name = 'references/references_create.html'
    context_object_name = 'recovery_method_create'


class RecoveryMethodUpdate(PermissionRequiredMixin, UpdateView):
    permission_required = 'references.change_recoverymethod'
    form_class = form.CreateRecoveryMethod
    template_name = 'references/references_create.html'
    model = model.RecoveryMethod


class RecoveryMethodDelete(PermissionRequiredMixin, DeleteView):
    permission_required = 'references.delete_recoverymethod'
    model = model.RecoveryMethod
    template_name = 'references/recovery_method/recovery_method_delete.html'
    success_url = reverse_lazy('/', )


class ServiceCompanyList(PermissionRequiredMixin, ListView):
    permission_required = 'references.view_servicecompany'
    model = model.ServiceCompany
    template_name = 'references/service_company/service_company_list.html'
    context_object_name = 'service_company_list'


class ServiceCompanyCreate(PermissionRequiredMixin, CreateView):
    permission_required = 'references.add_servicecompany'
    model = model.ServiceCompany
    form_class = form.CreateServiceCompany
    template_name = 'references/references_create.html'
    context_object_name = 'service_company_create'


class ServiceCompanyUpdate(PermissionRequiredMixin, UpdateView):
    permission_required = 'references.change_servicecompany'
    form_class = form.CreateServiceCompany
    template_name = 'references/references_create.html'
    model = model.ServiceCompany


class ServiceCompanyDelete(PermissionRequiredMixin, DeleteView):
    permission_required = 'references.delete_servicecompany'
    model = model.ServiceCompany
    template_name = 'references/service_company/service_company_delete.html'
    success_url = reverse_lazy('/', )


class OrganizationMaintenanceList(PermissionRequiredMixin, ListView):
    permission_required = 'references.view_organizationmaintenance'
    model = model.OrganizationMaintenance
    template_name = 'references/organization_maintenance/organization_maintenance_list.html'
    context_object_name = 'organization_maintenance_list'


class OrganizationMaintenanceCreate(PermissionRequiredMixin, CreateView):
    permission_required = 'references.add_organizationmaintenance'
    model = model.OrganizationMaintenance
    form_class = form.CreateOrganizationMaintenance
    template_name = 'references/references_create.html'
    context_object_name = 'organization_maintenance_create'


class OrganizationMaintenanceUpdate(PermissionRequiredMixin, UpdateView):
    permission_required = 'references.change_organizationmaintenance'
    form_class = form.CreateOrganizationMaintenance
    template_name = 'references/references_create.html'
    model = model.OrganizationMaintenance


class OrganizationMaintenanceDelete(PermissionRequiredMixin, DeleteView):
    permission_required = 'references.delete_organizationmaintenance'
    model = model.OrganizationMaintenance
    template_name = 'references/organization_maintenance/organization_maintenance_delete.html'
    success_url = reverse_lazy('/', )
