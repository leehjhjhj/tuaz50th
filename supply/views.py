from django.shortcuts import render


def buy(request):
    return render(request, 'buy.html')

