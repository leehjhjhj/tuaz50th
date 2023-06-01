from django.db import models
from item.models import *

class Order(models.Model):
    STATUS_CHOICES = (
        ('waiting', '입금 대기'),
        ('completed', '입금 완료'),
    )
    name = models.CharField(max_length=10)
    phone = models.CharField(max_length=11)
    email = models.EmailField(max_length=50)
    grade = models.IntegerField()
    all_price = models.IntegerField()
    status = models.CharField(max_length=20, choices=STATUS_CHOICES)

class OrderItems(models.Model):
    order = models.ForeignKey(Order,related_name='order', on_delete=models.CASCADE)
    item = models.ForeignKey(Item, related_name='item', on_delete=models.CASCADE)
    quantity = models.IntegerField()
    size = models.CharField(max_length=10, null=True)
    
    