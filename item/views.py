from django.shortcuts import render, get_object_or_404
from .models import Item

def all_items(request):
    category = request.GET.get("category")
    if not category or category == 'all':
        items = Item.objects.all()
    else:
        items = Item.objects.filter(category=category)
    
    context = {
        'items': items,
        'selected_category': category,
    }
    return render(request, 'all_items.html', context)

def item_detail(request, item_id):
    item = get_object_or_404(Item, pk=item_id)
    context = {
        'item': item
    }
    return render(request, 'item_detail.html', context)



