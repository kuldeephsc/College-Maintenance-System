from django.db import models

class EE(models.Model):
    ee_name = models.CharField(max_length=30)
    ee_rollnumber = models.CharField(max_length=10)
    ee_year = models.CharField(max_length=15)
    ee_branch = models.CharField(max_length=2)
    ee_reason = models.CharField(max_length=100, default='None')
    ee_start_date = models.DateField()
    ee_end_date = models.DateField()
    ee_applydate = models.DateField(auto_now=True)
    ee_permission = models.CharField(max_length=10)
