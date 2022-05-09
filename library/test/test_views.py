from urllib import response
from django.test import TestCase, Client
from django.urls import reverse
from django.contrib.auth.models import User, Group
from django.utils.timezone import now
from django.contrib.auth import get_user_model

#Test Views here

class TestViews(TestCase):
    def test_index(self):
        client = Client()
        response = client.get(reverse('index'))
        self.assertTemplateUsed(response, 'library/index.html')

# class TestAdmin(TestCase):
#     def test_signup(self):
#         user = User.objects.create_user(username="User", first_name="Fname", last_name="Lname", email="e@mail.com", start_date=now,  is_staff=False, is_active=True)
#         self.assertEqual(user.count(), 1)
#         response = self.client.get("adminsignup")
#         self.assertTemplateUsed(response, template_name='adminsignup.html')