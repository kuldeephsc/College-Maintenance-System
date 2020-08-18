from django.urls import path, include
from . import views
urlpatterns = [
    path('IT/', views.it, name='outpassIT'),
]