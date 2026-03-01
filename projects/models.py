from django.db import models

class ResearchProject(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    photo = models.ImageField(blank=True, upload_to='projects/research')
    url = models.URLField(blank=True)
    button_label = models.CharField(max_length=100, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class SocialProject(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    photo = models.ImageField(blank=True, upload_to='projects/social')
    url = models.URLField(blank=True)
    button_label = models.CharField(max_length=100, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)