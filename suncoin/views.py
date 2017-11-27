from django.shortcuts import render, redirect
from django.http import HttpResponse
#from employee.models import UserProfile

def login(request):
    return render(request, 'suncoin/login.html')

def signup(request):

    if request.method == 'GET':
        if request.GET.get('ref') and request.GET['ref']:
            ref = request.GET['ref']
            print(ref)

    return render(request, 'suncoin/signup.html')

def forget_password(request):
    return render(request, 'suncoin/forget_password.html')