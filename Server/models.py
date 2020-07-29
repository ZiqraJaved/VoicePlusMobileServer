from datetime import datetime

import django
from django.db import models


# Create your models here.
class UserModel(models.Model):
    user_phone_number = models.CharField(max_length=13, unique=True, null=False)

    user_password = models.CharField(max_length=20, null=False)
    user_real_name = models.CharField(max_length=100, null=False)
    user_address = models.CharField(max_length=255, null=False)
    image = models.ImageField(upload_to='uploads/', verbose_name='image', null=True)

    user_role = models.CharField(default='consumer', max_length=11, null=False)
    created_at = models.DateTimeField(default=django.utils.timezone.now)

    class Meta:
        db_table = 'tbl_login_user'

    def __str__(self):
        return self.user_real_name


class PricingModel(models.Model):
    mobile_company = models.CharField(max_length=50, default=None, null=False)
    mobile_model = models.CharField(max_length=50, default=None, null=False)
    repairing_part = models.CharField(max_length=70, default=None, null=False)
    repairing_price = models.IntegerField(default=0, null=True)
    repairing_description = models.TextField(max_length=1000, null=False, default=None)

    class Meta:
        db_table = "tbl_repair_pricing"
        unique_together = ('mobile_company', 'mobile_model', 'repairing_part')

    def __str__(self):
        return self.mobile_company + " " + self.mobile_model + " " + self.repairing_part


class RepairOrderModel(models.Model):
    user_phone_number = models.ForeignKey(UserModel, to_field='user_phone_number', null=False, on_delete=models.CASCADE)
    mobile_brand = models.CharField(max_length=50, null=False)
    mobile_model = models.CharField(max_length=50, null=False)
    mobile_fault = models.TextField(max_length=1000, null=True)
    image = models.ImageField(upload_to='uploads/', verbose_name='image', null=True)

    date_order_placed = models.DateTimeField(default=django.utils.timezone.now)
    date_item_received = models.DateTimeField(null=True)
    date_item_delivered = models.DateTimeField(null=True)

    order_status = models.CharField(max_length=20, null=False, default="Pending")
    has_repaired = models.BooleanField(default=False)

    charges = models.IntegerField(null=True)

    created_at = models.DateTimeField(default=django.utils.timezone.now)

    class Meta:
        db_table = "tbl_repair_order"


class FeedbackModel(models.Model):
    user_phone_number = models.ForeignKey(UserModel, to_field='user_phone_number', null=False,
                                          on_delete=models.CASCADE)
    user_real_name = models.CharField(max_length=100, null=False)
    user_feedback = models.TextField(max_length=3000, null=False, default=None)

    created_at = models.DateTimeField(default=django.utils.timezone.now)

    class Meta:
        db_table = "tbl_feedback"


class GalleryModel(models.Model):
    gallery_image = models.ImageField(upload_to='uploads/', verbose_name='gallery_image', null=True)
    mobile_company = models.CharField(max_length=50, default=None, null=False)
    mobile_model = models.CharField(max_length=50, default=None, null=False)

    class Meta:
        db_table = "tbl_gallery"


class PaymentModel(models.Model):
    order_no = models.OneToOneField(RepairOrderModel, to_field='id',  null=False, on_delete=models.CASCADE)
    payment_method = models.CharField(max_length=50, default=None, null=False)
    payment_no = models.CharField(max_length=50, default=None, null=False)
    amount_paid = models.CharField(max_length=50, default=None, null=False)

    class Meta:
        db_table = "tbl_payment"
