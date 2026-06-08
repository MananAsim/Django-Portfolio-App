"""
Experience App — Admin Configuration

Registers Experience, Achievement, and ExperienceTechnology models.
Uses inline admin classes to show related records within the
Experience detail page — demonstrating relational database design.

Instructor Note: Model relationships are visible in the admin panel.
When editing an Experience record, its related Achievements and
Technologies appear inline below the main form.
"""

from django.contrib import admin
from .models import Experience, Achievement, ExperienceTechnology


class AchievementInline(admin.TabularInline):
    """Inline admin for achievements — visible inside Experience edit page."""
    model = Achievement
    extra = 1
    fields = ('text', 'order')
    ordering = ('order',)


class ExperienceTechnologyInline(admin.TabularInline):
    """Inline admin for technologies used — visible inside Experience edit page."""
    model = ExperienceTechnology
    extra = 1
    fields = ('name',)


@admin.register(Experience)
class ExperienceAdmin(admin.ModelAdmin):
    """Admin configuration for the Experience model with inline relations."""

    list_display = ('role', 'organization', 'dates', 'order')
    search_fields = ('role', 'organization')
    list_filter = ('organization',)
    list_editable = ('order',)
    ordering = ('order',)

    # Show related models inline (demonstrates relational DB design)
    inlines = [AchievementInline, ExperienceTechnologyInline]


@admin.register(Achievement)
class AchievementAdmin(admin.ModelAdmin):
    list_display = ('experience', 'text', 'order')
    search_fields = ('text', 'experience__role')
    list_filter = ('experience',)


@admin.register(ExperienceTechnology)
class ExperienceTechnologyAdmin(admin.ModelAdmin):
    list_display = ('name', 'experience')
    search_fields = ('name', 'experience__role')
    list_filter = ('experience',)
