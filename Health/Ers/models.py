from django.db import models
# Create your models here.
class event (models.Model):
    e_doctor_id = models.IntegerField()
    e_department_id = models.IntegerField()
    e_hospital_id = models.IntegerField()
    e_user_id = models.IntegerField()
    e_appointment = models.IntegerField()
    e_state = models.IntegerField()

class chat(models.Model):
    appointment_id = models.IntegerField()
    master = models.CharField(max_length=50)
    message = models.CharField(max_length=150)
    flag = models.IntegerField()