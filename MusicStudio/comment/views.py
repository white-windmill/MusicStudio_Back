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
    
    articleId = request.GET.get('articleid')
    data=[]
    commentData = list(Comment.objects.values().filter(articleid=articleId))
    if commentData:
        for j in commentData:
            commentUserData = list(User.objects.values().filter(userid=j['userid_id']))
            j.update({"userdata": commentUserData[0]})
        data.append({"comment": commentData})
    else:
        data.append({"comment": []})
    return JsonResponse({'ret': 0, 'data': data})

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
