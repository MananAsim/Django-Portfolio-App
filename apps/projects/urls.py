"""Projects App — URL Configuration"""
from django.urls import path
from . import views

app_name = 'projects'

urlpatterns = [
    path('projects/', views.projects_list, name='projects_list'),
    path('certifications/', views.certifications_list, name='certifications_list'),
    path('case-studies/', views.case_studies_list, name='case_studies_list'),
]
