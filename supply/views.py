from django.shortcuts import render, redirect
from item.models import *
from .models import *
from django.views.decorators.csrf import csrf_exempt

def buy(request):
    all_item = Item.objects.all()
    context = {
        'all_item': all_item,
    }
    return render(request, 'buy.html', context)

@csrf_exempt
def create(request):
    if request.method == 'POST':  
        new_order = Order()
        new_order.name = request.POST['name']   
        new_order.phone = request.POST['phone'] 
        email_id = request.POST['email_id']   
        email_server = request.POST['email_server']
        new_order.email = email_id + '@' + email_server
        new_order.grade = request.POST['grade']
        new_order.all_price = request.POST['total-price-input']
        new_order.status = 'waiting'
        new_order.save()


        product_names = request.POST.getlist('category[]')
        sizes = request.POST.getlist('size-category[]')
        quantities = request.POST.getlist('quantity[]')

        print(product_names, sizes, quantities)
        for i in range(len(product_names)):
            product_name = product_names[i]
            size = sizes[i]
            quantity = quantities[i]
            
            new_order_item = OrderItems()
            new_order_item.order = new_order
            new_order_item.item = Item.objects.get(name=product_name)
            if not new_order_item.item.category == 'cloth':
                new_order_item.size = '없음'
            else:
                new_order_item.size = size
            new_order_item.quantity = quantity
            new_order_item.save()

    # 추가적인 작업 수행
        return redirect('home.html')
    return redirect('home.html')