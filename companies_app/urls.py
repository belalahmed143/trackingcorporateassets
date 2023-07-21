from django.urls import path
from .views import *
from django.contrib.auth import views as auth_views
from companies_app import views as user_views

urlpatterns = [
    path('', home, name='home'),

    path("acompany-registration", companyregister, name="company-register"),
    path('company-registration-update/<pk>',companyregisterupdate,name='company-register-update'),
    path('delete-company/<pk>', delete_company, name='delete-company'),
    

    path('add-new-employee', employeeAdd, name='employee-add'),
    path('employee-info-update/<pk>',employee_info_update,name='employee-info-update'),
    path('delete-employee/<pk>', delete_employee, name='delete-employee'),
    
    path('device-list', device_list, name='device-list'),
    path('add-new-device', deviceAdd, name='device-add'),
    path('device-info-update/<pk>',device_info_update,name='device-info-update'),
    path('delete-device/<pk>', delete_device, name='delete-device'),
    

    path('provided-device-list', provided_device_list, name='provided-device-list'),
    path('device-checkout', providedeviceAdd, name='device-checkout'),
    path('provided-device-info-update/<pk>',provided_device_info_update,name='provided-device-info-update'),
    path('delete-provided-device/<pk>', delete_provided_device, name='delete-provided-device'),
    
    path('company/profile/update', user_views.update_company_profile, name='update-company-profile'),
    path('login/', auth_views.LoginView.as_view(template_name='companies_app/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(template_name='companies_app/logout.html'), name='logout'),
    
]   