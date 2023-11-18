from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    email = models.EmailField(unique=True)
    steamId = models.CharField(max_length=50, unique=True, null=True)
    bio = models.TextField(null=True)
    username = models.CharField(max_length=30, unique=True, default='default_username')

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    def __str__(self):
        return self.email
    

class Bundles(models.Model):
    name = models.CharField(max_length=100,null=False)
    price = models.FloatField()
    description = models.TextField(null=True,blank=True)  
    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)
    
    class Mela:
        ordering = [
            '-updated','-created'
        ]
    def __str__(self):
        return self.name

class Server(models.Model):
    serverId = models.CharField(max_length=200,null=True,blank=True)
    serverName = models.CharField(max_length=200,null=True,blank=True)
    
    def __str__(self):
        return self.serverName
