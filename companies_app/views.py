from django.shortcuts import render,redirect
from .forms import *
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from companies_app.decorators import *

# Create your views here.
@login_required
def home(request):
    companies = User.objects.filter(is_company=True)
    employees = Employee.objects.filter(company=request.user)

    context = {
       'companies':companies,
       'employees':employees,
    }
    return render(request, 'companies_app/home.html',context)

#Superuser Function

@login_required
@company_register_required
def companyregister(request):
    if request.method =='POST':
        form = CompanyRegisterForm(request.POST)
        if form.is_valid():
            first_name =form.cleaned_data.get('first_name')
            form.save()     
            messages.success(request,f'Account created for {first_name}')
            return redirect('/')
    else:
        form =CompanyRegisterForm()
    return render(request, 'companies_app/company-register.html',{'form':form})


@login_required
@company_register_required
def companyregisterupdate(request,pk):
    company = User.objects.get(pk=pk)
    if request.method =='POST':
        form = CompanyRegisterUpdateForm(request.POST,instance=company)
        if form.is_valid():
            form.save()     
            messages.success(request,f'Successfully Update')
            return redirect('/')
    else:
        form =CompanyRegisterUpdateForm(instance=company)
    return render(request, 'companies_app/company-register.html',{'form':form})

@login_required
@company_register_required
def delete_company(request,pk):
    company = User.objects.get(pk=pk)
    company.delete()
    messages.success(request,f'Successfully Delete')
    return redirect('/')


# Company all function

@login_required
@company_required
def employeeAdd(request):
    if request.method =='POST':
        form = EmployeeAddForm(request.POST, request.FILES)
        if form.is_valid():
            form.instance.company = request.user
            form.save()     
            messages.success(request,f'Successfully add new employee')
            return redirect('/')
    else:
        form =EmployeeAddForm()
    return render(request, 'companies_app/add-employee.html',{'form':form})
    
@login_required
@company_required
def employee_info_update(request,pk):
    employee = Employee.objects.get(pk=pk)
    if request.method =='POST':
        form = EmployeeAddForm(request.POST,request.FILES,instance=employee)
        if form.is_valid():
            form.instance.company = request.user
            form.save()     
            messages.success(request,f'Successfully Update')
            return redirect('/')
    else:
        form =EmployeeAddForm(instance=employee)
    return render(request, 'companies_app/add-employee.html',{'form':form})

@login_required
@company_required
def delete_employee(request,pk):
    employee = Employee.objects.get(pk=pk)
    employee.delete()
    messages.success(request,f'Successfully Delete')
    return redirect('/')

@login_required
def update_company_profile(request):
    if request.method == 'POST':
        form = UpdateCompaniesProfileForm(request.POST,
                                   request.FILES,
                                   instance=request.user.companiesprofile)
        if form.is_valid():
            form.save()
            messages.success(request, f'Profile has been updated!')
            return redirect('home')
    else:
        form = UpdateCompaniesProfileForm(instance=request.user.companiesprofile)

    context = {
        'form': form,
    }

    return render(request, 'companies_app/company-profile-update.html', context)



# Device all function

def device_list(request):
    device = Device.objects.filter(company=request.user)

    context = {
       'device':device,
    }
    return render(request, 'companies_app/device.html',context)


@login_required
@company_required
def deviceAdd(request):
    if request.method =='POST':
        form = DeviceAddForm(request.POST, request.FILES)
        if form.is_valid():
            form.instance.company = request.user
            form.save()     
            messages.success(request,f'Successfully add new Device')
            return redirect('device-list')
    else:
        form =DeviceAddForm()
    return render(request, 'companies_app/add-device.html',{'form':form})
    
@login_required
@company_required
def device_info_update(request,pk):
    device = Device.objects.get(pk=pk)
    if request.method =='POST':
        form = DeviceAddForm(request.POST,request.FILES,instance=device)
        if form.is_valid():
            form.instance.company = request.user
            form.save()     
            messages.success(request,f'Successfully Update')
            return redirect('device-list')
    else:
        form =DeviceAddForm(instance=device)
    return render(request, 'companies_app/add-device.html',{'form':form})

@login_required
@company_required
def delete_device(request,pk):
    device = Device.objects.get(pk=pk)
    device.delete()
    messages.success(request,f'Successfully Delete')
    return redirect('device-list')



# ProvidedDevice all function

def provided_device_list(request):
    provided_device = ProvidedDevice.objects.filter(company=request.user)

    context = {
       'provided_device':provided_device,
    }
    return render(request, 'companies_app/provided-device.html',context)


@login_required
@company_required
def providedeviceAdd(request):
    if request.method =='POST':
        form = ProvidedDeviceAddForm(request.POST, request.FILES)
        if form.is_valid():
            form.instance.company = request.user
            form.save()     
            messages.success(request,f'Successfully add new Device')
            return redirect('provided-device-list')
    else:
        form =ProvidedDeviceAddForm()
    return render(request, 'companies_app/add-provided-device.html',{'form':form})
    
@login_required
@company_required
def provided_device_info_update(request,pk):
    provided_device = ProvidedDevice.objects.get(pk=pk)
    if request.method =='POST':
        form = ProvidedDeviceAddForm(request.POST,request.FILES,instance=provided_device)
        if form.is_valid():
            form.instance.company = request.user
            form.save()     
            messages.success(request,f'Successfully Update')
            return redirect('provided-device-list')
    else:
        form = ProvidedDeviceAddForm(instance=provided_device)
    return render(request, 'companies_app/add-provided-device.html',{'form':form})

@login_required
@company_required
def delete_provided_device(request,pk):
    provided_device = ProvidedDevice.objects.get(pk=pk)
    provided_device.delete()
    messages.success(request,f'Successfully Delete')
    return redirect('provided-device-list')