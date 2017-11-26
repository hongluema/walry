#encoding: utf-8
from django.conf.urls import url
from . import views

app_name = "bus"

urlpatterns = [
    url(r'^addRun/$', views.AddRunLoggingView.as_view()),#添加运营记录
    url(r'^showRun/$', views.ShowView.as_view()),#展示运营记录
]