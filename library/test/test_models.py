from django.test import TestCase
from library.models import Book

#Test Models here

class TestModels(TestCase):

    def test_create_book(self):
        book = Book.objects.create(name="Testbook", isbn=1234, author="Testauthor", genere="Testgenere")
        book.save()
        # self.assertTrue(isinstance(book, Book))
        self.assertEqual(book.__str__(), str(book.name)+"["+str(book.isbn)+']')