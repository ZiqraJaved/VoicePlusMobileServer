# Generated by Django 3.0.8 on 2020-07-12 20:36

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('Server', '0002_auto_20200713_0133'),
    ]

    operations = [
        migrations.AlterField(
            model_name='usermodel',
            name='created_at',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]
