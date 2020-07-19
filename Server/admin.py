from django.contrib import admin
from Server.models import UserModel, PricingModel, RepairOrderModel

# Register your models here.

admin.site.register(UserModel)
admin.site.register(PricingModel)
admin.site.register(RepairOrderModel)
