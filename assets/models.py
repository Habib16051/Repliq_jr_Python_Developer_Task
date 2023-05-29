from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone


class Company(models.Model):
    name = models.CharField(max_length=100)  # Name of the company

    def __str__(self):
        return self.name


class Employee(models.Model):
    name = models.CharField(max_length=100)  # Name of the employee
    # Company the employee belongs to
    company = models.ForeignKey(Company, on_delete=models.CASCADE)

    def __str__(self):
        return self.name


class Asset(models.Model):
    name = models.CharField(max_length=100)  # Name of the asset
    # Company the asset belongs to
    company = models.ForeignKey(Company, on_delete=models.CASCADE)
    assigned_date = models.DateField(
        null=True, blank=True)  # Date the asset was assigned
    # Date the asset was returned (if applicable)
    returned_date = models.DateField(null=True, blank=True)

    def __str__(self):
        return self.name


class DeviceLog(models.Model):
    # Asset associated with the device log
    device = models.ForeignKey(Asset, on_delete=models.CASCADE)
    # Employee associated with the device log
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE)
    # Date and time the device was checked out
    checkout_date = models.DateTimeField()
    # Date and time the device was returned (if applicable)
    return_date = models.DateTimeField(null=True, blank=True)
    condition = models.TextField(blank=True)  # Condition of the device

    def __str__(self):
        return f"{self.device} - {self.employee}"


class Subscription(models.Model):
    # Company associated with the subscription
    company = models.ForeignKey(Company, on_delete=models.CASCADE)
    # Default start date is the current date
    start_date = models.DateField(default=timezone.now)
    # End date of the subscription (can be null or blank)
    end_date = models.DateField(null=True, blank=True)
    # Indicates if the subscription is active or not
    active = models.BooleanField(default=True)

    def __str__(self):
        return f"{self.company} Subscription"
