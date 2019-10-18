from django.shortcuts import render
from django.views import generic
from django.contrib.gis.geos import fromstr
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.db import transaction
from django.core.serializers import serialize
from django.contrib import messages
from django.utils.translation import gettext as _
from django.shortcuts import redirect
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm
from .forms import UserForm, ProfileForm, SignUpForm
from .models import Profile
from .serializers import CustomSerializer


# This will make it simple to edit both User and Profile
# at once, due to the way the Profile class has been
# extended from Django User class


@login_required
@transaction.atomic
def update_profile(request):
    if request.method == 'POST':
        user_form = UserForm(
            request.POST,
            instance=request.user)
        profile_form = ProfileForm(
            request.POST,
            instance=request.user.profile)
        if user_form.is_valid() and \
         profile_form.is_valid():
            user_form.save()
            profile_form.save()
            messages.success(
                request,
                _('Your profile was successfully updated!'))
            return redirect('update_profile')
        else:
            messages.error(
                request,
                _('Please correct the error below.'))
    else:
        user_form = UserForm(
            instance=request.user)
        profile_form = ProfileForm(
            instance=request.user.profile)
    return render(
        request, 
        'profile/profile.html', {
        'user_form': user_form,
        'profile_form': profile_form
    })

def signup(request):
    if request.method == 'POST':
        user_form = SignUpForm(request.POST)
        profile_form = ProfileForm(request.POST)
        if user_form.is_valid() and\
         profile_form.is_valid():
            user = user_form.save()      
            user.refresh_from_db()

            user.profile.home_address =\
             profile_form.cleaned_data.get(
                'home_address')
            user.profile.phone_number = \
            profile_form.cleaned_data.get(
                'phone_number') 
            user.profile.location = \
            profile_form.cleaned_data.get(
                'location')  
            user.save()

            username = user_form.\
            cleaned_data.get('username')
            raw_password = user_form.\
            cleaned_data.get('password1')

            user = authenticate(
                username=username,
                password=raw_password)

            messages.success(
                request,
                _('Your account was successfully created!'))

            login(request, user)

            return redirect('user_list')
        else:
            messages.error(
                request,
                _('Please correct the error below.'))
    else:
        user_form = SignUpForm()
        profile_form = ProfileForm()
    return render(request, 'registration/signup.html', 
        {'user_form': user_form,
        'profile_form': profile_form}
        )


def user_list(request):

    serializers = CustomSerializer()
    users = serializers.serialize(
     Profile.objects.all().select_related('user'),
     geometry_field='location', 
     fields=('user__first_name','user__last_name',
        'home_address','phone_number'))

    return render(request, 
        'profile/index.html',
        {'users': users})