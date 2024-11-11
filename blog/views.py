from django.shortcuts import render
from .models import BlogPost
from django.views import generic

# Create your views here.

def home(request):
    return render(request, 'index.html')

class BlogListView(generic.ListView):
    model = BlogPost
    template_name = "Blog.html"
    context_object_name = "Posts"


class BlogDetailedView(generic.DetailView):
    model = BlogPost
    template_name = 'post.html'
    context_object_name = "post"