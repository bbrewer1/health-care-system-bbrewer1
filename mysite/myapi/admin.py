from django.contrib import admin
from .models import User, BillingInfo, MedicalHistory, Roles, UserRoles, Measurements, Device

# Register your models here.
admin.site.register(User)
admin.site.register(BillingInfo)
admin.site.register(MedicalHistory)
admin.site.register(Roles)
admin.site.register(UserRoles)
admin.site.register(Measurements)
admin.site.register(Device)