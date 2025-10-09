from django import forms
from .models import Task,Priority,Author
from django.contrib.auth.forms import UserCreationForm


class SignUpForm(UserCreationForm):
    username=forms.CharField(max_length=100)
    email=forms.EmailField(max_length=200)
    
    class Meta:
        model=Author
        fields=['username','email','password1','password2',]


class LoginForm(forms.Form):
    username=forms.CharField(max_length=100)
    email = forms.EmailField(max_length=200)
    
    class Meta:
        fields=['username','email']

        
class TaskForm(forms.Form):
    to_do=forms.Textarea()
    
    class Meta:
        model = Task
        fields = ['to_do','details','author']