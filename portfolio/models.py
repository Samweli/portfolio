from django.db import models
from django.contrib.auth.models import User
from django.contrib.gis.db import models as geomodels
from phone_field import PhoneField
from address.models import AddressField
from django.db.models.signals import post_save
from django.dispatch import receiver

# Models are created below here.

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    home_address = models.CharField(max_length=100)
    phone_number = PhoneField(null=True)
    location = geomodels.PointField( null=True)

# Adding create and save signals, so as Profile should 
# be automatically be created or updated when User is 
# created or updated

@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)

@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    instance.profile.save()