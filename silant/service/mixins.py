from django.contrib.auth.mixins import PermissionRequiredMixin
from .models import Car


class CustomPermissionRequiredMixin(PermissionRequiredMixin):

    def has_permission(self):
        car_id = self.get_object().id
        if self.request.user.is_authenticated:
            if Car.objects.filter(
                    id=car_id,
                    client__user=self.request.user.id) or \
                    Car.objects.filter(
                        id=car_id,
                        service_company__profile__user=self.request.user.id):
                return True

            elif self.request.user.is_staff or self.request.user.profile == 'MG':
                return True

            else:
                return False

        else:
            return True
