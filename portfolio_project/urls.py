"""
Root URL Configuration — portfolio_project

All page routes are handled by the bio app's main portfolio view.
Media files are served by Django during development.
"""

from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

from django.views.static import serve
from django.urls import re_path

urlpatterns = [
    # Django Admin — instructor can verify database-driven content here
    path('admin/', admin.site.urls),

    # Portfolio home page — handled by the bio app
    path('', include('apps.bio.urls')),
    
    # Serve media files on Vercel regardless of DEBUG status
    re_path(r'^media/(?P<path>.*)$', serve, {'document_root': settings.MEDIA_ROOT}),
]
