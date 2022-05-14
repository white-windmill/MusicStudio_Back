from django.contrib import admin

# Register your models here.
from django.contrib import admin

from .models import User, Article, Comment, History, Music, MusicCollection, PlayList, PlayListCollection,ImageTest

admin.site.register(User)
admin.site.register(Article)
admin.site.register(Comment)
admin.site.register(History)
admin.site.register(Music)
admin.site.register(MusicCollection)
admin.site.register(PlayList)
admin.site.register(PlayListCollection)
admin.site.register(ImageTest)