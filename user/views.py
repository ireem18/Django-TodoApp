from cgi import log

from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.core.exceptions import PermissionDenied
from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect

# Create your views here.
from django.urls import reverse

import todo
from user.models import TodoForm, Todo


def index(request):
    return render(request, "userTodoPage.html")


@login_required(login_url='/login')
def addTodo(request):
    if request.method == 'POST':
        form = TodoForm(request.POST, request.FILES)
        if form.is_valid():
            current_user = request.user
            data = Todo()
            data.user_id = current_user.id
            data.type = form.cleaned_data['type']
            data.note = form.cleaned_data['note']
            data.clicked = form.cleaned_data['clicked']
            data.status = 'False'
            data.save()
            messages.success(request,'Add Successfuly')
            return HttpResponseRedirect('/')
        else:
            messages.success(request,'Todo Form Error:' + str(form.errors))
            return HttpResponseRedirect('/')
    else:
        form = TodoForm()
        context = {
            'form':form
        }
    return render(request,'content.html',context)


def todoList(request):
    current_user = request.user
    todos = Todo.objects.filter(user_id = current_user.id)
    form = TodoForm()
    context = {
        'todos':todos,
    }
    return render(request, "userTodoPage.html",context)

@login_required(login_url='/login')
def todoEdit(request,id):
    todo = Todo.objects.get(id =id)
    if request.method == 'POST':
        form = TodoForm(request.POST, request.FILES, instance=todo)
        if form.is_valid():
            form.save()
            messages.success(request,'Your Todo Updated Successfuly')
            return HttpResponseRedirect('/')
        else:
            messages.success(request,'Todo Form Error:'+str(form.errors))
            return HttpResponseRedirect('/')
    else:
        form = TodoForm(instance=todo)
        context = {
            'form': form
        }
        return render(request,'editPage.html',context)

@login_required(login_url='/login')
def todoDelete(request,id):
    current_user = request.user
    Todo.objects.filter(id=id,user_id=current_user.id).delete()
    messages.success(request,'Todo Silindi')
    return HttpResponseRedirect('/user/todoList')


def todo_completed(request,id):
    todo = Todo.objects.get(id=id)
    todo.clicked = False
    todo.complated_time = todo.update_at
    todo.save()
    return redirect('/user/todoList')


def todo_no_completed(request,id):
    todo = Todo.objects.get(id=id)
    todo.clicked = True
    todo.complated_time = todo.update_at
    todo.save()
    return redirect('/user/todoList')

