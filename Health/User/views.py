from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.

def index(request):
    return render(request,'/index.html')



def register_view():
    return None


def login_view():
    return None
