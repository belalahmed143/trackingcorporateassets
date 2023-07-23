from rest_framework import serializers
from  companies_app.models import *

class EmployeeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Employee
        exclude = ('company',)

class DeviceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Device
        exclude = ('company',)


class ProvidedDeviceSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProvidedDevice
        exclude = ('company',)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['employee'].queryset = Employee.objects.filter(company=self.context['request'].user)
        self.fields['device'].queryset = Device.objects.filter(company=self.context['request'].user)


