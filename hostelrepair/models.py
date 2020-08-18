from django.db import models

class Hostel(models.Model):
    student_name = models.CharField(max_length=30, default='root')
    userid = models.CharField(max_length=10, default='root')
    hostel = models.CharField(max_length=20, default='root')
    floor = models.CharField(max_length=20, default='root')
    room = models.SmallIntegerField(default=0)
    appliances = models.CharField(max_length=20, default='root')
    status = models.CharField(max_length=20, default='pending')