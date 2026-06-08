"""
Skills App — Views

Provides a standalone view for the skills section.
Also used by the main bio view for data aggregation.

MVT: View layer for the skills section.
"""

from django.shortcuts import render
from .models import Skill


def skills_list(request):
    """Returns skills grouped by category."""
    tools_skills = Skill.objects.filter(category='tools_platforms')
    language_skills = Skill.objects.filter(category='languages_frameworks')
    concept_skills = Skill.objects.filter(category='technical_concepts')
    context = {
        'tools_skills': tools_skills,
        'language_skills': language_skills,
        'concept_skills': concept_skills,
    }
    return render(request, 'skills/skills_list.html', context)
