from django.db import models

# Create your models here.

class Register(models.Model):
    name = models.CharField(max_length=100)
    address = models.CharField(max_length=100)
    username = models.CharField(max_length=100)
    password = models.CharField(max_length=100)
    def __str__(self):
        self.username()

class Login(models.Model):
    usernames = models.CharField(max_length=100)
    passwords = models.CharField(max_length=100)
    def __str__(self):
        self.username()