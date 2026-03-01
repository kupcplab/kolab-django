from django.urls import path
from . import views

app_name = 'projects' 

urlpatterns = [
    path('research/', views.researchproject_list, name='research_projects'),
    path('social/', views.socialproject_list, name='social_projects'),
]