from django.db import models
from django.contrib.auth.models import User
from ckeditor_uploader.fields import RichTextUploadingField
from ckeditor.fields import RichTextField

CATEGORY = (
    ("Beginner", "Beginner"),
    ("Intermediate", "Intermediate"),
    ("Advanced", "Advanced"),
)


class Post(models.Model):
    title = models.CharField(max_length=300, unique=True)
    slug = models.SlugField(max_length=300, unique=True)
    # author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='course_posts')
    content = RichTextField(blank=True, null=True)
    # content = RichTextUploadingField(blank=True, null=True)

    category = models.CharField(max_length=25, choices=CATEGORY, default=0)

    created_at = models.DateField(auto_now_add=True)

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return self.title
