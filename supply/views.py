from django.shortcuts import render
from item.models import *

def buy(request):
    all_item = Item.objects.all()
    context = {
        'all_item': all_item,
    }
    return render(request, 'buy.html', context)

