from django.urls import path
from .views import *

urlpatterns = [
    path('employees-list-api/', EmployeeListAPIView.as_view(), name='employee-list'),
    path('employees-create-api/', EmployeeCreateView.as_view(), name='employee-create'),
    path('employees-update-api/<pk>', EmployeeUpdateAPIView.as_view(), name='employee-update'),
    path('employees-delete-api/<pk>', EmployeeDestroyAPIView.as_view(), name='employee-delete'),

    path('devices/', DeviceListCreateAPIView.as_view(), name='device-lc'),
    path('devices/<int:pk>/', DeviceetrieveUpdateDestroy.as_view(), name='device-rud'),

    path('provided-devices-list/', ProvidedDeviceListAPIView.as_view(), name='provided-device-l'),
    path('provided-devices-create/', ProvidedDeviceCreateAPIView.as_view(), name='provided-device-c'),
    path('provided-devices/<int:pk>/', ProvidedDevicerieveUpdateDestroy.as_view(), name='provideddevice-rud'),

]