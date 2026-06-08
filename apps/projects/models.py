"""
Projects App — Models

Stores projects, certifications, and case studies.
Each project has related technologies, screenshots, and features
(demonstrating ForeignKey relationships).

Certifications and CaseStudies are bonus sections that demonstrate
additional database-driven content beyond the base requirements.

MVT: Model layer for the projects section.
Demonstrates: Model relationships, ImageField, FileField, URLField.
"""

from django.db import models


class Project(models.Model):
    """
    Represents a portfolio project with all metadata.
    Related technologies, screenshots, and features are in separate models.
    """
    STATUS_CHOICES = [
        ('completed', 'Completed'),
        ('in_progress', 'In Progress'),
        ('live', 'Live'),
        ('archived', 'Archived'),
    ]

    name = models.CharField(max_length=200, verbose_name="Project Name")
    description = models.TextField(verbose_name="Project Description")
    github_url = models.URLField(verbose_name="GitHub Repository URL", blank=True, null=True)
    live_url = models.URLField(
        verbose_name="Live URL / Demo",
        blank=True,
        null=True,
        max_length=500
    )
    status = models.CharField(
        max_length=20,
        choices=STATUS_CHOICES,
        blank=True,
        null=True,
        verbose_name="Project Status"
    )
    # Control display order
    order = models.PositiveIntegerField(default=0, verbose_name="Display Order")

    class Meta:
        verbose_name = "Project"
        verbose_name_plural = "Projects"
        ordering = ['order', 'id']

    def __str__(self):
        return self.name


class ProjectTechnology(models.Model):
    """
    A technology used in a specific project.
    ForeignKey → Project (many technologies per project).
    """
    project = models.ForeignKey(
        Project,
        on_delete=models.CASCADE,
        related_name='technologies',
        verbose_name="Project"
    )
    name = models.CharField(max_length=100, verbose_name="Technology Name")

    class Meta:
        verbose_name = "Project Technology"
        verbose_name_plural = "Project Technologies"

    def __str__(self):
        return f"{self.name} ({self.project.name})"


class ProjectScreenshot(models.Model):
    """
    A screenshot image for a project.
    ForeignKey → Project (many screenshots per project).
    Supports media handling through ImageField.
    """
    project = models.ForeignKey(
        Project,
        on_delete=models.CASCADE,
        related_name='screenshots',
        verbose_name="Project"
    )
    image = models.ImageField(
        upload_to='projects/screenshots/',
        verbose_name="Screenshot Image"
    )
    caption = models.CharField(max_length=200, verbose_name="Caption", blank=True)
    order = models.PositiveIntegerField(default=0, verbose_name="Display Order")

    class Meta:
        verbose_name = "Project Screenshot"
        verbose_name_plural = "Project Screenshots"
        ordering = ['order', 'id']

    def __str__(self):
        return f"Screenshot for {self.project.name}"


class ProjectFeature(models.Model):
    """
    A key feature / bullet point for a project.
    ForeignKey → Project (many features per project).
    """
    project = models.ForeignKey(
        Project,
        on_delete=models.CASCADE,
        related_name='features',
        verbose_name="Project"
    )
    text = models.CharField(max_length=300, verbose_name="Feature Description")
    order = models.PositiveIntegerField(default=0, verbose_name="Display Order")

    class Meta:
        verbose_name = "Project Feature"
        verbose_name_plural = "Project Features"
        ordering = ['order', 'id']

    def __str__(self):
        return f"{self.text[:60]} ({self.project.name})"


# ─── Bonus Models ─────────────────────────────────────────────────────────────

class Certification(models.Model):
    """
    BONUS: Stores professional certifications with issuer, date, and image.
    Database-driven — not hardcoded in templates.
    """
    name = models.CharField(max_length=200, verbose_name="Certification Name")
    issuer = models.CharField(max_length=200, verbose_name="Issuing Organization")
    issue_date = models.CharField(
        max_length=50,
        verbose_name="Issue Date",
        blank=True
    )
    credential_url = models.URLField(verbose_name="Credential URL", blank=True, null=True)
    image = models.ImageField(
        upload_to='certifications/',
        verbose_name="Certificate Image",
        blank=True,
        null=True
    )
    order = models.PositiveIntegerField(default=0, verbose_name="Display Order")

    class Meta:
        verbose_name = "Certification"
        verbose_name_plural = "Certifications"
        ordering = ['order', 'id']

    def __str__(self):
        return f"{self.name} — {self.issuer}"


class CaseStudy(models.Model):
    """
    BONUS: Stores case study documents and metadata.
    Links to PDF files through FileField — proper media handling.
    """
    title = models.CharField(max_length=200, verbose_name="Case Study Title")
    description = models.TextField(verbose_name="Description / Summary")
    pdf_file = models.FileField(
        upload_to='case_studies/',
        verbose_name="PDF Document",
        blank=True,
        null=True
    )
    thumbnail = models.ImageField(
        upload_to='case_studies/thumbnails/',
        verbose_name="Thumbnail Image",
        blank=True,
        null=True
    )
    live_url = models.URLField(
        verbose_name="External Link (if any)",
        blank=True,
        null=True,
        max_length=500
    )
    order = models.PositiveIntegerField(default=0, verbose_name="Display Order")

    class Meta:
        verbose_name = "Case Study"
        verbose_name_plural = "Case Studies"
        ordering = ['order', 'id']

    def __str__(self):
        return self.title
