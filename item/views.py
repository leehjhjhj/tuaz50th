from django.shortcuts import render, get_object_or_404
from .models import *

def all_items(request):
    category = request.GET.get("category")
    order = ['clothes', 'cup', 'badge']

    if not category or category == 'all':
        items = Item.objects.all()
    else:
        items = Item.objects.filter(category=category)
    items = sorted(list(items), key=lambda item: order.index(item.category))

    context = {
        'items': items,
        'selected_category': category,
    }
    return render(request, 'all_items.html', context)

def item_detail(request, item_id):
    item_detail = get_object_or_404(Item, pk=item_id)
    item_photos = ItemImage.objects.filter(item=item_id)
    related_items = Item.objects.filter(category=item_detail.category).exclude(pk=item_id)
    context = {
        'item_detail': item_detail,
        'item_photos': item_photos,
        'related_items': related_items,
    }
    return render(request, 'item_detail.html', context)



