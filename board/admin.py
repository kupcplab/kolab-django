from django.contrib import admin
from .models import Notice, Column

@admin.register(Notice)
class NoticeAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'author', 'created_at')
    list_filter = ('author',)
    search_fields = ('title', 'content')
    ordering = ('-is_important', '-id',)

@admin.register(Column)
class ColumnAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'created_at')
    search_fields = ('title',)
    ordering = ('-is_important', '-id',)