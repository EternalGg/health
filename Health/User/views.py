from django.http import HttpResponse
from django.contrib import auth
import random
import time
from django.contrib import auth
from django.contrib.auth.hashers import make_password, check_password
from django.contrib.auth.models import User
from django.http import HttpResponse, JsonResponse, HttpResponseRedirect
from django.shortcuts import render
from .models import *
import traceback


# Create your views here.

#
# def index(request):
#     return render(request,'/index.html')
#

def register_view(request):
    uname = request.POST.get('uname')
    pwd = request.POST.get('password')
    email = request.POST.get('email')
    # 插入数据库
    users = user.objects.create(u_account=uname, u_password=pwd, u_email=email)
    print(uname, pwd)
    traceback.print_exc()
    # 判断是否注册成功
    if users:
        # 将用户信息存放至session对象中
        # request.session['user'] = users

        return HttpResponseRedirect('/')

    return HttpResponseRedirect('/')


def login_view(request):
    uname = request.POST.get('uname')
    pwd = request.POST.get('password')
    print(uname, pwd)
    if uname and pwd:
        # Correct password, and the user is marked "active"
        userList = user.objects.filter(u_account=uname, u_password=pwd)

        if userList:
            # request.session['user'] = userList[0]
            return HttpResponseRedirect('/')
        return HttpResponseRedirect('/users/loginorregister/')


def login_page(request):
    return render(request, 'logsign.html')


def check_uname(request):
    print("jasidjioajsdjiajsidojaisjdiajsoidioasjdjaiosjdoiajsidjioajdioajsodjoajdoiajsdiosa")
    traceback.print_exc()
    uname = request.Get.get('uname', '')

    # 根据用户名去数据库中查询
    userList = user.objects.filter(u_account=uname)

    flag = False

    # 判断是否存在
    if userList:
        flag = True

    return JsonResponse({'flag': flag})