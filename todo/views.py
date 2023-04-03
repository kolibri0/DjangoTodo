from django.shortcuts import render
from django.views.decorators.http import require_http_methods
from django.http import HttpResponseRedirect
from .models import Todo
import random


# Create your views here.


def index(request):
    todos = {}
    if not request.user.is_authenticated:
        return HttpResponseRedirect("users/login")
    else:
        todos = Todo.objects.filter(user=request.user)
        return render(request, 'todo/todos.html', {"todos": todos})


def create(request):
    if request.method == 'POST':
        if request.user.is_authenticated:
            title = request.POST["title"]
            todo = Todo(title=title)
            todo.user = request.user
            # Todo.objects.create(title=title, user=request.user)
            todo.save()
        return HttpResponseRedirect("/")


def update(request, id):
    todo = Todo.objects.get(id=id)
    todo.is_complite = not (todo.is_complite)
    todo.save()
    return HttpResponseRedirect("/")


def delete(request, id):
    todo = Todo.objects.get(id=id)
    todo.delete()
    return HttpResponseRedirect("/")
