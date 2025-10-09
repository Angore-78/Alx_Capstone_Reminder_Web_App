from django.urls import path
from  . import views


app_name = 'reminders'

urlpatterns=[
    path('<int:id>',views.index,name='base'),
    path('',views.home, name='home'),
    path('tasks/',views.tasks,name='task_list'),
    path('login/',views.login,name='login'),
    path('sign_up/',views.sign_up,name='sign_up'),
    
]
