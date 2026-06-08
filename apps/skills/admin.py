"""
Skills App — Admin Configuration

Registers the Skill model with list_display, search_fields,
list_filter (by category), and list_editable for fast updates.

Instructor Note: All skills are stored in the database with categories and
proficiency levels. These drive the progress bars in the frontend template.
Visit Admin → Skills to view and edit.
"""

from django.contrib import admin
from .models import Skill


@admin.register(Skill)
class SkillAdmin(admin.ModelAdmin):
    """Admin configuration for the Skill model."""

    list_display = ('name', 'category', 'proficiency', 'order')
    search_fields = ('name',)
    list_filter = ('category',)
    list_editable = ('proficiency', 'order')
    ordering = ('category', 'order', 'name')
