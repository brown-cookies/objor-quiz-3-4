from .models import Profile
from datetime import timedelta
from django import forms
from django.utils import timezone

class ProfileUpdateForm(forms.ModelForm):
    class Meta:
        model = Profile
        exclude = ['user']

    def clean_availability(self):
        availability = self.cleaned_data.get('availability')
        last_donation_date = self.cleaned_data.get('last_donation_date')

        # Check if availability is set to True and last donation is within 56 days
        if availability and last_donation_date:
            days_since_donation = (timezone.now().date() - last_donation_date).days
            if days_since_donation < 56:
                raise forms.ValidationError(f"Cannot be available for donation. Only {days_since_donation} days have passed since your last donation.")
        return availability
