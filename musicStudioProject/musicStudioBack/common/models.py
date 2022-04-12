from django.db import models

# Create your models here.
from django.db import models
from django.db.models import DO_NOTHING


class User(models.Model):

    username = models.CharField(max_length=200)
    password = models.CharField(max_length=200)
    userid = models.CharField(max_length=200,primary_key=True)
    information = models.CharField(max_length=200,default='周杰伦')
    briefintroduction = models.CharField(max_length=200,default='这个人很懒，什么都没有留下')
    #userimage = models.ImageField()用户头像

class Music(models.Model):

    musicid = models.CharField(max_length=200,primary_key=True)
    musicname = models.CharField(max_length=200)
    musicsinger = models.CharField(max_length=200)
    musicalbum = models.CharField(max_length=200)#该歌曲所属专辑

class PlayList(models.Model):

    playlistname = models.CharField(max_length=200)
    musicid = models.ForeignKey(Music,on_delete=DO_NOTHING)
    # playlistcover = models.ImageField()歌单封面
    playlistfounder = models.CharField(default="default",max_length=200)#如果为默认值则表示该歌单是默认歌单，不是用户创建歌单

class History(models.Model):

    listentime = models.DateTimeField()
    musicid = models.ForeignKey(Music,on_delete=DO_NOTHING)
    perception = models.CharField(max_length=200)
    userid = models.ForeignKey(User,on_delete=DO_NOTHING)

class Article(models.Model):

    articleid = models.CharField(max_length=200,primary_key=True)
    articlecontent = models.CharField(max_length=200)
    articlelike = models.IntegerField(default=0)#点赞数
    articlecomment = models.IntegerField(default=0)#评论数
    articletime = models.DateTimeField(default=0) #发帖时间
    # articlepic1 = models.ImageField()
    # articlepic2 = models.ImageField()
    # articlepic3 = models.ImageField()
    userid = models.ForeignKey(User,on_delete=DO_NOTHING)

class Comment(models.Model):

    commenttime = models.DateTimeField()
    articleid = models.ForeignKey(Article,on_delete=DO_NOTHING)
    userid = models.ForeignKey(User,on_delete=DO_NOTHING)
    commentcontent = models.CharField(max_length=200)


class MusicCollection(models.Model):

    userid = models.ForeignKey(User,on_delete=DO_NOTHING)
    musicid = models.ForeignKey(Music,on_delete=DO_NOTHING)

class PlayListCollection(models.Model):

    playlistname = models.CharField(max_length=200)
    userid = models.ForeignKey(User,on_delete=DO_NOTHING)

class ImageTest(models.Model):

    image1 = models.ImageField(upload_to='img/')
