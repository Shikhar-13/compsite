from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.forms import User
from django import forms

class RegisterUserForm(UserCreationForm):
    first_name=forms.CharField()
    last_name=forms.CharField()
    Email=forms.EmailField()
    Branch= forms.ChoiceField(choices=[('Computer Engineering','Computer engineering')])
    Select_Year = forms.ChoiceField(choices=[ ('second year','Second Year')])

    class Meta:
        model = User
        fields=('username','first_name','last_name','Email','Select_Year','Branch','password1','password2')