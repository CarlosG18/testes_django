from django.shortcuts import render
from .models import User
from django.http import HttpResponseRedirect, HttpResponse
from django.urls import reverse
from . import forms

def index(request):
    return render(request, "user/index.html")

def create(request):
    form = forms.MyForms(request.POST, request.FILES)
    user = User(nome=request.POST["nome"], foto=request.FILES['foto'])
    user.save()
    return HttpResponseRedirect(reverse('user:home'))

def home(request):
    users = User.objects.all()
    return render(request, 'user/home.html', {
        'users': users,
    })