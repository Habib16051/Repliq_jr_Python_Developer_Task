from rest_framework import viewsets
from .models import Company, Employee, Asset, DeviceLog
from .serializers import CompanySerializer, EmployeeSerializer, AssetSerializer, DeviceLogSerializer


class CompanyViewSet(viewsets.ModelViewSet):
    queryset = Company.objects.all()  # Retrieve all instances of the Company model
    # Use the CompanySerializer for serialization
    serializer_class = CompanySerializer


class EmployeeViewSet(viewsets.ModelViewSet):
    queryset = Employee.objects.all()  # Retrieve all instances of the Employee model
    # Use the EmployeeSerializer for serialization
    serializer_class = EmployeeSerializer


class AssetViewSet(viewsets.ModelViewSet):
    queryset = Asset.objects.all()  # Retrieve all instances of the Asset model
    serializer_class = AssetSerializer  # Use the AssetSerializer for serialization


class DeviceLogViewSet(viewsets.ModelViewSet):
    # Retrieve all instances of the DeviceLog model
    queryset = DeviceLog.objects.all()
    # Use the DeviceLogSerializer for serialization
    serializer_class = DeviceLogSerializer
