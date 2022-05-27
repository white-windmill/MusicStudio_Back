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
        #request.params = json.loads(request.body)
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

    userId = request.GET.get("userid")
    qs = Article.objects.values()
    qs = list(qs.filter(userid=userId))
    try:
        for i in qs:
            articleId = i['articleid']
            userId = i['userid']
            articleUserData = list(User.objects.values().filter(userid=userId))
            commentData = list(Comment.objects.values().filter(articleid=articleId))
            if commentData:
                for j in commentData:
                    commentUserData = list(User.objects.values().filter(userid=j['userid_id']))
                    j.update({"userdata": commentUserData[0]})
                i.update({"comment": commentData})
            else:
                i.update({"comment": []})
        data = list(qs)
        return JsonResponse({'ret': 0, 'data': data})
    except:
        data = list(qs)
        return JsonResponse({'ret': 0, 'data': data})
    
def creatarticle(request):

    userId = request.POST.get('userid')
    userData = User.objects.get(userid=userId)
    articleContent = request.POST.get('articlecontent')
    articleTime =request.POST.get('articletime')
    articleId = userId + articleTime
    
    articlePic1 = request.FILES['articlepic1']
    print(articlePic1)
    articlePic2 = request.FILES['articlepic2']
    articlePic3 = request.FILES['articlepic3']  
    # articlePic1 = request.POST.get('articlepic1')
    # articlePic2 = request.POST.get('articlepic2')
    # articlePic3 = request.POST.get('articlepic3')
    Article.objects.create(userid=userData,articlecontent=articleContent,
                           articletime=articleTime,articleid=articleId,
                           articlepic1=articlePic1,
                           articlepic2=articlePic2,
                           articlepic3=articlePic3)
    return JsonResponse({'ret': 0})

def changearticle(request):

    articleId = request.params['articleid']
    articleData = Article.objects.get(articleid=articleId)
    articlelikeNum = articleData.articlelike + 1
    articleData.articlelike= articlelikeNum
    articleData.save()
    return JsonResponse({'ret': 0})

def increasearticle(request):
    
    request.params = json.loads(request.body)
    articleId = request.params['articleid']
    articleData = Article.objects.get(articleid=articleId)
    articlelikeNum = articleData.articlelike - 1
    articleData.articlelike= articlelikeNum
    articleData.save()
    return JsonResponse({'ret': 0})

def delarticle(request):

    articleId = request.params['articleid']
    articleData = Article.objects.get(articleid=articleId)
    articleData.delete()

    return JsonResponse({'ret': 0})

def getallarticle(request):
    qs = list(Article.objects.values())
    for i in qs:
        articleId = i['articleid']
        userId = i['userid_id']
        articleUserData = list(User.objects.values().filter(userid=userId))
        #print(articleUserData)
        i.update({"articleuserdata":articleUserData[0]})
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