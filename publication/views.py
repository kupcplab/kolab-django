from django.shortcuts import render
from .models import Publication

def publication_view(request):
    publication = Publication.objects.order_by('-created_at').first()
    return render(request, 'publication/publication_list.html', {
        'publication': publication
    })
