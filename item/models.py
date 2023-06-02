from django.db import models

class Item(models.Model):
    name = models.CharField(max_length=10)
    price = models.CharField(max_length=50, null=True)
    category = models.CharField(max_length=50)
    body = models.TextField(null = True)
    thumbnail = models.ImageField(upload_to='item_thumbnails/', null=True)

    def __str__(self):
        return f"{self.name}"
    

class ItemImage(models.Model):
    item = models.ForeignKey(Item, related_name='images', on_delete=models.CASCADE)
    image = models.ImageField(upload_to='item_images/')

    def __str__(self):
        return f"{self.id}: {self.item.name}의 사진"