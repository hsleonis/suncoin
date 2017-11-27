from django.conf.urls import include, url  
from django.contrib import admin
from . import views
from django.contrib.auth import views as auth_views

app_name = 'suncoin'
urlpatterns = [
    url(r'^$', auth_views.login, {'template_name': 'suncoin/login.html'}, name='login'),
    url(r'^login/$', auth_views.login, {'template_name': 'suncoin/login.html'}, name='login'),
    url(r'^signup$', views.signup, name='signup' ),
    url(r'^forget_password$', views.forget_password ),
    url(r'^dashboard/', include('dashboard.urls')),
    url(r'^admin/', admin.site.urls),
] 
