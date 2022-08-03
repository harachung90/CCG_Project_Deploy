from django_summernote.admin import SummernoteModelAdmin
from django.contrib import admin
from .models import Quiz, Question, Answer, Mark


class AnswerInLine(admin.TabularInline):
    model = Answer

class AnswerAdmin(admin.ModelAdmin):
    list_display = ('question', 'content', 'question')
    search_fields = ('question', 'content', 'question')


class QuestionAdmin(admin.ModelAdmin):
    inlines = [AnswerInLine]

class QuestionAdmin(admin.ModelAdmin):
    list_display = ('num', 'content', 'level', 'quiz')
    search_fields = ('num', 'content', 'level', 'quiz')


admin.site.register(Question, QuestionAdmin)
admin.site.register(Answer, AnswerAdmin)


class QuizAdmin(admin.ModelAdmin):
    list_display = ('name', 'num_of_questions', 'score_to_pass')
    search_fields = ('name', 'num_of_questions', 'score_to_pass')


class QuizAdmin(SummernoteModelAdmin):
    list_display = ('name', 'num_of_questions', 'score_to_pass')
    search_fields = ('name', 'num_of_questions', 'score_to_pass')
    summernote_fields = ('description',)


class MarkAdmin(admin.ModelAdmin):
    list_display = ('quiz', 'user', 'score', 'user_level', 'passed')
    search_fields = ('quiz', 'user', 'score', 'user_level', 'passed')


admin.site.register(Mark, MarkAdmin)
admin.site.register(Quiz, QuizAdmin)
