from django.db import models
from django.contrib.auth.models import User


class Profile(models.Model):

    client = 'CL'
    manager = 'MG'
    service_company = 'SC'

    POSITIONS = [
        (client, 'Клиент'),
        (manager, 'Менеджер'),
        (service_company, 'Сервисная компания')
    ]

    user = models.OneToOneField(User, on_delete=models.PROTECT, verbose_name='Пользователь ')
    position = models.CharField(max_length=2, choices=POSITIONS, default=client, verbose_name='Вид деятельности')


    class Meta:
        verbose_name = 'Профили'
        verbose_name_plural = 'Профили'

    def __str__(self):
        return f'{self.user} {self.position}'
