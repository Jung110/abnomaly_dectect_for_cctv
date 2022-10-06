# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""

from django.urls import path, re_path
from apps.home import views
from django.conf.urls.static import static
from core import settings

urlpatterns = [

    # The home page
    path('', views.index, name='home'),
    path('profile.html', views.pages, name='profile'),
    path('player.html', views.player, name='player'),
    path('upload.html', views.upload, name='upload'),
    path('chart-morris.html', views.pages, name='chart-morris'),


    path('result/', views.VideoLV.as_view(), name='result_list'),
    path('result/<int:pk>/', views.VideoDV.as_view(), name='result_detail'),

    # Matches any html file
    #re_path(r'^.*\.*', views.pages, name='pages'),
]


