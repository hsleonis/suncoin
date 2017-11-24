from django.shortcuts import render, redirect
from django.http import HttpResponse
#from employee.models import UserProfile

def login(request):
    return render(request, 'suncoin/login.html')

def signup(request):
    return render(request, 'suncoin/signup.html')

def forget_password(request):
    return render(request, 'suncoin/forget_password.html')