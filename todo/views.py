from django.shortcuts import render
from django.views.decorators.http import require_http_methods
from django.http import HttpResponseRedirect


# Create your views here.


def index(request):
    return render(request, 'todo/todos.html')


@require_http_methods(["POST"])
def update(request):
    print("1@@#@#$@#$@#$@#$@###############################################")
    return HttpResponseRedirect("/")


def delete(request):
    print("----------------------------------------------------------------------")
    return HttpResponseRedirect("/")
