from django.contrib import admin
from .models import About

@admin.register(About)
class AboutAdmin(admin.ModelAdmin):
    list_display = ['photo', 'description', 'created_at', 'updated_at']
    list_display_links = ['photo']