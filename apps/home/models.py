# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""

from django.db import models
from django.urls import reverse


# Create your models here.
class Video(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField('TITLE', max_length=100, null=True, blank=True)
    position_category = (('T01', 'T01'), ('T02', 'T02'))
    pos = models.CharField('POSITION', max_length=50, choices=position_category, default='None')
    video = models.FileField(upload_to='upload/video/%y')
    status_categories = (('Incomplete', 'Incomplete'), ('Complete', 'Complete'))
    status = models.CharField('STATUS', max_length=20, choices=status_categories, default='Incomplete')
    result_categories = (('Normal', 'Normal'), ('Abnormal', 'Abnormal'))
    result = models.CharField('RESULT', max_length=30, choices=result_categories, null=True, blank=True)
    upload_dt = models.DateTimeField('UPLOAD DATE', auto_now_add=True, null=True)

    class Meta:
        ordering = ('upload_dt',)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('result_detail', args=(self.id,))
