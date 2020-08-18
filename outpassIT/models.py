from django.db import models

class IT(models.Model):
    it_name = models.CharField(max_length=30)
    it_rollnumber = models.CharField(max_length=10)
    it_year = models.CharField(max_length=15)
    it_branch = models.CharField(max_length=2)
    it_reason = models.CharField(max_length=100, default='None')
    it_start_date = models.DateField()
    it_end_date = models.DateField()
    it_applydate = models.DateField(auto_now=True)
    it_permission= models.CharField(max_length=10)

