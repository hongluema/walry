#encoding: utf-8
from django.conf.urls import url
from . import views

app_name = "weixin"

urlpatterns = [
    url(r'^findTask/',views.find_task,name="findTask"),
    url(r'^deleteTask/',views.delete_task,name="deleteTask"),
    url(r'^recoverTask/',views.recover_task,name="recoverTask"),
    url(r'^showuowei/',views.show_zuowei,name="show_zuowei"),#展示座位
    url(r'^createLog/',views.create_log,name="create_log"),#创建车辆运营记录
]