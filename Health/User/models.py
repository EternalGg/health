from django.db import models

# Create your models here.
class user(models.Model):
    u_account = models.CharField(max_length=20,unique=True)
    u_password = models.CharField(max_length=20)
    u_sex = models.CharField(max_length=20)
    u_name = models.CharField(max_length=20)
    u_phone = models.CharField(max_length=11,unique=True)
    u_history = models.CharField(max_length=100)
    u_age = models.IntegerField()
    u_weight = models.FloatField()

