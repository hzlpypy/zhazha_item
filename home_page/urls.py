# -*- coding: utf-8 -*-
from home_page import views

__author__ = 'hzl'
__date__ = '202018/5/19 15:31'
from django.conf.urls import url
urlpatterns = [
    url('head_infor',views.head_infor),
    url('catalog',views.catalog),
    url('search',views.search),
    url('shiyan',views.shiyan),
    url('info/',views.info),
    url('jump/',views.jump_htm),

]