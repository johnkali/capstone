#from django.contrib.auth.models import Person
from django import forms
from .models import Person


class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model=Person
        fields = ['first_name', 'second_name', 'third_name',
                  'email', 'password', ]