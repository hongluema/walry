#encoding: utf-8
from django.conf.urls import url
from . import views

app_name = "weixin"

urlpatterns = [
    url(r'^findTask/',views.find_task,name="findTask"),
    url(r'^deleteTask/',views.delete_task,name="deleteTask"),
    url(r'^recoverTask/',views.recover_task,name="recoverTask"),
    url(r'^showZuowei/',views.show_zuowei,name="show_zuowei"),#展示座位
]