# Generated by Django 3.0.8 on 2020-07-14 16:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Server', '0004_auto_20200713_0152'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='usermodel',
            name='user_name',
        ),
        migrations.AlterField(
            model_name='usermodel',
            name='user_phone_number',
            field=models.CharField(max_length=13, unique=True),
        ),
    ]
