from django.urls import path
from . import views
urlpatterns = [
    path('EE/', views.ee, name='OutpassEE')
]