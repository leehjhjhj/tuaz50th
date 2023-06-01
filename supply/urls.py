from .views import *
from django.urls import path
app_name = 'supply'

urlpatterns = [
    path('', buy, name='buy'),
    path('create/', create, name='create'),
    path('all/', order_list, name='order_list')
]