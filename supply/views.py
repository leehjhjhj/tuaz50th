from django.shortcuts import render, redirect, reverse, get_object_or_404
from item.models import *
from .models import *


def buy(request):
    all_item = Item.objects.all().exclude(price=0)
    context = {
        'all_item': all_item,
    }
    return render(request, 'buy.html', context)


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
        new_order.password = request.POST['password']
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


def find_order(request):
    if request.method == 'GET':
        return render(request, 'find_order_input.html')

    elif request.method == 'POST':
        phone = request.POST['phone']
        password = request.POST['password']
        orders = Order.objects.filter(phone=phone, password=password)
        if orders:
            context = {
                'orders': orders
                }
            return render(request, 'find_order.html', context)
        else:
            return render(request, 'fail.html')


def cancel_order(request, order_id):
    order = get_object_or_404(Order, id=order_id)
    if request.method == 'GET':
        context = {
            'order': order
        }
        return render(request, 'order_cancel.html', context)
    elif request.method == 'POST':

        new_cancel = Cancel()
        new_cancel.order = order
        new_cancel.account = request.POST['account']
        new_cancel.bank = request.POST['bank']
        new_cancel.account_holder = request.POST['account_holder']
        new_cancel.save()

        order.status = 'cancel_wait'
        order.save()
        return render(request, 'order_cancel_complete.html') 

def delete_order(request, order_id):
    order = get_object_or_404(Order, id=order_id)
    if request.method == 'POST':
        order.delete()
    return render(request, 'order_cancel_complete.html')  


def is_money_order(request, order_id):
    context = {'order_id': order_id}
    if request.method == 'GET':
        return render(request, 'order_cancel_isMoney.html', context)
    elif request.method == 'POST':
        if request.POST['is_money'] == 'yes':
            return redirect('supply:cancel_order', order_id=order_id)
        else:
            order = get_object_or_404(Order, id=order_id)
            order.status = 'canceled'
            order.save()
    return render(request, 'order_cancel_complete.html') 

def change_order(request, order_id):
    order = get_object_or_404(Order, id=order_id)

    if request.method == 'GET':
        context ={
            'order': order
        }
        return render(request, 'order_change.html', context)
    
    elif request.method == 'POST':
        new_grade = request.POST['new_grade']
        new_name = request.POST['new_name']

        order.number_name = new_grade + ' ' + new_name
        order.grade = new_grade
        order.name = new_name
        
        order.phone = request.POST['new_phone']
        order.email = request.POST['new_email']
        order.save()
    
        return render(request, 'order_cancel_complete.html')
