from django.contrib import admin
from .models import ModelTechnique, EngineModel, TransmissionModel, ModelDriveBridge, ControlledBridgeModel, \
    TypeMaintenance, OrganizationMaintenance, ServiceCompany, RecoveryMethod, FailureNode

admin.site.register(ModelTechnique)
admin.site.register(EngineModel)
admin.site.register(TransmissionModel)
admin.site.register(ModelDriveBridge)
admin.site.register(ControlledBridgeModel)
admin.site.register(TypeMaintenance)
admin.site.register(FailureNode)
admin.site.register(RecoveryMethod)
admin.site.register(ServiceCompany)
admin.site.register(OrganizationMaintenance)
