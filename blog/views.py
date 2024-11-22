from django.shortcuts import render
from .models import BlogPost
from django.views import generic
from django.conf import settings
from django.contrib.admin.views.decorators import staff_member_required
from django.views.decorators.http import require_http_methods
from django.http import JsonResponse
from django.core.mail import send_mail

# Tiny
@staff_member_required
@require_http_methods(['GET'])
def get_tiny(request):
    key = getattr(settings, 'TINY_KEY', 'Key not Defined!')
    if not key:
        return JsonResponse({'Error': 'TinyMCE key is not configured. Please contact the SysAdmin.'})
    return JsonResponse({'key': key})

def home(request):
    return render(request, 'index.html')

def contacts(request):
    return render(request, 'Contact.html')

def contact_me(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        message = request.POST.get('message')

        full_email = f"Name: {name}\nEmail: {email}\nMessage: \n{message}"

        send_mail(
            subject = 'Bloggy Contact Form User',
            message = full_email, 
            from_email = settings.EMAIL_HOST_USER, 
            recipient_list = ['tarvkoome@gmail.com']
        )

    return render(request, 'Success.html')

class BlogListView(generic.ListView):
    model = BlogPost
    template_name = "Blog.html"
    context_object_name = "Posts"


class BlogDetailedView(generic.DetailView):
    model = BlogPost
    template_name = 'Post.html'
    context_object_name = "post"