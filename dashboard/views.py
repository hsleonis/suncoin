from django.shortcuts import render
from postgres import Postgres
from pprint import pprint

def database():
    db = Postgres("postgres://sun_admin@localhost/dsb_suncoin")
    return db


# Create your views here.
def dashboard(request):
    return render(request, 'dashboard/dashboard.html')

# User profile
def profile(request):
    current_user = request.user

    #db = database()
    #user = db.one("SELECT * FROM auth_users WHERE username='"+ current_user +"'")
    #pprint(user)

    response_model = {
        'username': current_user
    }

    return render(request, 'dashboard/profile.html', response_model)
