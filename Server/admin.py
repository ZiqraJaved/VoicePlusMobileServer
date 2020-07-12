from django.contrib import admin
from Server.models import UserModel, PricingModel
# Register your models here.

admin.site.register(UserModel)
admin.site.register(PricingModel)