from django.db import models

# # Create your models here.
class hospital (models.Model):
    h_name = models.CharField(max_length=50)


class department (models.Model):
    d_name = models.CharField(max_length=50)

