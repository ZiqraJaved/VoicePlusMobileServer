# Generated by Django 3.0.8 on 2020-07-18 23:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Server', '0007_auto_20200719_0441'),
    ]

    operations = [
        migrations.AlterField(
            model_name='repairordermodel',
            name='charges',
            field=models.IntegerField(null=True),
        ),
    ]
