from . import views
from django.urls import path, include

app_name = 'course_app'

urlpatterns = [
    path('course/', views.PostList.as_view(), name='course'),
    path('course/<slug:slug>/', views.PostDetail.as_view(), name='course_posts'),
    path('summernote/', include('django_summernote.urls')),
]
