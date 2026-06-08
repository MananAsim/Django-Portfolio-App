"""
Education App — Admin Configuration

Registers the Education model with list_display, search_fields,
and list_filter for easy navigation.

Instructor Note: Education records are database-driven.
Add or edit degrees in Admin → Education Records.
"""

from django.contrib import admin
from .models import Education


@admin.register(Education)
class EducationAdmin(admin.ModelAdmin):
    """Admin configuration for the Education model."""

    list_display = ('degree', 'institution', 'start_year', 'end_year', 'gpa', 'order')
    search_fields = ('degree', 'institution')
    list_filter = ('start_year', 'end_year')
    list_editable = ('order',)
    ordering = ('order', '-start_year')
