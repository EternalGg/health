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

class doctor(models.Model):
    d_account = models.CharField(max_length=20,unique=True)
    d_password = models.CharField(max_length=20)
    d_sex = models.CharField(max_length=20)
    d_name = models.CharField(max_length=20)
    d_phone = models.CharField(max_length=11,unique=True)
    d_history = models.CharField(max_length=100)
    d_age = models.IntegerField()
    d_department = models.IntegerField()
    d_hospital = models.IntegerField()