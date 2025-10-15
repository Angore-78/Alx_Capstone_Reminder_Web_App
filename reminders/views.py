from django.shortcuts import render,redirect
from django.http import HttpResponse,HttpResponseRedirect
from .models import Task
from django.contrib.auth import login,authenticate
from django.contrib.auth.forms import UserCreationForm
from .forms import LoginForm,SignUpForm,TaskForm


def index(request):
    return render(request,'reminders/task_list.html',{})


def home(request):
    return render(request,'reminders/home.html',{})


def tasks(request):
    if request.method=='POST':
        form =TaskForm(request.POST)
        if form.is_valid():
            clean=form.cleaned_data['to_do']
            task=Task(name=clean)
            task.save()
        return HttpResponseRedirect("/%i" %task.id)
    else:
        task = Task.objects.all()
    context = {'task':task}
    return render(request,'reminders/to_do.html',context)

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
            return redirect("")
    else:
        form=SignUpForm
    return render(request,'registration/sign_up.html',{'form':form})
