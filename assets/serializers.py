from rest_framework import serializers
from .models import Company, Employee, Asset, DeviceLog


class CompanySerializer(serializers.ModelSerializer):
    class Meta:
        model = Company
        fields = '__all__'  # Serialize all fields of the Company model


class EmployeeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Employee
        fields = '__all__'  # Serialize all fields of the Employee model


class AssetSerializer(serializers.ModelSerializer):
    class Meta:
        model = Asset
        fields = '__all__'  # Serialize all fields of the Asset model


class DeviceLogSerializer(serializers.ModelSerializer):
    class Meta:
        model = DeviceLog
        fields = '__all__'  # Serialize all fields of the DeviceLog model
