from django.db import models
from django.contrib.auth.models import User
from CCG_Project import settings

User = settings.AUTH_USER_MODEL

LEVEL = (
    ("Beginner", "Beginner"),
    ("Intermediate", "Intermediate"),
    ("Advanced", "Advanced"),
)


class Quiz(models.Model):
    name = models.CharField(max_length=50)
    num_of_questions = models.IntegerField(default=1)
    score_to_pass = models.IntegerField(help_text="Required score in %", default=67)
    description = models.TextField(default="This is a test quiz.")

    def __str__(self):
        return f'{self.name}'

    def get_questions(self):
        return self.question_set.all()

    class Meta:
        verbose_name_plural = 'Quizzes'


class Question(models.Model):
    num = models.IntegerField(default=1, unique=False)
    total = models.IntegerField(default=6)
    content = models.CharField(max_length=200)
    level = models.CharField(choices=LEVEL, default='Beginner', max_length=30)
    quiz = models.ForeignKey(Quiz, on_delete=models.CASCADE)

    def __str__(self):
        return self.content

    def get_answers(self):
        return self.answer_set.all()

    def get_levels(self):
        return self.level_set.all()


class Answer(models.Model):
    content = models.CharField(max_length=200)
    is_correct = models.BooleanField(default=False)
    question = models.ForeignKey(Question, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.question.content}: {self.content} - {self.is_correct}'


class Mark(models.Model):
    quiz = models.ForeignKey(Quiz, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    score = models.FloatField(default=0)
    user_level = models.CharField(choices=LEVEL, max_length=25, default="Beginner")

    def __str__(self):
        return str(self.quiz)
