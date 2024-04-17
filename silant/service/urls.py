from django.urls import path
from django.conf.urls.static import static
from django.conf import settings
from django.views.decorators.cache import cache_page

from service import views

urlpatterns = [
                  path('', views.HomePage.as_view(), name='home'),
                  path('car/<int:pk>/', views.CarDetail.as_view(), name='car_detail'),
                  path('car/create/', views.CarCreate.as_view(), name='car_create'),
                  path('car/<int:pk>/update/', views.CarUpdate.as_view(), name='car_update'),
                  path('car/<int:pk>/delete/', views.CarDelete.as_view(), name='car_delete'),

                  path('technical_service/<int:pk>/', views.TechnicalMaintenanceDetail.as_view(),
                       name='technical_service_detail'),
                  path('technical_service/create/', views.TechnicalMaintenanceCreate.as_view(),
                       name='technical_service_CREATE'),
                  path('technical_service/<int:pk>/update/', views.TechnicalMaintenanceUpdate.as_view(),
                       name='technical_service_update'),
                  path('technical_service/<int:pk>/delete/', views.TechnicalMaintenanceDelete.as_view(),
                       name='technical_service_delete'),

                  path('complaints/<int:pk>/', views.ComplaintsDetail.as_view(), name='complaints_detail'),
                  path('complaints/create/', views.ComplaintsCreate.as_view(), name='complaints_create'),
                  path('complaints/<int:pk>/update/', views.ComplaintsUpdate.as_view(), name='complaints_update'),
                  path('complaints/<int:pk>/delete/', views.ComplaintsDelete.as_view(), name='complaints_delete'),

              ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
