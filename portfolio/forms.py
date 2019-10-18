from django import forms
from .models import Profile
from django.contrib.auth.models import User
from django.contrib.gis import forms as geoforms
from leaflet.forms.widgets import LeafletWidget


class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'email')

class ProfileForm(forms.ModelForm):
	class Meta:
		model = Profile
		fields = ('home_address', 'phone_number', 'location')
		widgets = {'location': LeafletWidget()}