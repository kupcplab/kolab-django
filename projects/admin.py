from django.contrib import admin
from .models import ResearchProject, SocialProject

@admin.register(ResearchProject)
class ResearchProjectAdmin(admin.ModelAdmin):
    list_display = ['title', 'description', 'photo', 'created_at', 'updated_at']
    list_display_links = ['title']
    search_fields = ['title']

@admin.register(SocialProject)
class SocialProjectAdmin(admin.ModelAdmin):
    list_display = ['title', 'description', 'photo', 'created_at', 'updated_at']
    list_display_links = ['title']
    search_fields = ['title']