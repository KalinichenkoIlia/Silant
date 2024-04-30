from rest_framework import serializers
from service import models


class SerializersCar(serializers.ModelSerializer):
    class Meta:
        model = models.Car
        fields = ['factory_number', 'model_technique', 'engine_model', 'engine_serial_number',
                  'transmission_model', 'transmission_serial_numbers', 'model_drive_bridge',
                  'factory_number_drive_bridge', 'controlled_bridge_model', 'factory_number_controlled_bridge',
                  'delivery_agreement', 'factory_shipment_date', 'consignee', 'delivery_address',
                  'equipment', 'client', 'service_company'
                  ]


class SerializersTechnicalMaintenance(serializers.ModelSerializer):
    class Meta:
        model = models.TechnicalMaintenance
        fields = [
            'type_maintenance', 'date_event', 'operating_time', 'order_number', 'date_order',
            'organization_maintenance', 'car', 'service_company'
        ]


class SerializersComplaints(serializers.ModelSerializer):
    class Meta:
        model = models.Complaints
        fields = [
            'date_refusal', 'operating_time', 'failure_node', 'description_failure',
            'recovery_method', 'list_spare_parts', 'date_restoration', 'car', 'service_company',
            'equipment_downtime'
        ]
