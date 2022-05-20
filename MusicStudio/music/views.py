import json

import simplejson as simplejson
from django.http import HttpResponse, JsonResponse

from common.models import Music
from common.models import PlayList
from common.models import User
from common.models import PlayListCollection

def dispatcher(request):

    if request.method == 'POST':
        request.params = json.loads(request.body)
        return collectmusic(request)

    elif request.method == 'DELETE':
        request.params = json.loads(request.body)
        return nocollectmusic(request)

    else:
        return JsonResponse({'ret': 1, 'msg': 'error'})

def collectmusic(request): #收藏歌曲

    userId = request.params['userid']
    playlistName = request.params['playlistname']
    musicId = request.params['musicid']
    musicName = request.params['musicname']
    musicSigner = request.params['musicsinger']
    musicAlbym = request.params['musicalbum']
    try :
        Music.objects.get(musicid=musicId)
    except :
        Music.objects.create(musicid=musicId, musicname=musicName, musicsinger=musicSigner
                                         ,musicalbum=musicAlbym)
    musicData = Music.objects.get(musicid=musicId)
    #print(musicData)
    try :
        PlayList.objects.get(musicid=musicId,playlistname=playlistName,playlistfounder=userId)
    except :
        PlayList.objects.create(musicid=musicData, playlistname=playlistName, playlistfounder=userId)
        return JsonResponse({
            'ret': 0
})
    return JsonResponse({'ret': 1,'msg': '该歌曲已经在当前歌单里了'})

def nocollectmusic(request): #取消收藏

    musicId = request.params['musicid']
    playlistName = request.params['playlistname']
    try:
        PlayListData = PlayList.objects.get(playlistname = playlistName,musicid = musicId)
        PlayListData.delete()
        return JsonResponse({'ret': 0})
    except:
        return JsonResponse({'ret': 1,'data':'已经取消收藏'})       

def rank(request):

    qs =list(Music.objects.values())
    data=[]
    for i in range(10):
        data.append(qs[i])
    return JsonResponse({'ret': 0,"data":data})



    