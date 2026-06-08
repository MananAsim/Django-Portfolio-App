"""
Bio App — Views

The main portfolio view. Pulls ALL section data from the database
and passes it to the single-page portfolio template.

MVT: View layer — connects Models (database) to Templates (HTML).
Demonstrates: Database querying, cross-app data aggregation, context passing.
"""

from django.shortcuts import render
from .models import Bio
from apps.education.models import Education
from apps.skills.models import Skill
from apps.experience.models import Experience
from apps.projects.models import Project, Certification, CaseStudy


def portfolio_view(request):
    """
    Main portfolio view — fetches all section data from the database
    and passes it to the portfolio template as context variables.

    This single view demonstrates Django's MVT pattern:
    - Models: Data comes from database via ORM queries
    - View: This function processes and prepares data
    - Template: portfolio/index.html renders the data dynamically
    """

    # ── Bio (one record expected) ─────────────────────────────────────────────
    bio = Bio.objects.first()

    # ── Education records ─────────────────────────────────────────────────────
    education_records = Education.objects.all()

    # ── Skills grouped by category ────────────────────────────────────────────
    tools_skills = Skill.objects.filter(category='tools_platforms')
    language_skills = Skill.objects.filter(category='languages_frameworks')
    concept_skills = Skill.objects.filter(category='technical_concepts')

    # ── Experience with prefetched related data ───────────────────────────────
    # prefetch_related loads achievements and technologies in efficient queries
    experience_records = Experience.objects.prefetch_related(
        'achievements', 'technologies'
    ).all()

    # ── Projects with prefetched related data ─────────────────────────────────
    projects = Project.objects.prefetch_related(
        'technologies', 'screenshots', 'features'
    ).all()

    # ── Bonus: Certifications and Case Studies ────────────────────────────────
    certifications = Certification.objects.all()
    case_studies = CaseStudy.objects.all()

    # ── Build context dictionary ──────────────────────────────────────────────
    # All data is from the database — NO hardcoded content below
    context = {
        'bio': bio,
        'education_records': education_records,
        'tools_skills': tools_skills,
        'language_skills': language_skills,
        'concept_skills': concept_skills,
        'experience_records': experience_records,
        'projects': projects,
        'certifications': certifications,
        'case_studies': case_studies,
    }

    return render(request, 'portfolio/index.html', context)
