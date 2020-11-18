from django.db import models

# Create your models here.
class user(models.Model):
    u_account = models.CharField(max_length=20,unique=True)
    u_password = models.CharField(max_length=20)
