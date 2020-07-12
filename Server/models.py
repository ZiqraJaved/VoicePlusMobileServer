from django.db import models


# Create your models here.
class UserModel(models.Model):
    user_name = models.CharField(max_length=20, unique=True, db_index=True, null=False)
    user_password = models.CharField(max_length=20, null=False)
    user_role = models.CharField(default='operator', max_length=20, null=False)

    class Meta:
        db_table = 'tbl_login_user'

    def __str__(self):
        return self.user_name


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
