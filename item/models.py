from django.db import models

class Item(models.Model):
    CATEGORY_CHOICES = (
        ('clothes', '의류'),
        ('cup', '컵'),
        ('badge', '뱃지'),
    )
    name = models.CharField(max_length=32)
    price = models.CharField(max_length=50, null=True)
    category = models.CharField(max_length=50, choices=CATEGORY_CHOICES)
    body = models.TextField(null = True)
    thumbnail = models.ImageField(upload_to='item_thumbnails/', null=True)

    def __str__(self):
        return f"{self.name}"
    

class ItemImage(models.Model):
    item = models.ForeignKey(Item, related_name='images', on_delete=models.CASCADE)
    image = models.ImageField(upload_to='item_images/')

    def __str__(self):
        return f"{self.id}: {self.item.name}의 사진"