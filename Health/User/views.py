from django.http import HttpResponse
from django.contrib import auth
import random
import time
from django.contrib.auth.hashers import make_password, check_password
from django.contrib.auth.models import User
from django.http import HttpResponse, JsonResponse, HttpResponseRedirect
from django.shortcuts import render
from .models import *
import traceback
import re
from Info.models import *
from User.models import *

# Create your views here.

#
# def index(request):
#     return render(request,'/index.html')
#

def register_view(request):
    uname = request.POST.get('uname')
    pwd = request.POST.get('password')
    pwdagain = request.POST.get('passwordagain')
    email = request.POST.get('email')
    userList = user.objects.filter(u_account=uname)
    # 判断是否存在
    if userList:
        return render(request, 'logsign.html',
                      {'code': '账户名已存在', 'sign': True})
    if pwd != pwdagain:
        return render(request, 'logsign.html',
                      {'code': '请输入相同的密码', 'sign': True})
    if len(pwd) < 6 and len(uname) < 6:
        return render(request, 'logsign.html',
                      {'code': '账户密码不可少于6位', 'sign': True})
    if not re.match(r'^[0-9a-zA-Z_]{0,19}@[0-9a-zA-Z]{1,13}\.[com,cn,net]{1,3}$', email):
        return render(request, 'logsign.html',
                      {'code': '邮箱格式不正确', 'sign': True})
    else:
        users = user.objects.create(u_account=uname, u_password=pwd, u_email=email)
        request.session['username'] = uname
        request.session['is_login'] = True
        request.session.set_expiry(24 * 60 * 60)
        return HttpResponseRedirect('/', {'username': uname})


def login_view(request):
    uname = request.POST.get('uname')
    pwd = request.POST.get('password')
    if uname and pwd:
        # Correct password, and the user is marked "active"
        userList = user.objects.filter(u_account=uname, u_password=pwd)

        if userList:
            request.session['username'] = uname
            request.session['is_login'] = True
            request.session.set_expiry(24 * 60 * 60)
            # request
            return HttpResponseRedirect('/', {'user_name': uname})
        else:
            return render(request, 'logsign.html',
                          {'code': '密码错误或无此账号！', 'sign': True})


def login_page(request):
    return render(request, 'logsign.html')


def doctorlogin_view(request):
    return render(request, 'doctorlog.html')


def doctorlogin(request):
    uname = request.POST.get('uname')
    pwd = request.POST.get('password')
    if uname and pwd:
        userList = doctor.objects.get(d_account=uname, d_password=pwd)
        if userList:
            request.session['username'] = userList.id
            request.session['is_login'] = True
            request.session.set_expiry(24 * 60 * 60)
            print(userList.d_password)
            appointments = appointment.objects.filter(d_id=userList.id, is_done=0)
            appointments_isdone = appointment.objects.filter(d_id=userList.id, is_done=1)
            return render(request, 'domain.html',
                          {'username': uname,
                           'appointments': appointments,
                           'appointments_isdone': appointments_isdone})
        else:
            return render(request, 'doctorlog.html',
                          {'code': '密码错误或无此账号！', 'sign': True})
    else:
        return render(request, 'doctorlog.html',
                  {'code': '账号或密码不能为空！', 'sign': True})


#查询诊断结果
def u_center(request):
    username = request.session.get('username')
    userid = user.objects.get(u_account=username).id
    appointments = appointment.objects.filter(u_id=userid, is_done=0)
    appointments_isdone = appointment.objects.filter(u_id=userid, is_done=1)
    return render(request, 'donecenter.html',
                  {'username': username, 'appointments': appointments,
                   'appointments_isdone': appointments_isdone})


def update_doctorInfo(request):
    return render(request, 'updatedoinfo.html')


def update_doctor():
    return None