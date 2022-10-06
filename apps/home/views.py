# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""

from turtle import position
from django import template
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.template import loader
from django.urls import reverse
from .forms import UploadForm
from .models import Video
import os
import datetime
from django.views.generic import ListView, DetailView


@login_required(login_url="/login/")
def index(request):
    context = {'segment': 'index'}

    html_template = loader.get_template('home/index.html')
    return HttpResponse(html_template.render(context, request))


@login_required(login_url="/login/")
def pages(request):
    print('function pages start')
    context = {}
    # All resource paths end in .html.
    # Pick out the html file name from the url. And load that template.
    try:

        load_template = request.path.split('/')[-1]
        print('현재 load된 템플릿은', load_template)
        if load_template == 'admin':
            return HttpResponseRedirect(reverse('admin:index'))
        context['segment'] = load_template

        html_template = loader.get_template('home/' + load_template)

        if load_template == 'upload.html':
            print('page 함수에서 실행됨')
            re = upload(request)
            print(re)
        elif load_template == 'player.html':
            print('pages 함수에서 실행됨')

        return HttpResponse(html_template.render(context, request))

    except template.TemplateDoesNotExist:
        html_template = loader.get_template('home/page-404.html')
        return HttpResponse(html_template.render(context, request))

    except:
        html_template = loader.get_template('home/page-500.html')
        return HttpResponse(html_template.render(context, request))


@login_required(login_url="/login/")
def player(request):
    print('player function start')
    load_template = request.path.split('/')[-1]
    html_template = 'home/' + load_template

    if request.method == "POST":
        print('request method is POST')
        video = Video()
        video.video_no = request.POST['position']
        # video.video_file = request.POST['file']
        video.video_url = request.POST['url']
        video.save()
        print('form data save!')

    return render(request, html_template, context={'POST': 'POST Method'})


def video_result(request):
    video = Video.objects.all()
    return render(request, '/player', {'video': video})


@login_required(login_url="/login/")
def upload(request):
    print('function upload video start')
    context = {}
    load_template = request.path.split('/')[-1]
    print(load_template)

    html_txt = 'home/' + load_template
    html_template = loader.get_template(html_txt)

    context['segment'] = load_template

    # create object of form
    if request.method == "POST" and request.FILES['video']:
        print('Request POST')
        year = datetime.datetime.now().strftime("%y")  # 미디어 파일 저장 경로를 위한 (연도별 저장)

        form = UploadForm(request.POST, request.FILES)

        # if str(form.video).split('.')[-1] != 'mp4':
        #     print('mp4 형식에 맞지 않음!')
        #     form = Video.objects.all()
        #     return render(request, html_template, context={'form': form})

        if form.is_valid():
            print('form is valid!')
            context['form'] = form
            print(str(request.FILES['video']))
            filePath = 'media/upload/video/' + year + '/'
            videoPath = os.path.dirname(filePath) + '/' + str(request.FILES['video'])

            upload_form = form.save(commit=False)
            upload_form.save(form)

            # form.Meta.model.video = videoPath
            # upload_form.save(form)

            # os.rename(str(request.FILES['video']), str(request.POST['title']+'.mp4'))
            # print(str(request.FILES['video']))
            # filePath = 'media/upload/video/' + year + '/'
            # print('file path is', filePath)
            # videoPath = os.path.dirname(filePath) + '/' + str(request.FILES['video'])
            # renamePath = os.path.dirname(filePath) + '/' + str(
            #     request.POST['title'] + '_' + str(request.POST['pos']) + '.mp4')
            # print('video path is', videoPath)
            # print('rename video path is ', renamePath)
            # file_path = os.path.dirname(os.path.realpath('./core/media/result/')) + str(v_file)
            # os.rename(videoPath, filePath+'/'+str(request.POST['title'])+'.mp4')
            # os.rename()
            html_template = loader.get_template('home/index.html')
            # return render(request, "accounts/login.html", {"form": form, "msg": msg})
            return HttpResponse(html_template.render({'segment': index}, request))
            # return render(request, html_template, {"form": form, "segment": index})
        else:
            print(request, "ERROR!")
            context['form'] = form

            return HttpResponse(html_template.render(context, request))
    else:
        print('Not Request POST')
        form = UploadForm()
        context['form'] = form
        return render(request, html_txt, context)

    print('function upload video end')
    context['POST'] = 'POST Method'
    return render(request, html_txt, context)


class VideoLV(ListView):
    model = Video


class VideoDV(DetailView):
    model = Video
