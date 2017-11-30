from django import forms
from django.contrib.auth.models import User

class ProfileEditForm(forms.Form):
    current_password = forms.CharField(label='Current Password', max_length=100)
    new_password = forms.CharField(label='New Password', max_length=100)
    confirm_password = forms.CharField(label='Confirm Password', max_length=100)
    fullname = forms.CharField(label='Full Name', max_length=100)
    birth_date = forms.DateField(label='Date of Birth')
    continent = forms.CharField(label='Continent', max_length=30)
    country = forms.CharField(label='Country', max_length=100)
    location = forms.CharField(label='Address', max_length=256)
    sponsor = forms.CharField(label='Sponsor', max_length=100)
    gender = forms.CharField(label='Gender', max_length=30)
    time_zone = forms.CharField(label='Time Zone', max_length=100)