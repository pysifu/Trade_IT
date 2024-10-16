from django.test import TestCase
from users.models import User
import datetime
import os
import django

django.setup()


class TestUserModel(TestCase):
    
    def create_test_user(self, 
                         username='CustomTestUser1', 
                         first_name='Jan', 
                         last_name='Kowalski',
                         email='test@user.com',
                         phone_number='123123123',
                         birthday=datetime.date.today(),
                         password1='Koman667?!',
                         password2='Koman667?!'):
        return User.objects.create(username=username,
                                   first_name=first_name,
                                   last_name=last_name,
                                   email=email,
                                   phone_number=phone_number,
                                   birthday=birthday,
                                   password1=password1,
                                   password2=password2)
    
    def test_user_creation(self):
        user_obj = self.create_test_user()
        self.assertTrue(isinstance(User, user_obj))
        self.assertEqual(user_obj.first_name, 'Jan')