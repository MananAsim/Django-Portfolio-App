"""
Projects App — Views

Provides standalone views for projects, certifications, and case studies.
MVT: View layer for the projects section.
"""

from django.shortcuts import render
from .models import Project, Certification, CaseStudy


def projects_list(request):
    """Returns all projects with related technologies, screenshots, and features."""
    projects = Project.objects.prefetch_related(
        'technologies', 'screenshots', 'features'
    ).all()
    context = {'projects': projects}
    return render(request, 'projects/projects_list.html', context)


def certifications_list(request):
    """Returns all certifications — bonus section."""
    certifications = Certification.objects.all()
    context = {'certifications': certifications}
    return render(request, 'projects/certifications_list.html', context)


def case_studies_list(request):
    """Returns all case studies — bonus section."""
    case_studies = CaseStudy.objects.all()
    context = {'case_studies': case_studies}
    return render(request, 'projects/case_studies_list.html', context)
