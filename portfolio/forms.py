from django import forms
from .models import Profile
from django.contrib.auth.models import User
from django.contrib.gis.db import models as geomodels


class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'email')

class ProfileForm(forms.ModelForm):
	location = geomodels.PointField()
	class Meta:
		model = Profile
		fields = ('home_address', 'phone_number', 'location')