# -*- coding: utf-8 -*-
from django.shortcuts import render
from django.shortcuts import render_to_response

from django.views.decorators.csrf import csrf_exempt
from django.contrib import messages

from born_user.models import user, project, music, MusicFile

@csrf_exempt
def login(request):
    if request.method == 'POST':
        try:
            account = request.POST['account']
            passwd = request.POST['passwd']
            user_data = user.objects.get(account=account, password=passwd)
            if user_data:
                messages.success(request, 'Login Success!')
                # 儲存登入狀態session
                request.session['login_id'] = user_data.id
                return render_to_response('index.html')
            else:
                messages.error(request, 'Failed Account or Password!')
                return render_to_response('login.html')
        except Exception, ex:
            messages.error(request, 'Error login: ' + ex.message)
            return render_to_response('login.html')
    return render_to_response('login.html')

@csrf_exempt
def register(request):
    if request.method == 'POST':
        try:
            account = request.POST['account']
            email = request.POST['email']
            passwd = request.POST['passwd']
            name = request.POST['name']
            birthday = request.POST['birthday']
            sex = request.POST['sex']
            nickname = request.POST['nickname']
            user_data = user.objects.create(
                account=account,
                email=email,
                password=passwd,
                name=name,
                birthday=birthday,
                sex=sex,
                nickname=nickname
            )
            messages.success(request, 'Create Success!')
            # 預設註冊完即登入，儲存session
            request.session['login_id'] = user_data.id
            return render_to_response('index.html')
        except Exception, ex:
            messages.error(request, 'Error register: ' + ex.message)
            return render_to_response('login.html')
    return render_to_response('login.html')

from django.core.files import File
from django.core.files.base import ContentFile
@csrf_exempt
def new_project(request):
    if request.method == 'POST':
        if request.session['login_id']:
            file_content = ContentFile(request.FILES['video'].read())
            m_file = MusicFile()
            m_file.musicfile.save(request.FILES['video'].name, file_content)
            messages.success(request, 'Upload Success!')
        else:
            messages.error(request, 'Permission denied')
    return render_to_response('upload.html')
