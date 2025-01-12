from django.shortcuts import render, redirect
from .forms import UserForm, LoginForm
from django.contrib.auth import login, logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required

@login_required
def add_product(request, id):    
    return render(request, 'main.html')



