from django.db import models

class Balloon(models.Model):
    writer = models.CharField(max_length=10, unique=True, null=True)
    body = models.CharField(max_length=50, unique=True, null=True)