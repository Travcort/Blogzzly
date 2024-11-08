from django.shortcuts import render
from .models import BlogPost
from django.views import generic

# Create your views here.

class BlogListView(generic.ListView):
    model = BlogPost
    template_name = "index.html"
    context_object_name = "Posts"


class BlogDetailedView(generic.DetailView):
    model = BlogPost
    template_name = 'post.html'
    context_object_name = "post"