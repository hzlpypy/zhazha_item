# -*- coding: utf-8 -*-
from register import views

__author__ = 'hzl'
__date__ = '202018/5/19 10:59'
from django.conf.urls import url

urlpatterns = [
    url('login/',views.login),
    url('index/',views.index),
    url('register/',views.register),
    url('forget/',views.forget_pwd),
]