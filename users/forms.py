#! /usr/bin/env python
# -*- coding:utf-8 -*-
from django import forms
from django.contrib.auth.models import User

class UserRegistrationForm(forms.ModelForm):
    password = forms.CharField(label="密码",widget=forms.PasswordInput,max_length=16)
    password2 = forms.CharField(label="确认密码",widget=forms.PasswordInput,max_length=16)

    class Meta:
        model = User
        fields = ('username','email')

    def clean_password2(self): #固定格式，对一个表单某一个数据字段检验必须使用clean_开头加上该字段为函数名，如果有两个字段需要验证可以使用两个这样的函数
        cd = self.cleaned_data #这个也是固定的
        if cd["password"] != cd["passwords"]:
            raise forms.ValidationError("密码不匹配")
        return cd["password2"] #返回值也是固定的

class LoginForm(forms.Form):
    username = forms.CharField(label="用户名", required=False)
    password = forms.CharField(widget=forms.PasswordInput, label="密码", required=False)

    def clean(self):#固定格式，对一个表单多个数据字段检验使用clean函数
        cleaned_data = super(LoginForm, self).clean() #这个也是固定的，要继承
        username = cleaned_data.get('username', '')
        password = cleaned_data.get('password', '')
        if username == '' or password == '':
            raise forms.ValidationError('用户名或密码为空')

        count = User.objects.filter(username=username, password=password).count()
        if count == 0:
            raise forms.ValidationError("用户名或密码错误")
        # try:
        #     models.User2.objects.get(username=username, password=password)
        # except ObjectDoesNotExist as e:
        #     raise forms.ValidationError("用户名或密码错误")
        return cleaned_data #这个也是固定的

