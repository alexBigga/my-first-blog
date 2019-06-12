from django.shortcuts import render
from django.utils import timezone
from .models import Post

# Create your views here.

def post_list(request):
    # posts: Query-Set
    posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    # request: Anfrage vom user
    # blog/post_list.html: Template
    # {}: Zur Verwendung durch das Template, hier posts
    return render(request, 'blog/post_list.html', {'posts': posts})
