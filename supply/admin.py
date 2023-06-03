from django.contrib import admin
from .models import *
# Register your models here.




class OrderItemsInline(admin.TabularInline):
    model = OrderItems
    readonly_fields = ('id', 'order', 'item', 'quantity', 'size', 'get_item_price')
    extra = 0

    def has_delete_permission(self, request, obj=None):
        return False
    def get_item_price(self, obj):
        return obj.item.price
    
    get_item_price.short_description = 'Item Price'

class OrderAdmin(admin.ModelAdmin):
    list_display = ['id', 'number_name', 'phone', 'status']
    list_display_links = ['id', 'number_name', 'phone', 'status']
    readonly_fields = ('id', 'number_name', 'name', 'phone', 'email', 'grade', 'all_price')
    search_fields = ("phone", "number_name")
    list_filter = ['status']
    inlines = [
        OrderItemsInline,
    ]
admin.site.register(Order, OrderAdmin)

#################################################################################

class OrderItemsAdmin(admin.ModelAdmin):
    list_display = ['order', 'item', 'quantity','size']
    list_display_links = ['order', 'item']
    list_filter = ['item']
    readonly_fields = ('id', 'order', 'item', 'quantity', 'size',)


admin.site.register(OrderItems, OrderItemsAdmin)

#################################################################################
class CancelAdmin(admin.ModelAdmin):
    fields = ('order', 'bank', 'account', 'account_holder', 'display_order_status')
    readonly_fields = ('order', 'bank', 'account', 'account_holder', 'display_order_status')

    def display_order_status(self, obj):
        return obj.order.get_status_display()

    display_order_status.short_description = 'Order Status'


admin.site.register(Cancel, CancelAdmin)