from django.db import models


'''Справочники'''


class ModelTechnique(models.Model):
    title = models.CharField(max_length=128)
    description = models.TextField()

    def __str__(self):
        return f'{self.title}: {self.description}'


class EngineModel(models.Model):
    title = models.CharField(max_length=128)
    description = models.TextField()

    def __str__(self):
        return f'{self.title}: {self.description}'


class TransmissionModel(models.Model):
    title = models.CharField(max_length=128)
    description = models.TextField()

    def __str__(self):
        return f'{self.title}: {self.description}'


class ModelDriveBridge(models.Model):
    title = models.CharField(max_length=128)
    description = models.TextField()

    def __str__(self):
        return f'{self.title}: {self.description}'


class ControlledBridgeModel(models.Model):
    title = models.CharField(max_length=128)
    description = models.TextField()

    def __str__(self):
        return f'{self.title}: {self.description}'


class TypeMaintenance(models.Model):
    title = models.CharField(max_length=128)
    description = models.TextField()

    def __str__(self):
        return f'{self.title}: {self.description}'


class FailureNode(models.Model):
    title = models.CharField(max_length=128)
    description = models.TextField()

    def __str__(self):
        return f'{self.title}: {self.description}'


class RecoveryMethod(models.Model):
    title = models.CharField(max_length=128)
    description = models.TextField()

    def __str__(self):
        return f'{self.title}: {self.description}'


class ServiceCompany(models.Model):
    title = models.CharField(max_length=128)
    description = models.TextField()

    def __str__(self):
        return f'{self.title}: {self.description}'
