#encoding: utf-8
from django.conf.urls import url
from . import views
from django.contrib.auth.views import logout, login, login_required

app_name = "face"

urlpatterns = [
    url(r'^cookieGet/$', views.cookie_get),#获取cookie
    url(r'^cookieSet/$', views.cookie_set),#设置cookie
    url(r'^login/$', login, name='login'),
    url(r'^logout/$', logout, name='logout'),
]