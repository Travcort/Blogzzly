from django.contrib import admin
from blog.models import BlogPost

class BlogPostAdmin(admin.ModelAdmin):
    list_display = ['title', 'category', 'author', 'created_at']
    search_fields = ['title']
    ordering = ['-created_at']



admin.site.register(BlogPost, BlogPostAdmin)