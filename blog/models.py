from django.db import models
from django.contrib.auth.models import User
from django.utils.text import slugify
from cloudinary.models import CloudinaryField

class BlogPost(models.Model):
    title = models.CharField(max_length=100, unique=True)
    category = models.CharField(max_length=20)
    thumbnail_text = models.CharField(max_length=50)
    thumbnail_image = CloudinaryField('image', blank=True)
    slug = models.SlugField(max_length=150, unique=True)
    content = models.TextField()
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


    class Meta:
        ordering = ['-created_at']

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super().save(*args, **kwargs)


    def __str__(self):
        return self.title