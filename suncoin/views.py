from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.sites.shortcuts import get_current_site
from django.utils.encoding import force_bytes
from django.utils.http import urlsafe_base64_encode
from django.utils.http import urlsafe_base64_decode
from django.template.loader import render_to_string
from suncoin.forms import SignUpForm
from suncoin.tokens import account_activation_token
from django.contrib.auth import login
from django.contrib.auth.models import User
from django.utils.encoding import force_text
from django.core.mail import send_mail

# User Login
def login(request):
    return render(request, 'suncoin/login.html')

# User Signup
def signup(request):

    # Get sponsor
    if request.method == 'GET':
        if request.GET.get('ref') and request.GET['ref']:
            sponsor = request.GET['ref']

    if request.method == 'POST':
        form = SignUpForm(request.POST)

        if form.is_valid():
            user = form.save()
            user.refresh_from_db()  # load the profile instance created by the signal
            user.is_active = False
            user.save()

            current_site = get_current_site(request)
            subject = 'Activate Your Suncoin Account'
            message = render_to_string('suncoin/account_activation_email.html', {
                'user': user,
                'domain': current_site.domain,
                'uid': urlsafe_base64_encode(force_bytes(user.pk)),
                'token': account_activation_token.make_token(user),
            })
            print(message)

            send_mail(subject, message, 'noreply@suncoin.co', [user.email])
            return redirect('/login')
    else:
        form = SignUpForm()

    return render(request, 'suncoin/signup.html', {'form': form})

# Activate User
def activate(request, uidb64, token):
    try:
        uid = force_text(urlsafe_base64_decode(uidb64))
        user = User.objects.get(pk=uid)
    except (TypeError, ValueError, OverflowError, User.DoesNotExist):
        user = None

    if user is not None and account_activation_token.check_token(user, token):
        user.is_active = True
        user.profile.email_confirmed = True
        user.save()
        login(request, user)
        return redirect('/dashboard')
    else:
        return render(request, 'account_activation_invalid.html')

# Password Reset
def forget_password(request):
    return render(request, 'suncoin/forget_password.html')