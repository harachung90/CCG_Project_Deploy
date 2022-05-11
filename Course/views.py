from django.shortcuts import render
from django.views import generic
from .models import Post
from django.contrib.auth.mixins import LoginRequiredMixin


class PostList(LoginRequiredMixin, generic.ListView):
    """
    Return all posts that are with status 1 (published) and order from the latest one.
    """
    queryset = Post.objects.order_by('-created_at')
    template_name = 'course.html'
    login_url = '/login'

    def get_queryset(self):
        return Post.objects.all()

    def get_context_data(self, **kwargs):
        context = super(PostList, self).get_context_data(**kwargs)
        context['navbar'] = 'courses'
        return context


class PostDetail(LoginRequiredMixin, generic.DetailView):
    model = Post
    template_name = 'course_post.html'
    login_url = '/login'

    def get_context_data(self, **kwargs):
        context = super(PostDetail, self).get_context_data(**kwargs)
        context['navbar'] = 'courses'
        return context


def courses(request):
    return render(request, 'course.html', {'navbar': 'courses'})
