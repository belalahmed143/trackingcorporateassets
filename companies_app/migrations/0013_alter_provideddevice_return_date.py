# Generated by Django 4.2.3 on 2023-07-21 19:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('companies_app', '0012_rename_checkedout_date_provideddevice_checkeout_date_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='provideddevice',
            name='return_date',
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]
