from django_summernote.admin import SummernoteModelAdmin
from django.contrib import admin
from .models import Quiz, Question, Answer, Mark


# class AnswerInLine(admin.TabularInline):
#     model = Answer
#
#
# class QuestionAdmin(admin.ModelAdmin):
#     inlines = [AnswerInLine]


class AnswerInLine(admin.TabularInline):
    model = Answer

class QuestionAdmin(admin.ModelAdmin):
    list_display = ('name', 'num_of_questions', 'score_to_pass')
    search_fields = ('name', 'num_of_questions', 'score_to_pass')


class QuestionAdmin(SummernoteModelAdmin):
    list_display = ('name', 'num_of_questions', 'score_to_pass')
    search_fields = ('name', 'num_of_questions', 'score_to_pass')
    summernote_fields = ('description',)


admin.site.register(Quiz)
admin.site.register(Question, QuestionAdmin)
admin.site.register(Answer)
admin.site.register(Mark)