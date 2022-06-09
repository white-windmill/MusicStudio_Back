from django.shortcuts import render

# Create your views here.
import json

import simplejson as simplejson
from django.http import HttpResponse, JsonResponse

from common.models import User
from common.models import PlayList
from common.models import Music
from common.models import PlayListCollection
from django.http import HttpResponse

def listorders(request):
    return HttpResponse("下面是系统中所有的订单信息。。。")

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

    #playlistData = simplejson.loads(request.body.decode(encoding="utf-8"))
    playlistName = request.GET.get("playlistname")
    musicIdData = PlayList.objects.filter(playlistname=playlistName).values()
    if musicIdData:
        data = list(musicIdData)
        musicData = []
        s=0
        for i in data:
            musicId = i['musicid_id']
            print(musicId)
            if musicId != '-1':
    # qs =list(Music.objects.values())
    # data=[]
    # s=0
    # print(qs)
    # for i in range(5):
    #     if qs[i]['musicid']!='-1':
    #         qs[i].update({"sub":s})
    #         data.append(qs[i])
    #         s+=1
                qs = list(Music.objects.filter(musicid=musicId).values())[0]
                #print(qs)
                qs.update({"sub":s})
                #print(qs)
                musicData.append(qs)
                s+=1
        return JsonResponse({'ret': 0, 'data': musicData})
    else:
        return JsonResponse({'ret': 1})

def collectplaylist(request):

    userId = request.params['userid']
    playListName = request.params['playlistname']
    userData = User.objects.get(userid=userId) #防止歌单重复收藏
    try :
        data=PlayListCollection.objects.get(userid=userData,playlistname=playListName)
    except :
        PlayListCollection.objects.create(userid=userData, playlistname=playListName)
        return JsonResponse({'ret': 0})
    return JsonResponse({'ret': 1,'msg':'您已经收藏过该歌单了，请不要重复收藏'})

def nocollectplaylist(request):

    userId = request.params['userid']
    playListName = request.params['playlistname']
    #musicId = request.params['musicid']
    
    userData = User.objects.get(userid=userId)
    try:
      playListCollectionData = PlayListCollection.objects.get(playlistname = playListName,userid = userId,)
      playListCollectionData.delete()
    # playListData = PlayList.objects.get(playlistname = playListName,musicid = musicId)
    # playListData.delete()
    except:
      return JsonResponse({'ret':1,'data':'您还未收藏该歌单!'})
    return JsonResponse({'ret': 0})

def rank(request):

    playlistData = list(PlayList.objects.values())
    s=len(playlistData)
    data=[]
    sign=0
    for i in range(s):
        if data :
            for j in data:
                if j['playlistname']==playlistData[i]['playlistname']:
                    sign=1
                if playlistData[i]['playlistname'][-7:-1]=='defaul':
                    sign=1
                print(playlistData[i]['playlistname'][-7:-1])
            if sign==0:
                data.append(playlistData[i])
        else:    
            if playlistData[i]['playlistname'][-7:-1]!='defaul':
                data.append(playlistData[i])
        sign=0
    fristimg=playlistData[0]['playlistimage']
    return JsonResponse({'ret': 0,"data":data})

def testret(request):

    userId = request.GET.get('userid')
    playListName = request.GET.get('playlistname')
    #print(userId)
    try :
        userData = User.objects.get(userid=userId) #防止歌单重复收藏
        data=PlayListCollection.objects.get(userid=userData,playlistname=playListName)
        return JsonResponse({'ret': 1})
    except :
        #PlayListCollection.objects.create(userid=userData, playlistname=playListName)
        return JsonResponse({'ret': 0})
    
def creatplaylist(request):

    playlistName = request.POST.get('playlistname')
    playlistFounder = request.POST.get('userid')
#    img = request.FILES['playlistimage']
    musicData = Music.objects.get(musicid=-1)
    s=PlayList.objects.create(playlistimage='/img/777.jpg',playlistfounder=playlistFounder,playlistname=playlistName,
    musicid =musicData)
    return JsonResponse({'ret': 0})

def delplaylist(request):
    request.params = json.loads(request.body)
    userId = request.params['userid']
    playListName = request.params['playlistname']
    #musicId = request.params['musicid']

    userData = User.objects.get(userid=userId)
    try:
      playListData = PlayList.objects.get(playlistname = playListName,playlistfounder = userId,)
      playListData.delete()
    # playListData = PlayList.objects.get(playlistname = playListName,musicid = musicId)
    # playListData.delete()
    except:
      return JsonResponse({'ret':1,'data':'不是您创建的歌单！'})
    return JsonResponse({'ret': 0})
