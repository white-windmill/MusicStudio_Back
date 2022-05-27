import json

import simplejson as simplejson
from django.http import HttpResponse, JsonResponse
from django.core.files.base import ContentFile
from common.models import User
from common.models import PlayListCollection
from common.models import PlayList

def dispatcher(request):

    if request.method == 'GET':
        #request.params = request.GET
        return listuser(request)

    # elif request.method == 'POST':
    #     request.params = json.loads(request.body)
    #     return register(request)

    elif request.method == 'POST':
        
        return modifyuser(request)

    # elif request.method in ['POST', 'PUT', 'DELETE']:
    #     request.params = json.loads(request.body)

    else:
        return JsonResponse({'ret': 1, 'msg': 'error'})

def listuser(request):

    #userData = simplejson.loads(request.body.decode(encoding="utf-8"))
    userId =request.GET.get("userid")
    qs = User.objects.values()
    userCreatePlayListData = []
    userCollectPlayListData = []
    try:
        qs = qs.filter(userid=userId)
        data = list(qs)    #要包含创建的歌单和收藏的歌单两个的信息
        try :
            userCollectPlayList = list(PlayListCollection.objects.values("playlistname").filter(userid_id=userId).distinct())#收藏的歌单
            if userCollectPlayList:
                for j in userCollectPlayList:
                    playlistData=list(PlayList.objects.values("playlistimage").filter(playlistname=j["playlistname"]))
                    j.update(playlistData[0])
                    userCollectPlayListData.append(j)
        except:
            userCollectPlayListData = []
        try :
            userCreatePlayList = list(PlayList.objects.values("playlistname").filter(playlistfounder=userId).distinct())#创建的歌单
            if userCreatePlayList:
                for i in userCreatePlayList:
                    playlistData=list(PlayList.objects.values("playlistimage").filter(playlistname=i["playlistname"]))
                    i.update(playlistData[0])
                    userCreatePlayListData.append(i)
        except:
            userCreatePlayListData = []
        data[0].update({"usercollectdata": userCollectPlayListData})
        data[0].update({"usercreatedata": userCreatePlayListData})
        return JsonResponse({'ret': 0, 'data': data})
    except:
        return JsonResponse({'ret': 1})

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

    #userName = request.POST.get('username')
    # passWord = request.POST.get('password')
    #print(userName)
    global modifyUser
    #request_copy=request.body
    #testdata = json.loads(request.body)
    #file_content = ContentFile(request.FILES['img'].read())
    #print(request.FILES)
    #print(testdata)
    #request_params = json.dumps(response.renderer_context['request'].data)
    #print(request_params)
    try:
        img = request.FILES['userimage']
    except:
        img = "null"
    #print(img)
    #request.params = json.loads(request_copy)
    userName = request.POST.get('username')
    passWord = request.POST.get('password')
    information = request.POST.get('information')
    briefIntroduction = request.POST.get('introduce')
    userId = request.POST.get('userid')
    #print(userId)
    try:
        modifyUser = User.objects.get(userid=userId)
    except :
        User.objects.create(username=userName,password=passWord,userid=userId,userimage=img)
        userData = User.objects.get(userid=userId)
        PlayListCollection.objects.create(playlistname=userId + 'default', userid=userData)
        PlayList.objects.create(playlistname=userId + 'default',playlistfounder=userId,playlistimage='/img/1255.png')
        return JsonResponse({'ret': 0})

    if userName:
        modifyUser.username = userName
    if passWord:
        modifyUser.password = passWord
    if briefIntroduction:
        modifyUser.briefintroduction = briefIntroduction
    if information:
        modifyUser.information = information
    if img!="null":
        modifyUser.userimage=img    
    modifyUser.save()

    return JsonResponse({'ret': 0})
