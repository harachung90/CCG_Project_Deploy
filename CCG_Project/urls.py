from django.contrib import admin
from django.urls import path, include
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.index, name=''),
    path('admin/', admin.site.urls),
    path('', include('Quiz.urls', namespace='quiz_app')),
    path('', include('Course.urls', namespace='course_app')),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
