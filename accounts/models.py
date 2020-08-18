from django.db import models

# Create your models here.
class Messfeedback(models.Model):
    meal = models.CharField(max_length=20)
    rating = models.SmallIntegerField()
    review = models.TextField(max_length=300)
    feedback_date = models.DateTimeField(auto_now=True)