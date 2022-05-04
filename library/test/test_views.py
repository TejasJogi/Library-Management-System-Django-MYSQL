from django.test import TestCase, Client
from django.urls import reverse

#Test Views here

class TestIndex(TestCase):
    def test_index(self):
        client = Client()
        response =client.get(reverse('index'))
        self.assertTemplateUsed(response, 'library/index.html')