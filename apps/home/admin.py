# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""

from django.contrib import admin
from .models import *


@admin.register(Video)
class VideoAdmin(admin.ModelAdmin):
    list_display = ('title', 'video', 'pos', 'upload_dt')