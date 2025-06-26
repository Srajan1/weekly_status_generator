from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('tasks/<uuid:task_id>', views.task, name='views.task'),
    path('tasks/', views.tasks, name='views.tasks'),
]