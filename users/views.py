from django.http import HttpResponseRedirect
from django.shortcuts import render
from users.forms import UserForm, UserRegistrationForm
from django.contrib import auth


# Create your views here.


def MyLogin(request):
    if request.method == 'POST':
        form = UserForm(data=request.POST)
        if form.is_valid():
            username = request.POST["username"]
            password = request.POST["password"]
            user = auth.authenticate(username=username, password=password)
            if user:
                auth.login(request, user)
                return HttpResponseRedirect('/')
    else:
        form = UserForm()
    context = {
        'form': form,
        'title': 'login'
    }
    return render(request, 'auth/login.html', context)


def MyRegister(request):
    if request.method == 'POST':
        form = UserRegistrationForm(data=request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/users/login')
    else:
        form = UserRegistrationForm()
    context = {
        'form': form,
        'title': 'register'
    }
    return render(request, 'auth/register.html', context)
