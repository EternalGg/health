from django.db import models
# import channe
# Create your models here.
class event (models.Model):
    e_doctor_id = models.IntegerField()
    e_department_id = models.IntegerField()
    e_hospital_id = models.IntegerField()
    e_user_id = models.IntegerField()
    e_appointment = models.IntegerField()
    e_state = models.IntegerField()