from django import forms
from django.contrib.auth import get_user_model
from . import models


User = get_user_model()

class AdminSigup(forms.ModelForm):
    class Meta:
        model = models.User
        fields = ['firstname','lastname', 'email', 'password']

class BookForm(forms.ModelForm):
    class Meta:
        model = models.Book
        fields=['name','isbn','author','genere']

class StudentUserForm(forms.ModelForm):
    class Meta:
        model = models.User
        fields=['firstname','lastname','email','password']

class StudentForm(forms.ModelForm):
    class Meta:
        model = models.Student
        fields=['roll_no','div','branch']