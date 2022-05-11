from django.db import models
from django.contrib.auth.models import User

CATEGORY = (
    ("Beginner", "Beginner"),
    ("Intermediate", "Intermediate"),
    ("Advanced", "Advanced"),
)


class Post(models.Model):
    title = models.CharField(max_length=300, unique=True)
    slug = models.SlugField(max_length=300, unique=True)
    content = models.TextField(default='')

    category = models.CharField(max_length=25, choices=CATEGORY, default=0)

    created_at = models.DateField(auto_now_add=True)

    class Meta:
        ordering = ['created_at']

    def __str__(self):
        return self.title
