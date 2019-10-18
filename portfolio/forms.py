from django import forms
from .models import Profile
from django.contrib.auth.models import User
from django.contrib.gis import forms as geoforms
from django.contrib.auth.forms import UserCreationForm
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

class SignUpForm(UserCreationForm):
    first_name = forms.CharField(
    	max_length=30,
    	required=False, 
    	help_text='Optional.')
    last_name = forms.CharField(
    	max_length=30,
    	required=False,
    	help_text='Optional.')
    email = forms.EmailField(
    	max_length=254, 
    	help_text='Required. Inform a valid email address.')

    class Meta:
        model = User
        fields = (
        	'username', 
        	'first_name', 
        	'last_name', 
        	'email', 
        	'password1',
        	'password2', )