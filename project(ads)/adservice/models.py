from django.db import models
from django.conf import settings


class Ad(models.Model):
    title = models.CharField(max_length=255,default='0')
    description = models.TextField(default='0')
    price = models.DecimalField(max_digits=10, decimal_places=2,default='0')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title