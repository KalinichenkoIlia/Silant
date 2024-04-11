from django.db import models
import silant.references.models as references


class Car(models.Model):

    factory_number = models.CharField(unique=True)
    model_technique = models.ForeignKey(references.ModelTechnique, on_delete=models.CASCADE)

    engine_model = models.ForeignKey(references.EngineModel, on_delete=models.CASCADE)
    engine_serial_number = models.CharField(max_length=128)

    transmission_model = models.ForeignKey(references.TransmissionModel, on_delete=models.CASCADE)
    transmission_serial_numbers = models.CharField(max_length=128)

    model_drive_bridge = models.ForeignKey(references.ModelDriveBridge, on_delete=models.CASCADE)
    factory_number_drive_bridge = models.CharField(max_length=128)

    controlled_bridge_model = models.ForeignKey(references.ControlledBridgeModel, on_delete=models.CASCADE)
    factory_number_controlled_bridge = models.CharField(max_length=128)

    delivery_agreement = models.TextField()
    factory_shipment_date = models.DateField(auto_now_add=False)

    consignee = models.TextField()
    delivery_address = models.TextField()

    equipment = models.TextField()







