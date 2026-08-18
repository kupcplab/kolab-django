from django.db import models
from django_ckeditor_5.fields import CKEditor5Field


class Publication(models.Model):
    publication = CKEditor5Field('출판 목록', config_name='default')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return "Publications"


class Book(models.Model):
    book = CKEditor5Field('도서 목록', config_name='default')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return "Books"
