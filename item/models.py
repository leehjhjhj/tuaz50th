from django.db import models

class Item(models.Model):
    name = models.CharField(max_length=10)
    price = models.CharField(max_length=50, null=True)
    category = models.CharField(max_length=50)
    body = models.TextField(null = True)
    thumbnail = models.ImageField(upload_to='item/media/item_thumbnails/', null=True)

class ItemImage(models.Model):
    item = models.ForeignKey(Item, related_name='images', on_delete=models.CASCADE)
    image = models.ImageField(upload_to='item/media/item_images/')