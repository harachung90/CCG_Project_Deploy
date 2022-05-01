from . import views
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

app_name = 'course_app'

urlpatterns = [
    path('course/', views.PostList.as_view(), name='course'),
    path('course/<slug:slug>/', views.PostDetail.as_view(), name='course_posts'),
    # path('summernote/', include('django_summernote.urls')),
    # path('editor/<id>/', SummernoteEditor.as_view(),
    #      name='django_summernote-editor'),
    path('ckeditor/', include('ckeditor_uploader.urls')),
]
