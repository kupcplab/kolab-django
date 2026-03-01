from django.urls import path
from . import views

app_name = 'publication'

urlpatterns = [
    path('', views.publication_view, name='publication_list'),
]