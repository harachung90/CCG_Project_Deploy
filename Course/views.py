from django.shortcuts import render
from django.views import generic
from .models import Post


class PostList(generic.ListView):
    """
    Return all posts that are with status 1 (published) and order from the latest one.
    """
    queryset = Post.objects.order_by('-created_at')
    template_name = 'course.html'


class PostDetail(generic.DetailView):
    model = Post
    template_name = 'course_post.html'


def courses(request):
    return render(request, 'course.html', {'navbar': 'courses'})
