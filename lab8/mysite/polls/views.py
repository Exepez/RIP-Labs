from django.shortcuts import render
from django.http import HttpResponse


def index(request):
    return render(
    request,
    'index.html'
    )

def cpu1(request):
    return render(
    request,
    'cpu1.html'
    )

def cpu2(request):
    return render(
    request,
    'cpu2.html'
    )

def cpu3(request):
    return render(
    request,
    'cpu3.html'
    )