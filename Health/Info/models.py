from django.db import models
from User.models import user


class userinfo(models.Model):
    u_account = models.ForeignKey(user, to_field='u_account',on_delete=models.CASCADE, default='')
    u_name = models.CharField(max_length=10)
    u_age = models.CharField(max_length=10)
    u_gender = models.CharField(max_length=10)
    d_name = models.CharField(max_length=50)
    i_description = models.CharField(max_length=100)

class doctorinfo(models.Model):
    d_name = models.CharField(max_length=10)
    d_local = models.CharField(max_length=50)
    d_department = models.CharField(max_length=50)
    d_hospital = models.CharField(max_length=50)
    d_phone = models.CharField(max_length=30)
    d_title = models.CharField(max_length=50)
    d_experience = models.CharField(max_length=150)
    d_education = models.CharField(max_length=150)
    d_skills = models.CharField(max_length=150)
    d_mooto = models.CharField(max_length=50)