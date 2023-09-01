from django.shortcuts import render


def about(request):
    return render(request, 'about.html')


def blockgame(request):
    return render(request, 'blockgame.html')

def audiotest(request):
    return render(request, 'audiotest.html')

def intro(request):
    return render(request, 'intro.html')

def my(request):
    return render(request, 'my.html')