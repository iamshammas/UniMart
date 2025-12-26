from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE,related_name='profile')
    address = models.TextField(blank=True,null=True)
    phone = models.CharField(max_length=20,blank=True,null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        resp = self.user.username
        return resp.upper()