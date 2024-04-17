# Generated by Django 5.0.4 on 2024-04-17 14:32

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0001_initial'),
        ('references', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='servicecompany',
            name='profile',
            field=models.OneToOneField(on_delete=django.db.models.deletion.PROTECT, to='accounts.profile', verbose_name='Профиль сервисной компании '),
        ),
    ]
