"""
Bio App — Admin Configuration

Registers the Bio model with list_display, search_fields,
and fieldsets for clean admin panel display.

Instructor Note: All portfolio data is stored in the database.
Visit Admin → Bio to see and edit the portfolio owner's information.
"""

from django.contrib import admin
from .models import Bio


@admin.register(Bio)
class BioAdmin(admin.ModelAdmin):
    """Admin configuration for the Bio model."""

    # Columns shown in the changelist
    list_display = ('full_name', 'professional_title', 'email', 'location', 'phone')

    # Searchable fields
    search_fields = ('full_name', 'professional_title', 'email', 'location')

    # Grouped fieldsets for clean admin UI
    fieldsets = (
        ('Identity', {
            'fields': ('full_name', 'professional_title', 'tagline')
        }),
        ('Bio & About', {
            'fields': ('bio', 'about_section')
        }),
        ('Contact Details', {
            'fields': ('email', 'phone', 'location')
        }),
        ('Online Presence', {
            'fields': ('linkedin_url', 'github_url', 'portfolio_url')
        }),
        ('Media Files', {
            'fields': ('profile_image', 'resume_file'),
            'description': 'Upload profile photo and resume PDF here.'
        }),
    )
