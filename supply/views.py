from django.shortcuts import render, redirect, reverse, get_object_or_404
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

        new_order.number_name = request.POST['grade'] + " " + request.POST['name']
        new_order.save()


        product_names = request.POST.getlist('category[]')
        sizes = request.POST.getlist('size-category[]')
        quantities = request.POST.getlist('quantity[]')
        
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

        context = {
            'order': new_order
        }
        return render(request, 'order_one.html', context)
    return redirect('supply:order_list')

def order_list(request):
    orders = Order.objects.all()
    context = {
        'orders': orders
        }
    return render(request, 'order_list.html', context)

@csrf_exempt
def find_order(request):
    if request.method == 'GET':
        return render(request, 'find_order_input.html')

    elif request.method == 'POST':
        phone = request.POST['phone']
        orders = Order.objects.filter(phone=phone)
        context = {
            'orders': orders
            }
        return render(request, 'find_order.html', context)

@csrf_exempt
def cancel_order(request, order_id):
    order = get_object_or_404(Order, id=order_id)
    if request.method == 'POST':
        # Perform cancel order logic here
        order.delete()
        return render(request, 'order_cancel.html')  # Replace 'home' with the appropriate URL name
    return redirect('order_one', order_id=order_id)