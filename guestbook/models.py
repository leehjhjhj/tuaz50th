from django.db import models

class Balloon(models.Model):
    body = models.CharField(max_length=50, null=True)
    created_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.body}"