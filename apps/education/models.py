"""
Education App — Models

Stores academic history including degrees, institutions,
start/end years, GPA, and descriptions.

MVT: Model layer for the education section.
"""

from django.db import models


class Education(models.Model):
    """
    Represents a single educational qualification (degree, diploma, course, etc.).
    Ordered by the 'order' field for display control.
    """
    degree = models.CharField(max_length=200, verbose_name="Degree / Qualification")
    institution = models.CharField(max_length=300, verbose_name="Institution Name")
    start_year = models.CharField(max_length=10, verbose_name="Start Year")
    end_year = models.CharField(
        max_length=10,
        verbose_name="End Year",
        blank=True,
        help_text="Leave blank or write 'Present' if currently enrolled"
    )
    gpa = models.CharField(
        max_length=10,
        verbose_name="GPA / Grade",
        blank=True,
        null=True
    )
    description = models.TextField(
        verbose_name="Description / Coursework",
        blank=True,
        null=True
    )
    # Control display order (lowest number = shown first)
    order = models.PositiveIntegerField(default=0, verbose_name="Display Order")

    class Meta:
        verbose_name = "Education"
        verbose_name_plural = "Education Records"
        ordering = ['order', '-start_year']

    def __str__(self):
        return f"{self.degree} — {self.institution}"
