from django import forms
from django.contrib.auth import get_user_model
from . import models


User = get_user_model()

class UserForm(forms.ModelForm):
    class Meta:
        model = models.User
        fields = ['firstname','lastname', 'email', 'password']

class BookForm(forms.ModelForm):
    class Meta:
        model = models.Book
        fields=['name','isbn','author','genere']

# class AdminUserForm(forms.ModelForm):
#     class Meta:
#         model = models.User
#         fields=['firstname','lastname','email','password']

class StudentUserForm(forms.ModelForm):
    class Meta:
        model = models.User
        fields=['firstname','lastname','email','password']

class StudentForm(forms.ModelForm):
    class Meta:
        model = models.Student
        fields=['roll_no','div','branch']