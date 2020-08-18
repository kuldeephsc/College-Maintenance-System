from django.urls import path
from . import views
urlpatterns = [
    path('ME/', views.me, name='OutpassME')
]