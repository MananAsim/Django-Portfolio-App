"""
Experience App — Views

Provides a standalone view for the experience section.
MVT: View layer for the experience section.
"""

from django.shortcuts import render
from .models import Experience


def experience_list(request):
    """Returns all experience records with related achievements and technologies."""
    experience_records = Experience.objects.prefetch_related(
        'achievements', 'technologies'
    ).all()
    context = {'experience_records': experience_records}
    return render(request, 'experience/experience_list.html', context)
