from django.shortcuts import render
from rest_framework.generics import (ListAPIView,
                                    CreateAPIView,
                                    UpdateAPIView,
                                    DestroyAPIView,
                                    ListCreateAPIView,
                                    RetrieveUpdateDestroyAPIView
                                    )

from companies_app.models import *
from .serializers import *

# Create your views here.

# Employee model api 

class EmployeeListAPIView(ListAPIView):
    serializer_class = EmployeeSerializer

    def get_queryset(self):
        return Employee.objects.filter(company=self.request.user)


class EmployeeCreateView(CreateAPIView):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer

    def perform_create(self, serializer):
        if self.request.user.is_company:
            company = self.request.user
            serializer.save(company=company)
        else:
            raise PermissionDenied()

class EmployeeUpdateAPIView(UpdateAPIView):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer

    def perform_update(self, serializer):
        if self.request.user.is_company:
            company = self.request.user
            serializer.save(company=company)
        else:
            raise PermissionDenied()

class EmployeeDestroyAPIView(DestroyAPIView):
    serializer_class = EmployeeSerializer

    def get_queryset(self):
        return Employee.objects.filter(company=self.request.user)


class DeviceListCreateAPIView(ListCreateAPIView):
    serializer_class = DeviceSerializer

    def get_queryset(self):
        return Device.objects.filter(company=self.request.user)

    def perform_create(self, serializer):
        if self.request.user.is_company:
            company = self.request.user
            serializer.save(company=company)
        else:
            raise PermissionDenied()

class DeviceetrieveUpdateDestroy(RetrieveUpdateDestroyAPIView):
    serializer_class = DeviceSerializer

    def get_queryset(self):
        return Device.objects.filter(company=self.request.user)

    def perform_update(self, serializer):
        if self.request.user.is_company:
            company = self.request.user
            serializer.save(company=company)
        else:
            raise PermissionDenied()




class ProvidedDeviceListAPIView(ListAPIView):
    serializer_class = ProvidedDeviceSerializer

    def get_queryset(self):
        return ProvidedDevice.objects.filter(company=self.request.user)


class ProvidedDeviceCreateAPIView(CreateAPIView):
    serializer_class = ProvidedDeviceSerializer

    def perform_create(self, serializer):
        if self.request.user.is_company:
            company = self.request.user
            serializer.save(company=company)
        else:
            raise PermissionDenied()

class ProvidedDevicerieveUpdateDestroy(RetrieveUpdateDestroyAPIView):
    serializer_class = ProvidedDeviceSerializer

    def get_queryset(self):
        return ProvidedDevice.objects.filter(company=self.request.user)

    def perform_update(self, serializer):
        if self.request.user.is_company:
            company = self.request.user
            serializer.save(company=company)
        else:
            raise PermissionDenied()