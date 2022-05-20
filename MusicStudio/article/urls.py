from django.contrib import admin
from django.urls import path
from django.urls import path, include
from . import views

urlpatterns = [
    path('',views.dispatcher),
    path('all/',views.getallarticle),
    path('del/',views.increasearticle),
]
