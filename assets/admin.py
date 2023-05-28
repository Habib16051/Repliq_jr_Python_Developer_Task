from django.contrib import admin
from .models import Company, Employee, Asset, DeviceLog, Subscription


class AssetAdmin(admin.ModelAdmin):
    list_display = ('name', 'company', 'assigned_date', 'returned_date')
    list_filter = ('company',)


class DeviceLogAdmin(admin.ModelAdmin):
    list_display = ('device', 'employee', 'checkout_date', 'return_date')
    list_filter = ('device__company',)


class SubscriptionAdmin(admin.ModelAdmin):
    list_display = ('company', 'start_date', 'end_date', 'active')
    list_filter = ('company', 'active')


admin.site.register(Company)
admin.site.register(Employee)
admin.site.register(Asset, AssetAdmin)
admin.site.register(DeviceLog, DeviceLogAdmin)
admin.site.register(Subscription, SubscriptionAdmin)
