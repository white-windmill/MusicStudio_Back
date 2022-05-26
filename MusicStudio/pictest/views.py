
from django.shortcuts import render

# Create your views here.
import json

import simplejson as simplejson
from django.http import HttpResponse, JsonResponse
from django.core.files.base import ContentFile
from common.models import User
from common.models import PlayList
from common.models import Music
from common.models import PlayListCollection
from common.models import ImageTest

def dispatcher(request):

    if request.method == 'GET':
        return getimg(request)

    elif request.method == 'POST':
        #request.params = json.loads(request.body)
        return postimg(request)

def getimg(request):

    imgs = ImageTest.objects.all()
    for i in imgs:
        x=i.image1
        y=str(x)
    print(y)
    z="1.1.PNG"
    img_url='http://124.220.169.238:8000/media/img/'+z
    return JsonResponse({'ret': 0,'img':img_url})

def postimg(request):

    img = request.FILES['img']
    url = 'http://124.220.169.238:8000/media/img/'+str(img)
    img = ImageTest(image1=request.FILES['img'])
    img.save()
    return JsonResponse({'ret': 0,'data':url})
