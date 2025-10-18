import datetime
from django.db import models
from django.contrib.auth.models import AbstractBaseUser,BaseUserManager
from django.urls import reverse


class UserManager(BaseUserManager):
    def create_author(self,email,username,password):
        user=self.model(
            email=self.normalize_email(email),
            username=username
        )
        user.set_password=(password)
        user.save()
        return user
    

    def create_superuser(self,email,username,password):
        user=self.model(
            email=email,
            username=username,
            password=password
        )
        user.is_staff=True
        user.is_superuser=True
        user.save()
        return user
        
        
class Author(AbstractBaseUser):
    username=models.CharField(max_length=100,unique=True)
    email=models.EmailField(max_length=100,unique=True)
    is_staff=models.BooleanField(default=False)
    is_active=models.BooleanField(default=True)
    is_superuser=models.BooleanField(default=False)

    USERNAME_FIELD='email'
    REQUIRED_FIELDS=['username']

    objects=UserManager()

    def __str__(self):
        return self.username
        

class Task(models.Model):
    to_do = models.CharField(max_length=50)
    details=models.TextField()
    duration=models.IntegerField(
        default=5,
        help_text="Input a specific number for whole days before the task's deadline"
    )
    added_on=models.DateTimeField(auto_now_add=True)
        

    def __str__(self):
        self.time_left=self.added_on + datetime.timedelta(days=self.duration)
        return f'{self.to_do} :> {self.details}\n {self.time_left}'



class Priority(models.Model):
    to_do = models.ForeignKey(Task, on_delete=models.PROTECT)
    priority = models.IntegerField(default=1)

    class Meta:
        verbose_name_plural='Priorities'

    def __str__(self):
        return f"{self.to_do} of priority {self.priority}"
