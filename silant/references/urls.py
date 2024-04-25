from django.conf import settings
from django.conf.urls.static import static
from django.urls import path

from references import views

urlpatterns = [
                  path('references', views.References.as_view(), name='references'),

                  path('model_technique_list/', views.ModelTechniqueList.as_view(), name='model_technique_list'),
                  path('model_technique/create', views.ModelTechniqueCreate.as_view(), name='model_technique_create'),
                  path('model_technique/<int:pk>/update/', views.ModelTechniqueUpdate.as_view(),
                       name='model_technique_update'),
                  path('model_technique/<int:pk>/delete/', views.ModelTechniqueDelete.as_view(),
                       name='model_technique_delete'),

                  path('engine_model_list/', views.EngineModelList.as_view(),
                       name='engine_model_list'),
                  path('engine_model/create/', views.EngineModelCreate.as_view(),
                       name='engine_model_create'),
                  path('engine_model/<int:pk>/update/', views.EngineModelUpdate.as_view(),
                       name='engine_model_update'),
                  path('engine_model/<int:pk>/delete/', views.EngineModelDelete.as_view(),
                       name='engine_model_delete'),

                  path('transmission_model_list/', views.TransmissionModelList.as_view(),
                       name='transmission_model_list'),
                  path('transmission_model/create/', views.TransmissionModelCreate.as_view(),
                       name='transmission_model_create'),
                  path('transmission_model/<int:pk>/update/', views.TransmissionModelUpdate.as_view(),
                       name='transmission_model_update'),
                  path('transmission_model/<int:pk>/delete/', views.TransmissionModelDelete.as_view(),
                       name='transmission_model_delete'),

                  path('model_drive_bridge_list/', views.ModelDriveBridgeList.as_view(),
                       name='model_drive_bridge_list'),
                  path('model_drive_bridge/create/', views.ModelDriveBridgeCreate.as_view(),
                       name='model_drive_bridge_create'),
                  path('model_drive_bridge/<int:pk>/update/', views.ModelDriveBridgeUpdate.as_view(),
                       name='model_drive_bridge_update'),
                  path('model_drive_bridge/<int:pk>/delete/', views.ModelDriveBridgeDelete.as_view(),
                       name='model_drive_bridge_delete'),

                  path('controlled_bridge_model_list/', views.ControlledBridgeModelList.as_view(),
                       name='controlled_bridge_model_list'),
                  path('controlled_bridge_model/create/', views.ControlledBridgeModelCreate.as_view(),
                       name='controlled_bridge_model_create'),
                  path('controlled_bridge_model/<int:pk>/update/', views.ControlledBridgeModelUpdate.as_view(),
                       name='controlled_bridge_model_update'),
                  path('controlled_bridge_model/<int:pk>/delete/', views.ControlledBridgeModelDelete.as_view(),
                       name='controlled_bridge_model_delete'),

                  path('type_maintenance_list/', views.TypeMaintenanceList.as_view(),
                       name='type_maintenance_list'),
                  path('type_maintenance/create/', views.TypeMaintenanceCreate.as_view(),
                       name='type_maintenance_create'),
                  path('type_maintenance/<int:pk>/update/', views.TypeMaintenanceUpdate.as_view(),
                       name='type_maintenance_update'),
                  path('type_maintenance/<int:pk>/delete/', views.TypeMaintenanceDelete.as_view(),
                       name='type_maintenance_delete'),

                  path('failure_node_list/', views.FailureNodeList.as_view(),
                       name='failure_node_list'),
                  path('failure_node/create/', views.FailureNodeCreate.as_view(),
                       name='failure_node_create'),
                  path('failure_node/<int:pk>/update/', views.FailureNodeUpdate.as_view(),
                       name='failure_node_update'),
                  path('failure_node/<int:pk>/delete/', views.FailureNodeDelete.as_view(),
                       name='failure_node_delete'),

                  path('recovery_method_list/', views.RecoveryMethodList.as_view(),
                       name='recovery_method_list'),
                  path('recovery_method/create/', views.RecoveryMethodCreate.as_view(),
                       name='recovery_method_create'),
                  path('recovery_method/<int:pk>/update/', views.RecoveryMethodUpdate.as_view(),
                       name='recovery_method_update'),
                  path('recovery_method/<int:pk>/delete/', views.RecoveryMethodDelete.as_view(),
                       name='recovery_method_delete'),

                  path('service_company_list/', views.ServiceCompanyList.as_view(),
                       name='service_company_list'),
                  path('service_company/create/', views.ServiceCompanyCreate.as_view(),
                       name='service_company_create'),
                  path('service_company/<int:pk>/update/', views.ServiceCompanyUpdate.as_view(),
                       name='service_company_update'),
                  path('service_company/<int:pk>/delete/', views.ServiceCompanyDelete.as_view(),
                       name='service_company_delete'),

                  path('organization_maintenance_list/', views.OrganizationMaintenanceList.as_view(),
                       name='organization_maintenance_list'),
                  path('organization_maintenance/create/', views.OrganizationMaintenanceCreate.as_view(),
                       name='organization_maintenance_create'),
                  path('organization_maintenance/<int:pk>/update/', views.OrganizationMaintenanceUpdate.as_view(),
                       name='organization_maintenance_update'),
                  path('organization_maintenance/<int:pk>/delete/', views.OrganizationMaintenanceDelete.as_view(),
                       name='organization_maintenance_delete'),

              ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
