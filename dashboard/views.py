import os
from django.shortcuts import render
from django.contrib.auth.models import User
from dashboard.models import Profile
from pprint import pprint
import json
from dashboard.forms import ProfileEditForm

# Get current user profile
def get_current_user(req):
    current_user = req.user
    user_profile = User.objects.get(username=current_user)
    return user_profile

# Dashboard
def index(request):
    return render(request, 'dashboard/dashboard.html')

# User profile
def profile(request):

    response_model = {
        'user': get_current_user(request),
        'base_url': 'http://127.0.0.1:8000'
    }

    return render(request, 'dashboard/user/profile.html', response_model)

# Edit user profile
def profile_edit(request):

    response_model = {
        'user': get_current_user(request),
        'countries':'',
        'timezones':'',
        'msg': ''
    }

    path = os.path.dirname(os.path.abspath(__file__))
    with open(os.path.join(path, 'static/dashboard/json/countries.json')) as countries:
        response_model['countries'] = json.load(countries)

    with open(os.path.join(path, 'static/dashboard/json/timezones.json')) as timezones:
        response_model['timezones'] = json.load(timezones)

    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = ProfileEditForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            data = form.cleaned_data
            print(data)
            response_model['msg'] = 'Profile Updated Successfully'
    else:
        form = ProfileEditForm()

    response_model['form'] = form

    return render(request, 'dashboard/user/profile_edit.html', response_model)
