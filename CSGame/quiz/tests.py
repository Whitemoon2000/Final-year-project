from django.test import TestCase
from numpy import require

# Create your tests here.
from quiz.models import Quiz

def setUpTestData(cls):
        # Set up non-modified objects used by all test methods
        Quiz.objects.create(name = "Math", topic = "1+1", 
        number_of_questions = 3, time = 3, 
        required_score_to_pass = 50, difficulty = "easy")