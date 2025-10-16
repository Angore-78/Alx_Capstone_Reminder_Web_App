from django import forms
from datetime import timedelta
from .models import Task,Priority
from django.contrib.auth.models import User 
from django.contrib.auth.forms import UserCreationForm


class TaskCreate(forms.Form):
    task=forms.CharField(label='Task',max_length=50)
    details=forms.CharField(label='Task Description',required=False,max_length=250)
    duration=forms.IntegerField(
        min_value=1,
        initial=7,
        label='Interlude before deadline',
        help_text='Duration entered should be whole numbers'
    )
    complete=forms.BooleanField(required=False,label='Complete')

    class Meta:
        model=Task
        fields=['task','details','created_at']

    def save(self,commit=True):
        instance=super().save(commit=False)
        days=self.cleaned_data('duration')
        if days is not None:
            instance.due_time=timedelta(days=days)

        if commit:
            instance.save()
        return instance


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
    

    