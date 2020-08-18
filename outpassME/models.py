from django.db import models


class ME(models.Model):
    me_name = models.CharField(max_length=30)
    me_rollnumber = models.CharField(max_length=10)
    me_year = models.CharField(max_length=15)
    me_branch = models.CharField(max_length=2)
    me_reason = models.CharField(max_length=100, default='None')
    me_start_date = models.DateField()
    me_end_date = models.DateField()
    me_applydate = models.DateField(auto_now=True)
    me_permission = models.CharField(max_length=10)


from django.db import models

# Create your models here.
