from django.contrib import admin
from .models import Car, TechnicalMaintenance, Complaints


admin.site.register(Car)
admin.site.register(TechnicalMaintenance)
admin.site.register(Complaints)

# Register your models here.
