from django.shortcuts import render
import json

import simplejson as simplejson
from django.http import HttpResponse, JsonResponse
from common.models import User


def sign(request): #登录
    #print(request)
    #data = json.loads(request.body.decode(encoding="utf-8"))
    #data = simplejson.loads(request.bIDody.decode(encoding="utf-8"))
    #print(data)
    userId = request.GET.get('userid')
    passWord = request.GET.get('password')
    #userId = data["userid"]
    #data = simplejson.loads(request.body)
    #passWord = data['password']
    type = User.objects.values().filter(userid=userId,password=passWord)
    if type:
        return JsonResponse({'ret': 0})
    else:
        return JsonResponse({'ret': 1})
