# urls.py 파일을 생성 후 다음을 추가한다. 
from django.contrib import admin
from django.urls import path
from .views import *

urlpatterns = [
    #  항상 index로 연결 
    path('cctv/', cctv_main, name='index'),
    # video_feed 함수의 path 추가
    path('cctv/feed/', video_feed, name='video_feed'),
]
