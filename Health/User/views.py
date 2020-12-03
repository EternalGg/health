from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import render
from .models import *


# Create your views here.

#
# def index(request):
#     return render(request,'/index.html')
#

def register_view(request):
    # if request.method == 'GET':
    #     return render(request, 'register.html')
    # else:
    #     uname = request.POST.get('uname', '')
    #     pwd = request.POST.get('pwd', '')
    #
    #     if uname and pwd:
    #         User = user(u_account=uname, u_password=pwd)
    #         User.save()
    #
    #         return HttpResponse('注册成功！')

    uname = request.POST.get('uname', '')
    pwd = request.POST.get('pwd', '')
    print (uname, pwd)
    if uname and pwd:
        User = user(u_account=uname, u_password=pwd)
        User.save()

        return HttpResponse('注册成功！')
    else:
        return HttpResponse('注册失败！')


def login_view(request):
    uname = request.POST.get('uname')
    pwd = request.POST.get('pwd')

    if uname and pwd:
        c = user.objects.filter(u_account=uname, u_password=pwd).count()
        if c == 1:
            return render(request,'main.html')
    return HttpResponse('登录失败！')