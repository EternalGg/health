from django.db import models

# Create your models here.
class user(models.Model):
    u_account = models.CharField(max_length=20,unique=True)
    u_password = models.CharField(max_length=20)
    u_sex = models.CharField(max_length=20)
    u_name = models.CharField(max_length=20)
    u_phone = models.PhoneNumberField(max_length=11)
    u_history = models.CharField(max_length=100)
    u_birthday = models.DateTimeField()
    

