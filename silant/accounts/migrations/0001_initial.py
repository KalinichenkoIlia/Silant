# Generated by Django 5.0.4 on 2024-04-12 16:14

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('position', models.CharField(choices=[('CL', 'Клиент'), ('MG', 'Менеджер'), ('SC', 'Сервисная компания')], default='CL', max_length=2, verbose_name='Вид деятельности')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.PROTECT, to=settings.AUTH_USER_MODEL, verbose_name='Пользователь ')),
            ],
            options={
                'verbose_name': 'Профили',
                'verbose_name_plural': 'Профили',
            },
        ),
    ]
