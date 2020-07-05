from django.contrib import messages
from django.contrib.auth import authenticate, logout, login
from django.http import HttpResponseRedirect
from django.shortcuts import render

# Create your views here.
from todo.forms import SignUpForm


def index(request):
    return render(request, "index.html")


def logout_view(request):
    logout(request)
    return HttpResponseRedirect('/')

def login_view(request):
    if request.method == 'POST': #Check form post
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request,user)
            messages.warning(request, "Giriş Yapıldı")
            return HttpResponseRedirect('/')
        else:
            messages.warning(request, "Login Hatası!")
            return HttpResponseRedirect('/login')
    return render(request, 'login.html')

def register_view(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid(): #Formdaki kontrolleri yapar
            form.save()
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=password)
            login(request,user)
            return HttpResponseRedirect('/')

    form = SignUpForm()
    context = {
               'form': form,
               }
    return render(request, 'register.html', context)