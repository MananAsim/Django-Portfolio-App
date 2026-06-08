"""
Bio App — Models

Stores the portfolio owner's personal information, contact details,
and profile data. This is the central identity model of the portfolio.

MVT: Model layer for the bio section.
"""

from django.db import models


class Bio(models.Model):
    """
    Central model storing the portfolio owner's identity and contact info.
    Only one record is expected (the portfolio owner).
    """
    # Identity
    full_name = models.CharField(max_length=100, verbose_name="Full Name")
    professional_title = models.CharField(max_length=200, verbose_name="Professional Title")
    tagline = models.CharField(max_length=300, verbose_name="Tagline", blank=True)

    # Bio & About
    bio = models.TextField(verbose_name="Short Bio")
    about_section = models.TextField(verbose_name="About Section Content")

    # Contact Details
    email = models.EmailField(verbose_name="Email Address")
    phone = models.CharField(max_length=30, verbose_name="Phone Number", blank=True)
    location = models.CharField(max_length=100, verbose_name="Location", blank=True)

    # Social / Online Presence
    linkedin_url = models.URLField(verbose_name="LinkedIn URL", blank=True)
    github_url = models.URLField(verbose_name="GitHub URL", blank=True)
    portfolio_url = models.URLField(verbose_name="Portfolio URL", blank=True)

    # Media
    profile_image = models.ImageField(
        upload_to='bio/',
        verbose_name="Profile Image",
        blank=True,
        null=True
    )
    resume_file = models.FileField(
        upload_to='resume/',
        verbose_name="Resume (PDF)",
        blank=True,
        null=True
    )

    class Meta:
        verbose_name = "Bio"
        verbose_name_plural = "Bio"

    def __str__(self):
        return self.full_name
