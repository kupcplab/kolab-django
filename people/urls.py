from django.urls import path
from . import views

app_name = 'people'

urlpatterns = [
    path('director/', views.director_view, name='director'),
    path('members/', views.members_list, name='members'),
    path('alumni/', views.alumni_list, name='alumni')
]