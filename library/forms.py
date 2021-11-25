from django import forms
from django.contrib.auth import get_user_model

User = get_user_model()

class AdminSigup(forms.ModelForm):
    first_name = forms.CharField(max_length=20)
    last_name = forms.CharField(max_length=20)
    email = forms.EmailField(help_text='Email')

    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'email', 'password']
