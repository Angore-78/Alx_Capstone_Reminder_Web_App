from django import forms
from .models import Task,Priority
from django.contrib.auth.models import User 
from django.contrib.auth.forms import UserCreationForm


class SignUpForm(UserCreationForm):
    email=forms.EmailField()

    class Meta:
        model=User
        fields=['username','email','password1','password2']


class LoginForm(forms.Form):
    username=forms.CharField(max_length=100,label='Username')
    password=forms.CharField(max_length=200,label='Password')
    email = forms.EmailField(widget=forms.PasswordInput,label='Email')
    
    class Meta:
        fields=['username','email','password']


        
class TaskForm(forms.Form):
    to_do=forms.CharField(label='Tasks',max_length=30)
    details=forms.CharField(label='Task Description',max_length=250)
    duration=forms.IntegerField(label='Time before deadline')
    

    