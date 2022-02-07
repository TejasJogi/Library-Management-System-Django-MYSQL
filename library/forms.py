from django import forms
from django.contrib.auth import get_user_model
from . import models


User = get_user_model()


class UserForm(forms.ModelForm):
    class Meta:
        model = models.User
        fields = ['firstname', 'lastname', 'email', 'password']


class BookForm(forms.ModelForm):
    class Meta:
        model = models.Book
        fields = ['name', 'isbn', 'author', 'genere']

# class AdminUserForm(forms.ModelForm):
#     class Meta:
#         model = models.User
#         fields=['firstname','lastname','email','password']


class StudentUserForm(forms.ModelForm):
    class Meta:
        model = models.User
        fields = ['firstname', 'lastname', 'email', 'password']


class StudentForm(forms.ModelForm):
    class Meta:
        model = models.Student
        fields = ['roll_no', 'div', 'branch']


class BookissueForm(forms.Form):
    isbn2 = forms.ModelChoiceField(queryset=models.Book.objects.all(
    ), empty_label="Name and ISBN", to_field_name="isbn", label='Name and Isbn')
    branch2 = forms.ModelChoiceField(queryset=models.Student.objects.all(
    ), empty_label="Name and Roll no.", to_field_name='roll_no', label='Name and Roll no.')
