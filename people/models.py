from django.db import models

class Director(models.Model):
    photo = models.ImageField(blank=True, upload_to='people/director')
    introduction = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class Member(models.Model):

    DEGREE_CHOICES = [
        ('undergrad', '학부'),
        ('master', '석사'),
        ('phd', '박사'),
    ]

    name = models.CharField(max_length=200)
    photo = models.ImageField(blank=True, upload_to='people/members')
    introduction = models.TextField()
    graduate = models.BooleanField(default=False)

    degree = models.CharField(
        max_length=10,
        choices=DEGREE_CHOICES,
        blank=False,
        null=False
    )

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name