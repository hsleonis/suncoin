from django.conf.urls import include, url  
from django.contrib import admin
from . import views
from django.contrib.auth import views as auth_views

app_name = 'suncoin'
urlpatterns = [
    url(r'^$', auth_views.login, {'template_name': 'suncoin/login.html'}, name='login'),
    url(r'^login/$', auth_views.login, {'template_name': 'suncoin/login.html'}, name='login'),
    url(r'^signup$', views.signup, name='signup' ),
    url(r'^activate/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/$', views.activate, name='activate'),
    url(r'^dashboard/', include('dashboard.urls')),
    url(r'^admin/', admin.site.urls),

    url(r'^password_reset/$', auth_views.password_reset, {'template_name': 'suncoin/registration/password_reset_form.html'}, name='password_reset'),
    url(r'^password_reset/done/$', auth_views.password_reset_done, {'template_name': 'suncoin/registration/password_reset_done.html'}, name='password_reset_done'),
    url(r'^reset/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/$',
        auth_views.password_reset_confirm, {'template_name': 'suncoin/registration/password_reset_confirm.html'}, name='password_reset_confirm'),
    url(r'^reset/done/$', auth_views.password_reset_complete, {'template_name': 'suncoin/registration/password_reset_complete.html'}, name='password_reset_complete'),
]