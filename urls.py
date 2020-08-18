from django.urls import path
from . import views

urlpatterns = [
    path('LabMaintenance/', views.lab, name='lab maintenance')
]
