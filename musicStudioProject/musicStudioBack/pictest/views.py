
from django.shortcuts import render

# Create your views here.
import json

import simplejson as simplejson
from django.http import HttpResponse, JsonResponse

from common.models import User
from common.models import PlayList
from common.models import Music
from common.models import PlayListCollection
from common.models import ImageTest

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

    # img = ImageTest(img1=request.FILES.get('img'))
    # img.save()
    # return JsonResponse({'ret': 0})
    imgs = ImageTest.objects.all()  # 从数据库中取出所有的图片路径
    for i in imgs:
        print(i.image1)
    return JsonResponse({'ret': 1})

def collectplaylist(request):
    imgs = ImageTest.objects.all()  # 从数据库中取出所有的图片路径
    context = {
        'imgs': imgs
    }
    print(imgs)
    return JsonResponse({'ret': 1,'msg':'您已经收藏过该歌单了，请不要重复收藏'})

def nocollectplaylist(request):

    userId = request.params['userid']
    playListName = request.params['playlistname']
    userData = User.objects.get(userid=userId)
    playListCollectionData = PlayListCollection.objects.get(playlistname = playListName,userid = userId,)
    playListCollectionData.delete()

    return JsonResponse({'ret': 0})