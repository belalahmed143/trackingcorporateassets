# Generated by Django 4.2.3 on 2023-07-21 18:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('companies_app', '0007_alter_employee_address_alter_employee_phone'),
    ]

    operations = [
        migrations.AlterField(
            model_name='employee',
            name='address',
            field=models.CharField(max_length=200),
        ),
        migrations.AlterField(
            model_name='employee',
            name='phone',
            field=models.CharField(max_length=15, unique=True),
        ),
    ]
