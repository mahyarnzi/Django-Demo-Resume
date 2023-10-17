from django.shortcuts import render
from .models import *


def index_view(request):
    profile = Profile.objects.first()
    educations = Education.objects.all().order_by('-start_date')
    experiences = Experience.objects.all().order_by('-start_date')
    technical_skills = TechnicalSkill.objects.all().order_by('created_date')
    languages = Language.objects.all()
    certificates = Certificate.objects.all().order_by('-issue_date')
    honors = Honor.objects.all().order_by('created_date')
    publications = Publication.objects.all().order_by('-publish_date')
    background = Background.objects.filter(name='main').first()
    context = {'profile': profile, 'educations': educations, 'experiences': experiences,
               'technical_skills': technical_skills, 'languages': languages, 'certificates': certificates,
               'honors': honors, 'publications': publications, 'background': background}
    return render(request, 'main/index.html', context)
