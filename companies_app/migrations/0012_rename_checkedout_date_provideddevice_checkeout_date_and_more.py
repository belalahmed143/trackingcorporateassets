# Generated by Django 4.2.3 on 2023-07-21 19:22

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('companies_app', '0011_provideddevice'),
    ]

    operations = [
        migrations.RenameField(
            model_name='provideddevice',
            old_name='checkedout_date',
            new_name='checkeout_date',
        ),
        migrations.RenameField(
            model_name='provideddevice',
            old_name='returned_date',
            new_name='return_date',
        ),
    ]
