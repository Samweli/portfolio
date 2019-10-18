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
from .forms import UserForm, ProfileForm
from .models import Profile
from .serializers import CustomSerializer

# Create your views here.

@login_required
@transaction.atomic
def update_profile(request):
    if request.method == 'POST':
        user_form = UserForm(request.POST, instance=request.user)
        profile_form = ProfileForm(request.POST, instance=request.user.profile)
        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            profile_form.save()
            messages.success(request, _('Your profile was successfully updated!'))
            return redirect('update_profile')
        else:
            messages.error(request, _('Please correct the error below.'))
    else:
        user_form = UserForm(instance=request.user)
        profile_form = ProfileForm(instance=request.user.profile)
    return render(request, 'profile/profile.html', {
        'user_form': user_form,
        'profile_form': profile_form
    })

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