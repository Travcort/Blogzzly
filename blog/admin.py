from django.contrib import admin
from django import forms
from blog.models import BlogPost

class PostAdminForm(forms.ModelForm):
    class Meta:
        model = BlogPost
        fields = '__all__'
        widgets = {
            'content': forms.Textarea(attrs={'id': 'id_content'})
        }

class BlogPostAdmin(admin.ModelAdmin):
    form = PostAdminForm
    list_display = ['title', 'category', 'author', 'created_at']
    search_fields = ['title']
    ordering = ['-created_at']

    class Media:
        js = (
            'js/tiny.js',
        )



admin.site.register(BlogPost, BlogPostAdmin)