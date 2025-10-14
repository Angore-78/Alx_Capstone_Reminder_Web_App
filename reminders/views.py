from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.views.generic import ListView,DetailView
from .models import Task
from django.contrib.auth.forms import UserCreationForm
from .forms import LoginForm,SignUpForm


def index(request,id):
    task = Task.objects.get(id = id)
   # detail=Task.objects.get(details=details)
    return HttpResponse("<h1>%s</h1><br></br><p1>%s</p1>"%(task.id))


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
            return n
    else:
     form = LoginForm
     return render(request,'registration/login.html',{'form':form})

def sign_up(request):
    if request.method=='POST':
        form=UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("/home")
    else:
        form=UserCreationForm
    return render(request,'registration/sign_up.html',{'form':form})
