from msilib.schema import Class
from pickle import FALSE
from unicodedata import name
from django.db import models
from django.contrib.auth.models import BaseUserManager
from django.contrib.auth.models import PermissionsMixin
from django.contrib.auth.models import AbstractBaseUser
from django.utils.translation import gettext_lazy as _
from datetime import datetime,timedelta

# Create your models here.


class Book(models.Model):
    catchoice = [
        ('education', 'Education'),
        ('entertainment', 'Entertainment'),
        ('comics', 'Comics'),
        ('biography', 'Biography'),
        ('history', 'History'),
        ('novel', 'Novel'),
        ('fantasy', 'Fantasy'),
        ('thriller', 'Thriller'),
        ('romance', 'Romance'),
        ('scifi', 'Sci-Fi'),
    ]
    name = models.CharField(max_length=30)
    isbn = models.PositiveIntegerField()
    author = models.CharField(max_length=40)
    genere = models.CharField(max_length=30, choices=catchoice, default='education')

    def __str__(self):
        return str(self.name)+"["+str(self.isbn)+']'

class CustomAccountManager(BaseUserManager):

    def create_superuser(self, email, password, **other_fields):

        other_fields.setdefault('is_staff', True)
        other_fields.setdefault('is_superuser', True)
        other_fields.setdefault('is_active', True)

        if other_fields.get('is_staff') is not True:
            raise ValueError(
                'Superuser must be assigned to is_staff=True.')
        if other_fields.get('is_superuser') is not True:
            raise ValueError(
                'Superuser must be assigned to is_superuser=True.')

        return self.create_user(email, password, **other_fields)

    def create_user(self, email, password, **other_fields):

        if not email:
            raise ValueError(_('You must provide an email address'))

        email = self.normalize_email(email)
        user = self.model(email=email, **other_fields)
        user.set_password(password)
        user.save()
        return 


class User(AbstractBaseUser, PermissionsMixin):
    
    firstname = models.CharField(max_length=50)    
    lastname = models.CharField(max_length=50)    
    email = models.EmailField(_('email address'), unique=True)
    start_date = models.DateTimeField(auto_now_add=True)
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)

    objects = CustomAccountManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    def __str__(self):
        self.fullname = str(self.firstname)+'_'+str(self.lastname)
        return str(self.fullname)


# class Admin(models.Model):
#     user=models.OneToOneField(User,on_delete=models.CASCADE)
    

#     def __str__(self):
#         self.fullname = str(self.user.firstname)+'_'+str(self.user.lastname)
#         return str(self.fullname)

    # @property
    # def getuserid(self):
    #     return self.user.id


class Student(models.Model):
    catchoice = [
        ('a', 'A'),
        ('b', 'B'),
        ('c', 'C'),
        ('d', 'D'),
    ]
    user=models.OneToOneField(User,on_delete=models.CASCADE)
    roll_no = models.PositiveIntegerField()
    div = models.CharField(max_length=30, choices=catchoice)
    branch = models.CharField(max_length=40)
    
    def __str__(self):
        return str(self.user.firstname)+'['+str(self.roll_no)+'/'+str(self.div)+']'
    
    @property
    def fullname(self):
        return str(self.user.firstname)+' '+ str(self.user.lastname)

    @property
    def rolldiv(self):
        return str(self.roll_no)+'/'+str(self.div)


def get_expiry():
    return datetime.today() + timedelta(days=15)

class IssuedBook(models.Model):
    branch = models.CharField(max_length=30, default='issued')
    isbn=models.CharField(max_length=30)
    issuedate=models.DateField(auto_now=True)
    expirydate=models.DateField(default=get_expiry)
    def __str__(self):
        return self.branch