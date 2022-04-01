from django.test import TestCase

# Create your tests here.
from Game.models import User


class UserModel(TestCase):
    @classmethod
    def setUpTestData(cls):
        # Set up non-modified objects used by all test methods
        User.objects.create(name = "peter", phone = "1234567", email = "peter@gmail.com")

    def test_name_label(self):
        user = User.objects.get(id=1)
        field_label = user._meta.get_field('name').verbose_name
        self.assertEqual(field_label, 'name')
    
    def test_phone_label(self):
        user = User.objects.get(id=1)
        field_label = user._meta.get_field('phone').verbose_name
        self.assertEqual(field_label, 'phone')
    
    def test_email_label(self):
        user = User.objects.get(id=1)
        field_label = user._meta.get_field('email').verbose_name
        self.assertEqual(field_label, 'email')
    
    def test_name_max_length(self):
        user = User.objects.get(id=1)
        max_length = user._meta.get_field('name').max_length
        self.assertEqual(max_length, 200)
    
    def test_phone_max_length(self):
        user = User.objects.get(id=1)
        max_length = user._meta.get_field('phone').max_length
        self.assertEqual(max_length, 200)
    
    def test_email_max_length(self):
        user = User.objects.get(id=1)
        max_length = user._meta.get_field('email').max_length
        self.assertEqual(max_length, 200)