"""
Experience App — Models

Stores professional work experience records. Each experience entry
has related Achievement and Technology records (one-to-many relationships).

MVT: Model layer for the experience section.
Demonstrates: Model relationships (ForeignKey).
"""

from django.db import models


class Experience(models.Model):
    """
    Represents a single work experience / job position.
    Related achievements and technologies are stored in separate models
    to demonstrate Django model relationships.
    """
    role = models.CharField(max_length=200, verbose_name="Job Role / Title")
    organization = models.CharField(max_length=200, verbose_name="Organization / Company")
    dates = models.CharField(max_length=200, verbose_name="Employment Dates")
    responsibilities = models.TextField(verbose_name="Role Description / Responsibilities")
    # Control display order (lowest = shown first)
    order = models.PositiveIntegerField(default=0, verbose_name="Display Order")

    class Meta:
        verbose_name = "Experience"
        verbose_name_plural = "Experience Records"
        ordering = ['order', 'id']

    def __str__(self):
        return f"{self.role} at {self.organization}"


class Achievement(models.Model):
    """
    A single achievement bullet point linked to a specific experience.
    Demonstrates ForeignKey relationship (many achievements → one experience).
    """
    experience = models.ForeignKey(
        Experience,
        on_delete=models.CASCADE,
        related_name='achievements',
        verbose_name="Experience"
    )
    text = models.TextField(verbose_name="Achievement Text")
    order = models.PositiveIntegerField(default=0, verbose_name="Display Order")

    class Meta:
        verbose_name = "Achievement"
        verbose_name_plural = "Achievements"
        ordering = ['order', 'id']

    def __str__(self):
        return f"Achievement for {self.experience.role}: {self.text[:60]}..."


class ExperienceTechnology(models.Model):
    """
    A technology/tool used in a specific role.
    Demonstrates ForeignKey relationship (many technologies → one experience).
    """
    experience = models.ForeignKey(
        Experience,
        on_delete=models.CASCADE,
        related_name='technologies',
        verbose_name="Experience"
    )
    name = models.CharField(max_length=100, verbose_name="Technology / Tool")

    class Meta:
        verbose_name = "Experience Technology"
        verbose_name_plural = "Experience Technologies"

    def __str__(self):
        return f"{self.name} ({self.experience.role})"
