from django.db.models.signals import post_save
from .models import User
from django.dispatch import receiver
from .models import CompaniesProfile


@receiver(post_save, sender=User)
def create_companiesprofile(sender, instance, created, **kwargs):
    if created:
        CompaniesProfile.objects.create(company=instance)

@receiver(post_save, sender=User)
def save_companiesprofile(sender, instance, **kwargs):
    instance.companiesprofile.save()
