from django.db import models
from django.contrib.auth.hashers import make_password


class User(models.Model):
    username = models.CharField(max_length=150, unique=True)
    email = models.CharField(max_length=150, unique=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    password = models.CharField(max_length=128, default='qwerty')

    def save(self, *args, **kwargs):
        if not self.id or 'password' in self.get_dirty_fields():
            self.password = make_password(self.password)
        super().save(*args, **kwargs)


    def __str__(self):
        return self.username
