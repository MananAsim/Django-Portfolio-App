"""
Projects App — Admin Configuration

Registers Project, ProjectTechnology, ProjectScreenshot, ProjectFeature,
Certification, and CaseStudy models.

Uses inline admin classes to show related project records together.
Demonstrates media handling through ImageField and FileField in the admin.

Instructor Note: All project data is database-driven.
Visit Admin → Projects to see all project records, technologies,
screenshots, and features stored as relational database records.
"""

from django.contrib import admin
from .models import (
    Project, ProjectTechnology, ProjectScreenshot,
    ProjectFeature, Certification, CaseStudy
)


class ProjectTechnologyInline(admin.TabularInline):
    """Technologies used — shown inline inside Project edit page."""
    model = ProjectTechnology
    extra = 1
    fields = ('name',)


class ProjectScreenshotInline(admin.TabularInline):
    """Screenshots — shown inline inside Project edit page."""
    model = ProjectScreenshot
    extra = 1
    fields = ('image', 'caption', 'order')


class ProjectFeatureInline(admin.TabularInline):
    """Key features — shown inline inside Project edit page."""
    model = ProjectFeature
    extra = 1
    fields = ('text', 'order')


@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    """Admin configuration for Project with all inline relations."""

    list_display = ('name', 'status', 'live_url', 'github_url', 'order')
    search_fields = ('name', 'description')
    list_filter = ('status',)
    list_editable = ('order',)
    ordering = ('order',)

    # Display all related models inline
    inlines = [ProjectFeatureInline, ProjectTechnologyInline, ProjectScreenshotInline]


@admin.register(ProjectTechnology)
class ProjectTechnologyAdmin(admin.ModelAdmin):
    list_display = ('name', 'project')
    search_fields = ('name', 'project__name')
    list_filter = ('project',)


@admin.register(ProjectScreenshot)
class ProjectScreenshotAdmin(admin.ModelAdmin):
    list_display = ('project', 'caption', 'order')
    search_fields = ('project__name', 'caption')
    list_filter = ('project',)


@admin.register(ProjectFeature)
class ProjectFeatureAdmin(admin.ModelAdmin):
    list_display = ('text', 'project', 'order')
    search_fields = ('text', 'project__name')
    list_filter = ('project',)


@admin.register(Certification)
class CertificationAdmin(admin.ModelAdmin):
    """Admin for bonus Certification model."""
    list_display = ('name', 'issuer', 'issue_date', 'order')
    search_fields = ('name', 'issuer')
    list_filter = ('issuer',)
    list_editable = ('order',)


@admin.register(CaseStudy)
class CaseStudyAdmin(admin.ModelAdmin):
    """Admin for bonus CaseStudy model."""
    list_display = ('title', 'order')
    search_fields = ('title', 'description')
    list_editable = ('order',)
