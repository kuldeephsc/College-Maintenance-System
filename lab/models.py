from django.db import models

class Labrepair(models.Model):
    lab = models.CharField(max_length=10)
    system = models.IntegerField()
    problem = models.CharField(max_length=15)
    lab_status = models.CharField(max_length=15, default='none')