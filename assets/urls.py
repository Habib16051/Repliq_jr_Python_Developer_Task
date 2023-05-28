from django.urls import path, include
from rest_framework import routers
from .views import CompanyViewSet, EmployeeViewSet, AssetViewSet, DeviceLogViewSet

router = routers.DefaultRouter()
router.register(r'companies', CompanyViewSet)
router.register(r'employees', EmployeeViewSet)
router.register(r'assets', AssetViewSet)
router.register(r'devicelogs', DeviceLogViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
