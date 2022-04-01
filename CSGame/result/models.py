from django.db import models
from quiz.models import Quiz
from django.contrib.auth.models import User
# This is the result model for store the quiz result into database
class Result(models.Model):
    quiz = models.ForeignKey(Quiz, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    score = models.FloatField()

    def __str__(self):
        return str(self.pk)