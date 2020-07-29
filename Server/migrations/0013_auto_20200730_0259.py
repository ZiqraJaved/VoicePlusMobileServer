# Generated by Django 3.0.8 on 2020-07-29 21:59

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Server', '0012_paymentmodel'),
    ]

    operations = [
        migrations.AlterField(
            model_name='paymentmodel',
            name='order_no',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Server.RepairOrderModel', unique=True),
        ),
    ]