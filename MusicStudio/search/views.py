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
    data = request.GET.get('search')
    musicnamedata = list(Music.objects.filter(musicname__contains=data,musicsinger__contains=data).values())
    musicsignerdata = list(Music.objects.filter(musicsinger__contains=data).values())
    if len(musicnamedata)!=0:   
        sign=1
        for i in range(len(musicnamedata)):
            result_data.append(musicnamedata[i])
    if len(musicsignerdata)!=0:
        sign=1
        for i in range(len(musicsignerdata)):
            result_data.append(musicsignerdata[i])
    if sign!=0:
        return JsonResponse({'ret': 0,'data': result_data })
    else:
        return JsonResponse({'ret': 1,'msg': '没有符合条件的歌曲或者歌手' })


    