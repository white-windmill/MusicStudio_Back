"""MusicStudio URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.conf.urls.static import static
from django.urls import path
from django.urls import path, include
from django.conf import settings
from playlist.views import listorders
from django.contrib import admin
from .settings import MEDIA_ROOT
from django.views.static import serve
urlpatterns = [   
    path('api/admin/', admin.site.urls),
    path('api/user/', include('user.urls')),
    path('api/sign/', include('sign.urls')),
    path('api/music/', include('music.urls')),
    path('api/history/', include('history.urls')),
    path('api/playlist/', include('playlist.urls')),
    path('api/comment/', include('comment.urls')),
    path('api/article/', include('article.urls')),
    path('api/imgurl/', include('pictest.urls')),
    path('api/search/', include('search.urls')),
    path(r'^media/(?P<path>.*)$', serve, {"document_root": MEDIA_ROOT}),
]  + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
