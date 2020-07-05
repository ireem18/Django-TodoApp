from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('',views.index, name='index'),
    path('addTodo/',views.addTodo, name='addTodo'),
    path('todoList/',views.todoList, name='todoList'),
    path('todoEdit/<int:id>/',views.todoEdit, name='todoEdit'),
    path('todoDelete/<int:id>/',views.todoDelete, name='todoDelete'),
    path("todo_completed/<int:id>/", views.todo_completed, name="todo_completed"),
    path("todo_no_completed/<int:id>/", views.todo_no_completed, name="todo_no_completed"),

]