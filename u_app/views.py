from django.shortcuts import render, render_to_response
from django.http import HttpResponse
import os
import time

# Create your views here.
def index(request):
    os.system("echo 'hellow world!!'")
    # return HttpResponse('Welcome!!!!!!!!')
    context = {}
    return render(request,'index.html',context)


def home_page(request):
    return  render(request, 'index.html')

def login(request):
    return render(request, 'login.html')