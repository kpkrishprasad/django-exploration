# todo/todo_api/urls.py : API urls.py
# from django.conf.urls import url
from django.urls import path, include
from .views.todo import (
    TodoView, 
    TodoListView
)

urlpatterns = [
    path('api', TodoListView.as_view()),
    path('api/<int:todo_id>/', TodoView.as_view()),


]
