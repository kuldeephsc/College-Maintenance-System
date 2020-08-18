
from django.urls import path
from . import views

urlpatterns = [
    path('register/', views.register, name='register page'),
    path('login/', views.login, name='login page'),
    path('logout/', views.logout, name='logout page'),
    path('login1/', views.login1, name='login1 page'),
    path('profile/', views.student, name='user profile'),
    path('MessFeedback/', views.mess, name='messfeedback'),



]
