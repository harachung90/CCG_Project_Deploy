from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('admin/', admin.site.urls),
    path('', include('Quiz.urls', namespace='quiz_app')),
    path('', include('Course.urls', namespace='course_app')),
    path('', include('Account.urls', namespace='account_app')),
    path('summernote/', include('django_summernote.urls')),
]
