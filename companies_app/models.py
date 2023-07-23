from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    is_company = models.BooleanField('is_company', default=True)

class CompaniesProfile(models.Model):
    company  = models.OneToOneField(User, on_delete=models.CASCADE, max_length=1)
    image    = models.ImageField(upload_to="profilepicture", default='no_profile.png')
    phone    = models.CharField(max_length=15,unique=True,blank=True,null=True)
    address  = models.CharField(max_length=100,blank=True,null=True)

    def __str__(self):
        return self.company.username


class Employee(models.Model):
    company   = models.ForeignKey(User,on_delete=models.CASCADE)
    name     = models.CharField(max_length = 150)
    image    = models.ImageField(upload_to="employeprofilepicture", default='no_img.png')
    phone    = models.CharField(max_length=15,unique=True)
    address  = models.CharField(max_length=200)

    def __str__(self):
        return self.name + self.phone


class Device(models.Model):
    company   = models.ForeignKey(User,on_delete=models.CASCADE)
    name     = models.CharField(max_length = 150)
    image    = models.ImageField(upload_to="Devicepicture", default='no_img.png')

    def __str__(self):
        return self.name


class ProvidedDevice(models.Model):
    company   = models.ForeignKey(User,on_delete=models.CASCADE)
    employee   = models.ForeignKey(Employee,on_delete=models.CASCADE)
    device   = models.ForeignKey(Device,on_delete=models.CASCADE)
    checkout_date = models.DateTimeField()
    return_date = models.DateTimeField(blank=True,null=True)

    def __str__(self):
        return self.device.name + ' / ' + self.employee.name

    