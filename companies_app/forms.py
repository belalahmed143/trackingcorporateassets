from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import *

class CompanyRegisterForm(UserCreationForm):
    first_name = forms.CharField(max_length=30,label='Company Name',
            )
    class Meta:
        model = User
        fields =['username', 'first_name', 'email']

class CompanyRegisterUpdateForm(forms.ModelForm):
    first_name = forms.CharField(max_length=30,label='Company Name',
            )
    class Meta:
        model = User
        fields =['username', 'first_name', 'email','is_active','is_company']

class UpdateCompaniesProfileForm(forms.ModelForm):
    class Meta:
        model = CompaniesProfile
        fields = '__all__'
        exclude = ('company',)
    
    
class EmployeeAddForm(forms.ModelForm):
    class Meta:
        model= Employee
        fields = '__all__'
        exclude = ('company',)
        
class DeviceAddForm(forms.ModelForm):
    class Meta:
        model= Device
        fields = '__all__'
        exclude = ('company',)

class ProvidedDeviceAddForm(forms.ModelForm):
    checkout_date = forms.DateTimeField(required=True,
                                     widget=forms.DateTimeInput(attrs={'type':'datetime-local'}))
    return_date = forms.DateTimeField(required=False,
                                          widget=forms.DateTimeInput(attrs={'type':'datetime-local'}))

    class Meta:
        model= ProvidedDevice
        fields = '__all__'
        exclude = ('company',)