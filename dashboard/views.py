from django.shortcuts import render
from django.contrib.auth.models import User
from dashboard.models import Profile
from pprint import pprint

# Dashboard
def index(request):
    return render(request, 'dashboard/dashboard.html')

# User profile
def profile(request):
    current_user = request.user
    user_profile = User.objects.get(username=current_user)

    response_model = {
        'user': user_profile,
        'base_url': 'http://127.0.0.1:8000'
    }

    return render(request, 'dashboard/profile.html', response_model)
