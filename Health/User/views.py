from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.

#
# def index(request):
#     return render(request,'/index.html')
#

def register_view(request):

    return render(request,'signin.html')


def login_view(request):
    return render(request,'login.html')