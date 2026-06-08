"""Education App — URL Configuration"""
from django.urls import path
from . import views

app_name = 'education'

urlpatterns = [
    path('education/', views.education_list, name='education_list'),
]
