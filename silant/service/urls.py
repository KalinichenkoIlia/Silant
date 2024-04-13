from django.urls import path
from .views import home_page
from django.conf.urls.static import static
from django.conf import settings
from django.views.decorators.cache import cache_page

urlpatterns = [
    path('', cache_page(60)(home_page)),
    path('home/', home_page, name='home')
              ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
