from datetime import timedelta
from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name="profile")
    first_name = models.CharField(null=True, blank=True, max_length=50)
    last_name = models.CharField(null=True, blank=True, max_length=50)
    weight = models.FloatField(null=True, blank=True)
    height = models.FloatField(null=True, blank=True)
    region = models.CharField(null=True, blank=True, max_length=100)
    province = models.CharField(null=True, blank=True, max_length=100)
    municipality = models.CharField(null=True, blank=True, max_length=100)
    blood_type = models.CharField(null=True, blank=True, max_length=3)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    availability = models.BooleanField(default=True)
    last_donation_date = models.DateField(null=True, blank=True)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"
    
    def can_be_available(self):
        if self.last_donation_date:
            return timezone.now().date() >= self.last_donation_date + timedelta(days=56)
        return True