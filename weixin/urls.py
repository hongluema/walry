#encoding: utf-8
from django.conf.urls import url
from . import views

app_name = "weixin"

urlpatterns = [
    url(r'^findTask/',views.find_task,name="findTask"),
    url(r'^deleteTask/',views.delete_task,name="deleteTask"),
]