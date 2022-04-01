from django.db import models
from quiz.models import Quiz
#This is the question model for store into database
class Question(models.Model):
    # It contain question text, which quiz and when it created
    text = models.CharField(max_length=200)
    quiz = models.ForeignKey(Quiz, on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.text)
    # The choices of this question
    def get_answers(self):
        return self.answer_set.all()

# This is the Answer model for store into database
class Answer(models.Model):
    text = models.CharField(max_length=200)
    correct = models.BooleanField(default=False)
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"question: {self.question.text}, answer: {self.text}, correct: {self.correct}"