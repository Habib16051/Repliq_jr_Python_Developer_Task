from django.contrib import admin
from .models import Company, Employee, Asset, DeviceLog, Subscription

# Customizing the Asset admin display


class AssetAdmin(admin.ModelAdmin):
    # Fields to display in the admin list view
    list_display = ('name', 'company', 'assigned_date', 'returned_date')
    list_filter = ('company',)  # Filters available in the admin list view

# Customizing the DeviceLog admin display


class DeviceLogAdmin(admin.ModelAdmin):
    # Fields to display in the admin list view
    list_display = ('device', 'employee', 'checkout_date', 'return_date')
    # Filters available in the admin list view
    list_filter = ('device__company',)

# Customizing the Subscription admin display


class SubscriptionAdmin(admin.ModelAdmin):
    # Fields to display in the admin list view
    list_display = ('company', 'start_date', 'end_date', 'active')
    # Filters available in the admin list view
    list_filter = ('company', 'active')


# Registering the models with their respective admin classes
# Register the Company model with the default admin display
admin.site.register(Company)
# Register the Employee model with the default admin display
admin.site.register(Employee)
# Register the Asset model with the custom AssetAdmin display
admin.site.register(Asset, AssetAdmin)
# Register the DeviceLog model with the custom DeviceLogAdmin display
admin.site.register(DeviceLog, DeviceLogAdmin)
# Register the Subscription model with the custom SubscriptionAdmin display
admin.site.register(Subscription, SubscriptionAdmin)
