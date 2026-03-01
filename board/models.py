from django.db import models
from django.contrib.auth.models import User
from django_ckeditor_5.fields import CKEditor5Field

class Notice(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    content = CKEditor5Field('내용', config_name='default')

    photo = models.ImageField(upload_to='notice/photos/', blank=True, null=True)
    file = models.FileField(upload_to='notice/files/', blank=True, null=True)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    is_important = models.BooleanField(default=False)

    class Meta:
        ordering = ['-is_important', '-id']

    def __str__(self):
        return f"{self.id}. {self.title}"

class Column(models.Model):
    title = models.CharField(max_length=200)
    url = models.URLField(blank=False)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    is_important = models.BooleanField(default=False)

    class Meta:
        ordering = ['-is_important', '-id']


    def __str__(self):
        return f"{self.id}. {self.title}"