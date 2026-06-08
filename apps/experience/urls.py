"""Experience App — URL Configuration"""
from django.urls import path
from . import views

app_name = 'experience'

urlpatterns = [
    path('experience/', views.experience_list, name='experience_list'),
]
