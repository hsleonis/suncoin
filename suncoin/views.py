from django.shortcuts import render, redirect
from django.http import HttpRequest
from django.contrib.sites.shortcuts import get_current_site
from django.utils.encoding import force_bytes
from django.utils.http import urlsafe_base64_encode
from django.utils.http import urlsafe_base64_decode
from django.template.loader import render_to_string
from suncoin.forms import SignUpForm
from suncoin.tokens import account_activation_token
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User
from django.utils.encoding import force_text
from django.core.mail import send_mail

# User Login
def login(request, msg=''):
    return render(request, 'suncoin/login.html', {'msg': msg})

# User Signup
def signup(request):

    response_model = {
        'success': True,
        'msg': '',
        'sponsor': ''
    }

    # Get sponsor
    if request.method == 'GET':
        if request.GET.get('ref') and request.GET['ref']:
            response_model['sponsor'] = request.GET['ref']

    if request.method == 'POST':
        form = SignUpForm(request.POST)

        if form.is_valid():
            user = form.save()

            user.refresh_from_db()
            user.is_active = False
            user.sponsor = request.POST['sponsor']
            user.save()

            current_site = get_current_site(request)
            subject = 'Activate Your Suncoin Account'
            message = render_to_string('suncoin/account_activation_email.html', {
                'user': user,
                'domain': current_site.domain,
                'uid': urlsafe_base64_encode(force_bytes(user.pk)),
                'token': account_activation_token.make_token(user),
            })

            ret = send_mail(subject, message, 'noreply@suncoin.co', [user.email], fail_silently=False)

            response_model['msg'] = 'Please check your email to activate account'
    else:
        form = SignUpForm()

    # pass signup form
    response_model['form'] = form

    return render(request, 'suncoin/signup.html', response_model)

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
        user.profile.ip_address = request.META['REMOTE_ADDR']
        user.save()
        #login(request, user)
        return redirect('/login', msg='Account activated. Please Login.')
    else:
        return redirect('/login', msg='Account already activated.')

# Password Reset
def forget_password(request):
    return render(request, 'suncoin/password_reset_form.html')