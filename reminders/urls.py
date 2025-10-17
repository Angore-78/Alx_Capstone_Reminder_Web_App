from django.urls import path
from  . import views


app_name = 'reminders'

urlpatterns=[
    path('list/',views.index,name='tasks'),
    path('',views.home, name='home'),
    path('to_do/',views.tasks,name='to_do'),
    path('login/',views.login,name='login'),
    path('sign_up/',views.sign_up,name='sign_up'),
    path('create/',views.create,name='create')    
]
