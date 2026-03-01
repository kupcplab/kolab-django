from django.db import models

class About(models.Model):
    photo = models.ImageField(blank=True, upload_to='home/about')
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
