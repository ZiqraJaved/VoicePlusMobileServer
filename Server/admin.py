from django.contrib import admin
from Server.models import UserModel, PricingModel, RepairOrderModel,FeedbackModel,GalleryModel,PaymentModel

# Register your models here.

admin.site.register(UserModel)
admin.site.register(PricingModel)
admin.site.register(RepairOrderModel)
admin.site.register(FeedbackModel)
admin.site.register(GalleryModel)
admin.site.register(PaymentModel)
