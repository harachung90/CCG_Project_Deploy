from django.urls import path, include
from Quiz import views
from .views import QuizListView

app_name = 'quiz_app'

urlpatterns = [
    path('congratulations/', views.congratulations, name='congratulations'),
    path('quiz_list/', QuizListView.as_view(), name='quiz_list'),
    path('quiz_list/<int:myid>/', views.quiz_view, name="quiz"),
    path('quiz_list/<int:myid>/data/', views.quiz_data_view, name='quiz-data'),
    path('quiz_list/<int:myid>/save/', views.save_quiz_view, name='quiz-save'),
    path('quiz_list/sample', views.quiz_sample, name='quiz_sample'),
]
