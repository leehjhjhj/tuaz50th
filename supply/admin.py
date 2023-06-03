from django.contrib import admin
from .models import *
# Register your models here.




class OrderItemsInline(admin.TabularInline):
    model = OrderItems
    readonly_fields = ('id', 'order', 'item', 'quantity', 'size')
    extra = 0
    def has_delete_permission(self, request, obj=None):
        return False

class OrderAdmin(admin.ModelAdmin):
    list_display = ['id', 'number_name', 'status']
    list_display_links = ['id', 'number_name', 'status']
    readonly_fields = ('id', 'number_name', 'name', 'phone', 'email', 'grade', 'all_price')
    search_fields = ("phone", "number_name")
    list_filter = ['status']
    inlines = [
        OrderItemsInline,
    ]
admin.site.register(Order, OrderAdmin)

#################################################################################

class OrderItemsAdmin(admin.ModelAdmin):
    list_display = ['order', 'item', 'quantity']
    list_display_links = ['order', 'item']
    list_filter = ['item']
    readonly_fields = ('id', 'order', 'item', 'quantity', 'size',)
admin.site.register(OrderItems, OrderItemsAdmin)

#################################################################################
class CancelAdmin(admin.ModelAdmin):
    readonly_fields = ('order', 'bank', 'account', 'account_holder')
    fields = ('order', 'bank', 'account', 'account_holder')



admin.site.register(Cancel, CancelAdmin)