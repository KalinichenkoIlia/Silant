from django.urls import path
from .views import HomePage
from django.conf.urls.static import static
from django.conf import settings
from django.views.decorators.cache import cache_page

urlpatterns = [
    path('', HomePage.as_view(), name='home')
              ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
