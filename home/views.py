from django.shortcuts import render
from .models import About

def home_view(request):
    about = About.objects.order_by('-created_at').first()
    return render(request, 'home/about.html', {
        'about': about
    })

def contact_view(request):
    return render(request, 'home/contact.html')
