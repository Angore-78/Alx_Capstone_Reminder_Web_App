from django.shortcuts import render,redirect
from django.http import HttpResponse,HttpResponseRedirect
from .models import Task
from django.contrib.auth import login,authenticate
from django.contrib.auth.forms import UserCreationForm
from .forms import LoginForm,SignUpForm,TaskForm,TaskCreate


def index(request):
    task=Task.objects.all()
    return render(request,'reminders/task_list.html',{'tasks':task})


def home(request):
    return render(request,'reminders/home.html',{})



def create(request):
    if request.method=='POST':
        form=TaskCreate(request.POST)
        if form.is_valid():
            name=form.cleaned_data['task']
            output=Task(name=name)
            output.save()
    
    else:
        form=TaskCreate()
    return render(request,'reminders/create.html',{'form':form})



def tasks(request):
    if request.method=='POST':
        form =TaskForm(request.POST)
        if form.is_valid():
            clean=form.cleaned_data['to_do']
            task=Task(name=clean)
            task.save()
            return HttpResponseRedirect("/%i" %task.id)
    else:
        task = TaskForm()
    return render(request,'reminders/create.html',{'task':task})


def login(request):
    if request.method=='POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            n=form.cleaned_data['username']
        return redirect(" ")
    else:
     form = LoginForm
     return render(request,'registration/login.html',{'form':form})



def sign_up(request):
    if request.method=='POST':
        form=SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            
    else:
        form=SignUpForm
    return render(request,'registration/sign_up.html',{'form':form})
