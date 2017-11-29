from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    email_confirmed = models.BooleanField(default=False)

    avatar = models.TextField(blank=True)
    fullname = models.CharField(max_length=100, blank=False)
    sponsor = models.CharField(max_length=100, blank=False)
    location = models.CharField(max_length=30, blank=True)
    continent = models.CharField(max_length=30, blank=True)
    country = models.CharField(max_length=30, blank=True)
    gender = models.CharField(max_length=30, blank=True)
    time_zone = models.CharField(max_length=30, blank=True)
    ip_address = models.CharField(max_length=30, blank=True)
    birth_date = models.DateField(null=True, blank=True)
    last_updated = models.DateField(null=True, blank=True)

@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)

@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
     instance.profile.save()