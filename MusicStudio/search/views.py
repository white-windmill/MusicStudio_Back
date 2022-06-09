import json

import simplejson as simplejson
from django.http import HttpResponse, JsonResponse

from common.models import Music
from common.models import PlayList
from common.models import User
from common.models import PlayListCollection

def search(request):

    result_data = []
    sign=0
    sub=0
    data = request.GET.get('search')
    musicnamedata = list(Music.objects.filter(musicname__contains=data).values())
    musicsignerdata = list(Music.objects.filter(musicsinger__contains=data).values())
    #print(musicnamedata)
    #print(musicsignerdata)  
    if len(musicnamedata)!=0:   
        sign=1
        for i in range(len(musicnamedata)):
            musicnamedata[i].update({"sub":sub})
            sub+=1
            result_data.append(musicnamedata[i])
    if len(musicsignerdata)!=0:
        sign=1
        for i in range(len(musicsignerdata)):
            print(musicsignerdata[i])
            musicsignerdata[i].update({'sub':sub})
            sub+=1
            result_data.append(musicsignerdata[i])
    if sign!=0:
        return JsonResponse({'ret': 0,'data': result_data })
    else:
        return JsonResponse({'ret': 1,'msg': '没有符合条件的歌曲或者歌手' })

def searchplaylist(request):
    
    result_data = []
    sign=0
    data = request.GET.get('search')
    #musicnamedata = list(Music.objects.filter(musicname__contains=data).values())
    playlistdata = list(PlayList.objects.filter(playlistname__contains=data).values())
    #print(musicnamedata)
    #print(musicsignerdata)
    if len(playlistdata)!=0:
        sign=1
        
        result_data.append(playlistdata[0])
            
    #if len(musicsignerdata)!=0:
    #   sign=1
    #  for i in range(len(musicsignerdata)):
    #        result_data.append(musicsignerdata[i])
    if sign!=0:
        return JsonResponse({'ret': 0,'data': result_data })
    else:
        return JsonResponse({'ret': 1,'msg': '没有符合条件的歌单' })

    
