from django.conf.urls import include, url  
from django.contrib import admin
from . import views
from django.contrib.auth import views as auth_views

app_name = 'dashboard'
urlpatterns = [
    url(r'^$', views.dashboard),
    url(r'^dashboard/$', views.dashboard, name='dashboard'),
    url(r'^profile/$', views.profile, name='profile'),
    url(r'^logout/$', auth_views.logout, {'next_page': '/login'}, name='logout'),
]
