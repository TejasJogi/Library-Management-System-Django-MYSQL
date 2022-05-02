from django.test import TestCase
from library.models import Book, IssuedBook, User, Student, get_expiry
from django.utils.timezone import now
from datetime import datetime, timedelta
from django.contrib.auth import get_user_model


#Test Models here

class TestBook(TestCase):

    def test_create_book(self):
        book = Book.objects.create(name="Testbook", isbn=1234, author="Testauthor", genere="Testgenere")
        book.save()
        self.assertEqual(book.__str__(), str(book.name)+"["+str(book.isbn)+']')

class TestUser(TestCase):
    def test_create_user(self):
        user = User.objects.create(username="User", first_name="Fname", last_name="Lname", email="e@mail.com", start_date=now,  is_staff=False, is_active=True)
        self.assertEqual(user.__str__(), str(user.first_name)+'_'+str(user.last_name))
        self.assertEqual(user.get_email(), user.email)

class TestStudent(TestCase):
    def test_create_student(self):
        student = Student.objects.create(user=User.objects.create(username="User", first_name="Fname", last_name="Lname", email="e@mail.com", start_date=now,  is_staff=False, is_active=True), roll_no=1, div="A", branch="Computers")
        self.assertEqual(student.__str__(), str(student.user.first_name)+'['+str(student.roll_no)+'/'+str(student.div)+']')
        self.assertEqual(str(student.fullname), str(student.user.first_name)+' '+ str(student.user.last_name))
        self.assertEqual(str(student.rolldiv), str(student.roll_no)+'/'+str(student.div))

class TestExpiry(TestCase):
    def test_get_expiry(self): 
        self.assertEqual(get_expiry(), datetime.today() + timedelta(days=15))

class TestIssuedBook(TestCase):
    def test_issued_book(self):
        issuedBook = IssuedBook.objects.create(branch="testbranch", isbn=1, issuedate=now, expirydate=get_expiry())
        self.assertEqual(issuedBook.__str__(),str(issuedBook.branch))

class TestCustomAccountManager(TestCase):
    def test_create_user(self):
        user = User.objects.create_user(email='test@email.com', password='password@123')
        self.assertRaises(ValueError, User.objects.create_user, email='', password='password@123')

    def test_create_superuser(self):
        User = get_user_model()
        superuser = User.objects.create_superuser(email='test@email.com', password='password@123')

        with self.assertRaisesMessage(ValueError, 'Superuser must be assigned to is_staff=True.'):
            User.objects.create_superuser(email='test@email.com', password='password@123', is_staff=False)
        
        with self.assertRaisesMessage(ValueError, 'Superuser must be assigned to is_superuser=True.'):
           User.objects.create_superuser(email='test@email.com', password='password@123', is_superuser=False)