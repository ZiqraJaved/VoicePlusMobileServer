# Generated by Django 3.0.8 on 2020-07-29 22:00

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Server', '0013_auto_20200730_0259'),
    ]

    operations = [
        migrations.AlterField(
            model_name='paymentmodel',
            name='order_no',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='Server.RepairOrderModel'),
        ),
    ]
