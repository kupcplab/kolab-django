from django.contrib import admin
from .models import Director, Member

@admin.register(Director)
class DirectorAdmin(admin.ModelAdmin):
    list_display = ['photo', 'introduction', 'created_at', 'updated_at']
    list_display_links = ['photo']

@admin.register(Member)
class MemberAdmin(admin.ModelAdmin):
    list_display = ['name', 'introduction', 'graduate', 'degree', 'created_at', 'updated_at']
    list_display_links = ['name']