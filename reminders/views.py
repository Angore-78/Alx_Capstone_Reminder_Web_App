from django.shortcuts import render
from django.views.generic import ListView,DetailView
from .models import Task
from .forms import LoginForm,SignUpForm


def index(request,id):
    task = Task.objects.get(id = id)
    return render(request,'reminders/base.html',{})


def home(request):
    return render(request,'reminders/home.html',{})


def tasks(request):
    task = Task.objects.get(task=Task.to_do)
    context = {'task':task}
    return render(request,'reminders/task_list.html',context)

def login(request):
    if request.method=='POST':
        form = LoginForm(request.Post)
        if form.is_valid():
            n=form.cleaned_data['username']
    
    else:
     form = LoginForm
     return render(request,'registration/login.html',{'form':form})

def sign_up(request):
    form=SignUpForm
    return render(request,'registration/sign_in.html')
