"""
Skills App — Models

Stores technical skills categorised by type, with proficiency percentages
used to render progress bars in the portfolio UI.

MVT: Model layer for the skills section.
"""

from django.db import models


class Skill(models.Model):
    """
    Represents a single technical skill with its category and proficiency level.
    Proficiency is stored as a percentage (0–100) for rendering HTML progress bars.
    """
    # Skill categories matching the dataset
    CATEGORY_CHOICES = [
        ('tools_platforms', 'Tools & Platforms'),
        ('languages_frameworks', 'Languages & Frameworks'),
        ('technical_concepts', 'Technical Concepts'),
    ]

    name = models.CharField(max_length=100, verbose_name="Skill Name")
    category = models.CharField(
        max_length=50,
        choices=CATEGORY_CHOICES,
        verbose_name="Category"
    )
    # Proficiency: 0 to 100 (displayed as a progress bar percentage)
    proficiency = models.PositiveIntegerField(
        default=80,
        verbose_name="Proficiency (%)",
        help_text="Enter a value between 0 and 100"
    )
    # Control display order within a category
    order = models.PositiveIntegerField(default=0, verbose_name="Display Order")

    class Meta:
        verbose_name = "Skill"
        verbose_name_plural = "Skills"
        ordering = ['category', 'order', 'name']

    def __str__(self):
        return f"{self.name} ({self.get_category_display()}) — {self.proficiency}%"
