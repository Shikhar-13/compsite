from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.forms import User
from django import forms
from django.core.exceptions import ValidationError

class RegisterUserForm(UserCreationForm):
    first_name=forms.CharField()
    last_name=forms.CharField()
    email=forms.EmailField()
    Branch= forms.ChoiceField(choices=[('',''),('Computer Engineering','Computer engineering'),('IT','IT')])
    Select_Year = forms.ChoiceField(choices=[('', ''), ('first year', 'First Year'), ('second year','Second Year')])

    class Meta:
        model = User
        fields=('username','first_name','last_name','email','Select_Year','Branch','password1','password2')
    
    def clean(self):
       email = self.cleaned_data.get('email')
       if User.objects.filter(email=email).exists():
            raise ValidationError("Email exists")
       return self.cleaned_data