from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def vista(request):
    return HttpResponse("<h1>app 1 vista 1</h1>")

def vista2(request):
    return HttpResponse("<h1>app 1 vista 2</h1>")