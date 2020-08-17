from django.shortcuts import render,redirect
from django.http import HttpResponse
def index(request):
    return render(request,'index.html')

def aboutus(request):
    if request.method == 'GET':
        return render(request,'aboutus2.html')
def studentoutpass(request):
    if request.method == 'GET':
        return render(request, 'studentoutpass.html')


