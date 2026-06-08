"""
Education App — Views

Provides a standalone view for the education section.
Also used by the main bio view for data aggregation.

MVT: View layer for the education section.
"""

from django.shortcuts import render
from .models import Education


def education_list(request):
    """Returns all education records ordered by display order."""
    education_records = Education.objects.all()
    context = {'education_records': education_records}
    return render(request, 'education/education_list.html', context)
