from django.db import models
from accounts.models import Profile

import references.models as references


class Car(models.Model):
    factory_number = models.CharField(unique=True, max_length=128, verbose_name='Заводской номер')
    model_technique = models.ForeignKey(references.ModelTechnique, on_delete=models.PROTECT,
                                        verbose_name='Модель техники')

    engine_model = models.ForeignKey(references.EngineModel, on_delete=models.PROTECT, verbose_name='Модель двигателя')
    engine_serial_number = models.CharField(max_length=128, verbose_name='Зав. № двигателя')

    transmission_model = models.ForeignKey(references.TransmissionModel, on_delete=models.PROTECT,
                                           verbose_name='Модель трансмиссии')
    transmission_serial_numbers = models.CharField(max_length=128, verbose_name='Зав. № трансмиссии')

    model_drive_bridge = models.ForeignKey(references.ModelDriveBridge, on_delete=models.PROTECT,
                                           verbose_name='Модель ведущего моста')
    factory_number_drive_bridge = models.CharField(max_length=128, verbose_name='Зав. № ведущего моста')

    controlled_bridge_model = models.ForeignKey(references.ControlledBridgeModel, on_delete=models.PROTECT,
                                                verbose_name='Модель управляемого моста')
    factory_number_controlled_bridge = models.CharField(max_length=128, verbose_name='Зав. № управляемого моста')

    delivery_agreement = models.TextField(verbose_name='Договор поставки №, дата', blank=True, null=True)
    factory_shipment_date = models.DateField(auto_now_add=False, verbose_name='Дата отгрузки с завода')

    consignee = models.TextField(verbose_name='Грузополучатель')
    delivery_address = models.TextField(verbose_name='Адрес поставки')
    equipment = models.TextField(verbose_name='Комплектация (доп. опции)')
    client = models.OneToOneField(Profile, on_delete=models.PROTECT, verbose_name='Клиент')
    service_company = models.OneToOneField(references.ServiceCompany, on_delete=models.PROTECT,
                                           verbose_name='Сервисная компания')

    class Meta:
        verbose_name = 'Машины'
        verbose_name_plural = 'Машины'

    def __str__(self):
        return f'{self.model_technique}: {self.client}'


class TechnicalMaintenance(models.Model):
    type_maintenance = models.ForeignKey(references.TypeMaintenance, on_delete=models.PROTECT, verbose_name='Вид ТО')
    date_event = models.DateField(auto_now_add=False, verbose_name='Дата проведения ТО')
    operating_time = models.IntegerField(default=0, verbose_name='Наработка, м/час')
    order_number = models.CharField(max_length=128, verbose_name='№ заказ-наряда')
    date_order = models.DateField(auto_now_add=False, verbose_name='Дата заказ-наряда')
    organization_maintenance = models.ForeignKey(references.OrganizationMaintenance, on_delete=models.PROTECT,
                                                 verbose_name='Организация, проводившая ТО')
    car = models.ForeignKey(Car, on_delete=models.PROTECT, verbose_name='Машина')
    service_company = models.ForeignKey(references.ServiceCompany, on_delete=models.PROTECT,
                                        verbose_name='Сервисная компания')

    class Meta:
        verbose_name = 'Техническое обслуживание'
        verbose_name_plural = 'Техническое обслуживание'

    def __str__(self):
        return f'{self.car}: {self.service_company}'


class Complaints(models.Model):
    date_refusal = models.DateField(auto_now_add=False, verbose_name='Дата отказа')
    operating_time = models.IntegerField(default=0, verbose_name='Наработка, м/час')
    failure_node = models.ForeignKey(references.FailureNode, on_delete=models.PROTECT, verbose_name='Узел отказа')
    description_failure = models.TextField(verbose_name='	Описание отказа')
    recovery_method = models.ForeignKey(references.RecoveryMethod, on_delete=models.PROTECT,
                                        verbose_name='Способ восстановления')
    list_spare_parts = models.TextField(verbose_name='Используемые запасные части')
    date_restoration = models.DateField(default='В ремонте', auto_now_add=False, blank=True, null=True, verbose_name='Дата восстановления')
    equipment_downtime = models.IntegerField(blank=True, null=True, verbose_name='Время простоя техники')
    car = models.ForeignKey(Car, on_delete=models.PROTECT, verbose_name='Mашина')
    service_company = models.ForeignKey(references.ServiceCompany, on_delete=models.PROTECT,
                                        verbose_name='Cервисная компания')

    class Meta:
        verbose_name = 'Рекламации'
        verbose_name_plural = 'Рекламации'

    def save(self, *args, **kwargs):
        if self.date_restoration is None:
            self.equipment_downtime = 0
            super().save(*args, **kwargs)
        elif self.date_restoration and self.date_refusal:
            self.equipment_downtime = (self.date_restoration - self.date_refusal).days
            super().save(*args, **kwargs)

    def __str__(self):
        return f'{self.car}: {self.service_company}'
