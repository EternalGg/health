from django.db import models
import django.utils.timezone as timezone


class userinfo(models.Model):
    u_account =models.CharField(max_length=10)
    u_name = models.CharField(max_length=10)
    u_age = models.CharField(max_length=10)
    u_gender = models.CharField(max_length=10)
    d_department = models.CharField(max_length=50)
    u_description = models.CharField(max_length=100)
    u_phone = models.CharField(max_length=50,default='')

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
    is_working = models.BooleanField(default=True)

class appointment(models.Model):
    d_department = models.CharField(max_length=50)
    d_id = models.IntegerField()
    info_id = models.IntegerField()
    is_working = models.BooleanField(default=False)
    is_done = models.BooleanField(default=False)
    opentime = models.DateTimeField(null=True)
    is_subsequent_visit = models.BooleanField(default=False)
    subsequent_visit_time =  models.DateTimeField(null=True)
    done_time = models.DateTimeField(null=True)