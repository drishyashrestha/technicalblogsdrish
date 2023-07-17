from django.db import models
from django.contrib.auth.models import User

class Profile(models.Model):
    user = models.OneToOneField(to=User, on_delete=models.CASCADE)
    firstname = models.CharField(max_length=20, null=True, blank=True)
    lastname = models.CharField(max_length=20, null=True, blank=True)
    contact = models.CharField(max_length=20, null=True, blank=True)
    address = models.CharField(max_length=100, null=True, blank=True)
    profile_image = models.CharField(max_length=20, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.user.username
    

class Blog(models.Model):
    user = models.ForeignKey(to=User, on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    description = models.CharField(max_length=100)
    image = models.CharField(max_length=1000)
    created_at = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.title
# Create your models here.

