# Deployment Instructions

## Django Portfolio Website — Manan Asim
**BS Computer Science | Web Technologies Term Project**
**University of Management & Technology (UMT), Lahore**

---

## Quick Start (Development)

```bash
# 1. Install dependencies
pip install -r requirements.txt

# 2. Run database migrations
python manage.py migrate

# 3. Load portfolio data from fixtures
python manage.py loaddata fixtures/fixtures.json

# 4. Create admin account (optional, for admin panel)
python manage.py createsuperuser

# 5. Run the development server
python manage.py runserver
```

Then open: **http://127.0.0.1:8000/**
Admin panel: **http://127.0.0.1:8000/admin/**

---

## Admin Panel Credentials

| Username | Password |
|----------|----------|
| admin    | admin123 |

> **Note:** Change the password after first login in production.

---

## Uploading Media Files

After running the server, upload the following files via the Admin Panel:

### Profile Image
1. Go to Admin → Bio → Bio #1 → Edit
2. Upload `profile.png` in the "Profile Image" field

### Resume PDF
1. Go to Admin → Bio → Bio #1 → Edit
2. Upload `AI_Resume.pdf` in the "Resume (PDF)" field

### Project Screenshots
1. Go to Admin → Projects → Project Screenshots
2. Link each screenshot to its respective project

### Certification Images
1. Go to Admin → Projects → Certifications
2. Upload `Cert1.png`, `Cert2.png`, `Cert3.png`, `RevOps_Cert.png` for each cert

### Case Study PDF
1. Go to Admin → Projects → Case Studies
2. Upload `HubSpot_To_Google_Sheets.pdf` for the case study record

---

## Environment Variables

Copy `.env.example` to `.env` and configure:

```env
SECRET_KEY=your-long-random-secret-key-here
DEBUG=True
ALLOWED_HOSTS=127.0.0.1,localhost
```

---

## Project Architecture (Academic Notes)

### MVT Pattern
| Layer | Component | Purpose |
|-------|-----------|---------|
| **Model** | `apps/*/models.py` | Database schema & ORM |
| **View** | `apps/bio/views.py` | Business logic, data fetching |
| **Template** | `templates/portfolio/index.html` | HTML rendering |

### App Structure
| App | Section | Models |
|-----|---------|--------|
| `apps.bio` | Hero, About, Contact | `Bio` |
| `apps.education` | Education timeline | `Education` |
| `apps.skills` | Skills with progress bars | `Skill` |
| `apps.experience` | Work experience | `Experience`, `Achievement`, `ExperienceTechnology` |
| `apps.projects` | Projects, Certs, Case Studies | `Project`, `ProjectTechnology`, `ProjectScreenshot`, `ProjectFeature`, `Certification`, `CaseStudy` |

### Key Django Features Demonstrated
- ✅ MVT Architecture
- ✅ App separation (5 apps)
- ✅ Database-driven content (NO hardcoded portfolio data)
- ✅ ForeignKey relationships (Experience → Achievements)
- ✅ ImageField & FileField media handling
- ✅ Admin panel with list_display, search_fields, filters
- ✅ Inline admin classes (related records inside parent form)
- ✅ Django ORM queries (filter, prefetch_related)
- ✅ Django fixtures for data seeding
- ✅ Template tags and filters
- ✅ Static files configuration
- ✅ Media files configuration

---

## Production Deployment

For production deployment (e.g., PythonAnywhere, Railway, Render):

```bash
# Install production extras
pip install gunicorn whitenoise

# Set environment
DEBUG=False
ALLOWED_HOSTS=yourdomain.com

# Collect static files
python manage.py collectstatic

# Run with gunicorn
gunicorn portfolio_project.wsgi:application
```

### settings.py changes for production:
```python
DEBUG = False
ALLOWED_HOSTS = ['yourdomain.com']

# Add WhiteNoise for static files
MIDDLEWARE = [
    'whitenoise.middleware.WhiteNoiseMiddleware',
    ...
]
STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'
```
