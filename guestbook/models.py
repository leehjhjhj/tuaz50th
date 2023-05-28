from django.db import models

class Balloon(models.Model):
    writer = models.CharField(max_length=10, null=True)
    body = models.CharField(max_length=50, null=True)