from django.urls import path
from . import views

urlpatterns = [
    path('HostelMaintenance/', views.repair, name='hostel maintenance'),
]
