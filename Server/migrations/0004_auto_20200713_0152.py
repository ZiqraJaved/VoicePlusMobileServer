# Generated by Django 3.0.8 on 2020-07-12 20:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Server', '0003_auto_20200713_0136'),
    ]

    operations = [
        migrations.AlterField(
            model_name='usermodel',
            name='image',
            field=models.ImageField(null=True, upload_to='uploads/', verbose_name='image'),
        ),
    ]