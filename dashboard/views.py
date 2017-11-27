from django.shortcuts import render
from postgres import Postgres
from pprint import pprint


# Create your views here.
def index(request):
    return render(request, 'dashboard/dashboard.html')

# User profile
def profile(request):
    current_user = request.user

    response_model = {
        'username': current_user,
        'base_url': 'http://127.0.0.1:8000'
    }

    return render(request, 'dashboard/profile.html', response_model)
