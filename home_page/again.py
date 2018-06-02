# -*- coding: utf-8 -*-
import json

from django.http import HttpResponse

__author__ = 'hzl'
__date__ = '202018/5/21 19:43'

def again(data=None,static=200):
    result = {}
    if data:
        result.update(static=static,msg='success',data=data)
        return HttpResponse(json.dumps(result), content_type='Application/json')



