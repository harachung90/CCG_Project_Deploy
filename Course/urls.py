from . import views
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

app_name = 'course_app'

urlpatterns = [
    path('course/', views.PostList.as_view(), name='course'),
    path('course/<slug:slug>/', views.PostDetail.as_view(), name='course_posts'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
