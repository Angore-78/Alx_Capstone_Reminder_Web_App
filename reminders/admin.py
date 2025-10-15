from django.contrib import admin
from .models import Author,UserManager,Task

admin.site.register(Author)

admin.site.register(Task)
