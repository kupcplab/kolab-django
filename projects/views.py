from django.shortcuts import render
from .models import ResearchProject, SocialProject

def researchproject_list(request):
    qs = ResearchProject.objects.all()
    return render(request, 'projects/research/researchproject_list.html', {
        'researchproject_list' : qs,
    })

def socialproject_list(request):
    qs = SocialProject.objects.all()
    return render(request, 'projects/social/socialproject_list.html', {
        'socialproject_list' : qs,
    })
