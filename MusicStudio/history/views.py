from django.shortcuts import render
import json

import simplejson as simplejson
from django.http import HttpResponse, JsonResponse
from common.models import History
from common.models import Music
from common.models import User

def dispatcher(request):

    if request.method == 'GET':
        return listhistory(request)

    elif request.method == 'POST':
        request.params = json.loads(request.body)
        return addhistory(request)

    else:
        return JsonResponse({'ret': 1, 'msg': 'error'})

def listhistory(request):

    #historyData = simplejson.loads(request.body.decode(encoding="utf-8"))
    userId = request.GET.get("userid")
    qs = History.objects.values()
    qs = qs.filter(userid=userId)
    data = list(qs)

    return JsonResponse({'ret': 0, 'data': data})

def addhistory(request):

    userId = request.params['userid']
    listenTime = request.params['listentime']
    musicId = request.params['musicid']
    perception = request.params['perception']
    musicName = request.params['musicname']
    musicSigner = request.params['musicsinger']
    musicAlbum = request.params['musicalbum']
    try:
        musicData = Music.objects.create(musicid=musicId,
                         musicname=musicName,
                         musicsinger=musicSigner,
                         musicalbum=musicAlbum,
                         )
    except:
        musicData = Music.objects.get(musicid=musicId,)
    musicId = Music.objects.get(musicid = musicId)
    userId = User.objects.get(userid = userId)
    History.objects.create(listentime = listenTime,
                        musicid = musicId,
                        perception = perception,
                        userid = userId,
                        )

    return JsonResponse({'ret': 0})


