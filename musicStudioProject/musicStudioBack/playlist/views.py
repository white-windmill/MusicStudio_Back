from django.shortcuts import render

# Create your views here.
import json

import simplejson as simplejson
from django.http import HttpResponse, JsonResponse

from common.models import User
from common.models import PlayList
from common.models import Music
from common.models import PlayListCollection

def dispatcher(request):

    if request.method == 'GET':
        #request.params = request.GET
        return listplaylist(request)

    elif request.method == 'POST':
        request.params = json.loads(request.body)
        return collectplaylist(request)

    elif request.method == 'DELETE':
        request.params = json.loads(request.body)
        return nocollectplaylist(request)
    else:
        return JsonResponse({'ret': 1, 'msg': 'error'})

def listplaylist(request):

    playlistData = simplejson.loads(request.body.decode(encoding="utf-8"))
    playlistName = playlistData["playlistname"]
    musicIdData = PlayList.objects.filter(playlistname=playlistName).values()
    data = list(musicIdData)
    print(data)
    musicData = []
    for i in data:
        musicId = i['musicid_id']
        musicData.append(list(Music.objects.filter(musicid=musicId).values())[0])
    return JsonResponse({'ret': 0, 'data': musicData})

def collectplaylist(request):

    userId = request.params['userid']
    playListName = request.params['playlistname']
    userData = User.objects.get(userid=userId) #防止歌单重复收藏
    try :
        PlayListCollection.objects.get(userid=userData,playlistname=playListName)
    except :
        PlayListCollection.objects.create(userid=userData, playlistname=playListName)
        return JsonResponse({
            'ret': 0
        })
    return JsonResponse({'ret': 1,'msg':'您已经收藏过该歌单了，请不要重复收藏'})

def nocollectplaylist(request):

    userId = request.params['userid']
    playListName = request.params['playlistname']
    userData = User.objects.get(userid=userId)
    playListCollectionData = PlayListCollection.objects.get(playlistname = playListName,userid = userId,)
    playListCollectionData.delete()

    return JsonResponse({'ret': 0})
