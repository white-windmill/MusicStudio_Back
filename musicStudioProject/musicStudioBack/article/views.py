import json

import simplejson as simplejson
from django.http import HttpResponse, JsonResponse
from django.core import serializers
from common.models import Music
from common.models import PlayList
from common.models import User
from common.models import PlayListCollection
from common.models import Article
from common.models import Comment
def dispatcher(request):

    if request.method == 'POST':
        request.params = json.loads(request.body)
        return creatarticle(request)

    elif request.method == 'GET':
        return listarticle(request)

    elif request.method == 'PUT':
        request.params = json.loads(request.body)
        return changearticle(request)

    elif request.method == 'DELETE':
        request.params = json.loads(request.body)
        return delarticle(request)

    else:
        return JsonResponse({'ret': 1, 'msg': 'error'})

def listarticle(request):

    userData = simplejson.loads(request.body.decode(encoding="utf-8"))
    if userData:
        userId = userData["userid"]
        qs = Article.objects.values()
        qs = list(qs.filter(userid=userId))
        for i in qs:
            articleId = i['articleid']
            commentData = list(Comment.objects.values().filter(articleid=articleId))
            if commentData:
                for j in commentData:
                    commentUserData = list(User.objects.values().filter(userid=j['userid_id']))
                    j.update({"userdata": commentUserData[0]})
                i.update({"comment": commentData})
            else:
                i.update({"comment": []})

        data = list(qs)

    else:
        qs = list(Article.objects.values())
        for i in qs:
            articleId = i['articleid']
            commentData = list(Comment.objects.values().filter(articleid=articleId))
            if commentData:
                for j in commentData:
                    commentUserData =list(User.objects.values().filter(userid=j['userid_id']))
                    j.update({"userdata":commentUserData[0]})
                i.update({"comment":commentData})
            else:
                i.update({"comment":[]})

        data = list(qs)

    return JsonResponse({'ret': 0, 'data': data})
def creatarticle(request):

    userId = request.params['userid']
    userData = User.objects.get(userid=userId)
    articleContent = request.params['articlecontent']
    articleTime = request.params['articletime']
    articleId = userId + articleTime
    Article.objects.create(userid=userData,articlecontent=articleContent,
                           articletime=articleTime,articleid=articleId)
    return JsonResponse({'ret': 0})

def changearticle(request):

    articleId = request.params['articleid']
    articleData = Article.objects.get(articleid=articleId)
    articlelikeNum = articleData.articlelike + 1
    articleData.articlelike= articlelikeNum
    articleData.save()
    return JsonResponse({'ret': 0})

def delarticle(request):

    articleId = request.params['articleid']
    articleData = Article.objects.get(articleid=articleId)
    articleData.delete()

    return JsonResponse({'ret': 0})
