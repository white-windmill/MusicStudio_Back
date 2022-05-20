from django.contrib import admin
from django.urls import path
from django.urls import path, include
from . import views

urlpatterns = [
    path('',views.dispatcher),
    path('creat/',views.creatplaylist),
    path('rank/',views.rank),
    path('ret/',views.testret)
]