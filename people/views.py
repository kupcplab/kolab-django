from django.shortcuts import render
from .models import Director, Member

def director_view(request):
    director = Director.objects.order_by('-created_at').first()
    return render(request, 'people/director/director.html', {
        'director': director
    })

def members_list(request):
    undergrads = Member.objects.filter(degree='undergrad', graduate=False).order_by('name')
    masters = Member.objects.filter(degree='master', graduate=False).order_by('name')
    phds = Member.objects.filter(degree='phd', graduate=False).order_by('name')

    return render(request, 'people/members/members_list.html', {
        'undergrads_list' : undergrads,
        'masters_list': masters,
        'phds_list': phds,
    })

def alumni_list(request):
    masters = Member.objects.filter(degree='master', graduate=True).order_by('name')
    phds = Member.objects.filter(degree='phd', graduate=True).order_by('name')

    return render(request, 'people/alumni/alumni_list.html', {
        'masters_list': masters,
        'phds_list': phds,
    })