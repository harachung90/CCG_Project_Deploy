from django.shortcuts import render, redirect, get_object_or_404
from django.http import JsonResponse
from django.contrib.auth.models import User
from django.views.generic import ListView
from .models import Quiz, Question, Answer, Mark


# Create your views here.
def index(request):
    return render(request, 'index.html', {'navbar': 'index'})


def congratulations(request):
    return render(request, 'congratulations.html', {'navbar': 'congratulations'})


# def quiz_list(request):
#     quizzes = Quiz.objects.all()
#
#     context = {
#         'quizzes': quizzes,
#     }
#
#     return render(request, 'quiz_list.html', context=context)
#
# def quiz(request, myid):
#
#     quiz = Quiz.objects.get(id=myid)
#
#     context = {
#         'quiz': quiz,
#     }
#
#     return render(request, 'quiz.html', context=context)

class QuizListView(ListView):
    model = Quiz
    template_name = 'quiz_list.html'


def quiz_view(request, myid):
    quiz = Quiz.objects.get(id=myid)

    context = {
        'quiz': quiz,
    }

    return render(request, 'quiz.html', context=context)


def quiz_data_view(request, myid):
    quiz = Quiz.objects.get(id=myid)
    questions = []
    for q in quiz.get_questions():
        answers = []
        for a in q.get_answers():
            answers.append(a.content)
        questions.append({str(q): answers})
    return JsonResponse({
        'data': questions,
    })


def save_quiz_view(request, myid):
    if request.is_ajax():
        questions = []
        data = request.POST
        data_ = dict(data.lists())

        data_.pop('csrfmiddlewaretoken')

        for k in data_.keys():
            print('key: ', k)
            question = Question.objects.get(content=k)
            questions.append(question)

        user = request.user
        quiz = Quiz.objects.get(id=myid)

        score = 0
        total = quiz.num_of_questions
        multiplier = 100 / total
        marks = []
        correct_answer = None

        for q in questions:
            a_selected = request.POST.get(q.content)

            if a_selected != "":
                question_answers = Answer.objects.filter(question=q)
                for a in question_answers:
                    if a_selected == a.content:
                        if a.is_correct:
                            score += 1
                            correct_answer = a.content

                    else:
                        if a.is_correct:
                            correct_answer = a.content

                marks.append({str(q): {'correct_answer': correct_answer, 'answered': a_selected}})
            else:
                marks.append({str(q): 'not answered'})

        score_num = score
        wrong_num = total - score_num
        score_percent = int(score * multiplier)
        name = user.first_name + " " + user.last_name
        user_level = ""

        if score_percent >= int(2 / 3 * 100):
            user_level = "Advanced"
            passed = True
        elif score_percent > int(1 / 3 * 100) & score_percent < int(2 / 3 * 100):
            user_level = "Intermediate"
            passed = False
        else:
            user_level = "Beginner"
            passed = False

        Mark.objects.create(quiz=quiz, user=user, score=score_percent, user_level=user_level)

    return JsonResponse({'passed': passed, 'score_num': score_num, 'score_percent': score_percent,
                         'total': total, 'marks': marks, 'name': name, 'user_level': user_level,
                         'wrong_num': wrong_num})
