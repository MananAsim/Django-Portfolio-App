"""
Bio App — URL Configuration

Maps URL patterns to views for the bio app.
The root URL '/' maps to the portfolio_view which renders the entire portfolio.
"""

from django.urls import path
from . import views

app_name = 'bio'

urlpatterns = [
    # Root URL — main portfolio single-page view
    path('', views.portfolio_view, name='portfolio'),
]
