import json

import simplejson as simplejson
from django.http import HttpResponse, JsonResponse

from common.models import User
from common.models import PlayListCollection
from common.models import PlayList

def dispatcher(request):

    if request.method == 'GET':
        #request.params = request.GET
        return listuser(request)

    elif request.method == 'POST':
        request.params = json.loads(request.body)
        return register(request)

    elif request.method == 'PUT':
        request.params = json.loads(request.body)
        return modifyuser(request)

    # elif request.method in ['POST', 'PUT', 'DELETE']:
    #     request.params = json.loads(request.body)

    else:
        return JsonResponse({'ret': 1, 'msg': 'error'})

def listuser(request):

    userData = simplejson.loads(request.body.decode(encoding="utf-8"))
    userId = userData["userid"]
    qs = User.objects.values()
    qs = qs.filter(userid=userId)
    data = list(qs)    #要包含创建的歌单和收藏的歌单两个的信息
    userCollectPlayList = list(PlayListCollection.objects.values("playlistname").filter(userid=userId))#收藏的歌单
    userCreatePlayList = list(PlayList.objects.values("playlistname").filter(playlistfounder=userId).distinct())#创建的歌单
    userCreatePlayListData = []
    userCollectPlayListData = []
    #该处最后还要添加歌单封面图片
    for i in userCreatePlayList:
        playlistData=list(PlayList.objects.values("playlistimage").filter(playlistname=i["playlistname"]))
        i.update(playlistData[0])
        userCreatePlayListData.append(i)
    for j in userCollectPlayList:
        playlistData=list(PlayList.objects.values("playlistimage").filter(playlistname=i["playlistname"]))
        j.update(playlistData[0])
        userCollectPlayListData.append(j)
    data[0].update({"usercollectdata": userCollectPlayListData})
    data[0].update({"usercreatedata": userCreatePlayListData})
    return JsonResponse({'ret': 0, 'data': data})

def register(request): #注册

    # userName = request.POST.get('username')
    # passWord = request.POST.get('password')
    userId = request.params['userid']
    userName = request.params['username']
    passWord = request.params['password']
    User.objects.create(username=userName,password=passWord,userid=userId)
    userData = User.objects.get(userid=userId)
    PlayListCollection.objects.create(playlistname=userId + 'default', userid=userData)
    return JsonResponse({'ret': 0})

def modifyuser(request): #修改

    # userName = request.POST.get('username')
    # passWord = request.POST.get('password')

    global modifyUser
    userName = request.params['username']
    passWord = request.params['password']
    information = request.params['information']
    briefIntroduction = request.params['introduce']
    # userimage = models.ImageField()用户头像
    userId = request.params['userid']

    try:
        modifyUser = User.objects.get(userid=userId)
    except modifyUser.DoesNotExist:
        return {
            'ret': 1,
            'msg': f'名称 为`{userName}`的客户不存在'
        }
    if userName:
        modifyUser.username = userName
    if passWord:
        modifyUser.password = passWord
    if briefIntroduction:
        modifyUser.briefintroduction = briefIntroduction
    if information:
        modifyUser.information = information
    #用户头像
    modifyUser.save()

    return JsonResponse({'ret': 0})
