from django.test import TestCase
from library.models import Book, User, Student
from django.utils.timezone import now
from django.contrib.auth import get_user_model
from datetime import datetime
from datetime import timedelta

#Test Models here

class TestModels(TestCase):

    def test_create_book(self):
        book = Book.objects.create(name="Testbook", isbn=1234, author="Testauthor", genere="Testgenere")
        book.save()
        # self.assertTrue(isinstance(book, Book))
        self.assertEqual(book.__str__(), str(book.name)+"["+str(book.isbn)+']')

    def test_create_user(self):
        user = User.objects.create(username="User", first_name="Fname", last_name="Lname", email="e@mail.com", start_date=now,  is_staff=False, is_active=True)
        self.assertEqual(user.__str__(), str(user.first_name)+'_'+str(user.last_name))
        self.assertEqual(user.get_email(), user.email)

    def test_create_student(self):
        student = Student.objects.create(user=User.objects.create(username="User", first_name="Fname", last_name="Lname", email="e@mail.com", start_date=now,  is_staff=False, is_active=True), roll_no=1, div="A", branch="Computers")
        self.assertEqual(student.__str__(), str(student.user.first_name)+'['+str(student.roll_no)+'/'+str(student.div)+']')
        self.assertEqual(str(student.fullname), str(student.user.first_name)+' '+ str(student.user.last_name))
        self.assertEqual(str(student.rolldiv), str(student.roll_no)+'/'+str(student.div))