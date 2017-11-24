from django.conf.urls import include, url  
from django.contrib import admin
from . import views

app_name = 'suncoin'
urlpatterns = [
    url(r'^$', views.login ),
    url(r'^login$', views.login ),
    url(r'^signup$', views.signup ),
    url(r'^forget_password$', views.forget_password ),
    url(r'^user/', include('user.urls')),
    url(r'^admin/', admin.site.urls),
] 
