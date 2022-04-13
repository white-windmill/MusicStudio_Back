from django.shortcuts import render

# Create your views here.
import json

import simplejson as simplejson
from django.http import HttpResponse, JsonResponse

from common.models import User
from common.models import Article
from common.models import PlayList
from common.models import Music
from common.models import Comment

def dispatcher(request):

    if request.method == 'GET':
        #request.params = request.GET
        return listcomment(request)

    elif request.method == 'POST':
        request.params = json.loads(request.body)
        return postcomment(request)

    else:
        return JsonResponse({'ret': 1, 'msg': 'error'})

def listcomment(request):

    commentData = simplejson.loads(request.body.decode(encoding="utf-8"))
    playlistName = commentData[""]
    musicIdData = PlayList.objects.filter(playlistname=playlistName).values()
    data = list(musicIdData)
    print(data)
    musicData = []
    for i in data:
        musicId = i['musicid_id']
        musicData.append(list(Music.objects.filter(musicid=musicId).values())[0])
    return JsonResponse({'ret': 0, 'data': musicData})

def postcomment(request):

    userId = request.params['userid']
    articleId = request.params['articleid']
    commentContent = request.params['commentcontent']
    commentTime = request.params['commenttime']
    articleData = Article.objects.get(articleid=articleId)
    userData = User.objects.get(userid=userId)
    Comment.objects.create(userid=userData,articleid=articleData,
                           commentcontent=commentContent,commenttime=commentTime)
    articlecommentNum = articleData.articlecomment + 1
    articleData.articlecomment = articlecommentNum
    articleData.save()
    return JsonResponse({'ret': 0})
