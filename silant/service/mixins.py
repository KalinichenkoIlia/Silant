from django.contrib.auth.mixins import PermissionRequiredMixin
from django.db.models import Q

from .models import Car, TechnicalMaintenance, Complaints


class CustomPermissionRequiredMixin(PermissionRequiredMixin):
    """
    Проверяет отношение клиента или сервисной компании к объекту модели

    :has_permission -> bool
    для менеджера или пользователя с статусом сотрудника -> "True"

    """
    def has_permission(self):

        id_obj: int = self.get_object().id
        user: int = self.request.user.id

        instance_car: bool = self.get_object().__class__.__name__ == 'Car'
        instance_technical: bool = self.get_object().__class__.__name__ == 'TechnicalMaintenance'
        instance_complaints: bool = self.get_object().__class__.__name__ == 'Complaints'

        if self.request.user.is_authenticated:

            if self.request.user.is_staff or self.request.user.profile.position == 'MG':
                return True

            elif instance_car and Car.objects.filter(Q(id=id_obj),
                                                     Q(service_company__profile__user=user) |
                                                     Q(client__user=user)):
                return True

            elif instance_technical and TechnicalMaintenance.objects.filter(Q(id=id_obj),
                                                                            Q(service_company__profile__user=user) |
                                                                            Q(car__client__user=user)):
                return True

            elif instance_complaints and Complaints.objects.filter(Q(id=id_obj),
                                                                   Q(service_company__profile__user=user) |
                                                                   Q(car__client__user=user)):
                return True

            else:
                return False

        elif instance_complaints or instance_technical:
            return False

        else:
            return True


class ManagerMixin(PermissionRequiredMixin):
    def has_permission(self):

        if self.request.user.is_authenticated:

            if self.request.user.is_staff or self.request.user.profile.position == 'MG':
                return True
            else:
                return False
        else:
            return False
