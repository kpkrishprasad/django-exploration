# todo/todo_api/urls.py : API urls.py
# from django.conf.urls import url
from django.urls import path, include
from todo_api.view import TodoDetailApiView
from .views import (
    TodoListApiView,
)

urlpatterns = [
    path('api', TodoListApiView.as_view()),
    path('api/<int:todo_id>/', TodoDetailApiView.as_view()),

]
