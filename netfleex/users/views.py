from random import randint
from typing import Reversible
from django.db.models.expressions import Random
from django.shortcuts import render, redirect
from .models import Netfeelex
from django.http import HttpResponseRedirect, HttpResponse
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login, logout, authenticate
from django.contrib import messages
from .forms import newUser
from django.contrib.auth.forms import UserCreationForm



# Create your views here.
def register(request):
    """Register a new user."""
    if request.method != 'POST':
        # Display blank registration form.   
        form = UserCreationForm()
    else:
        # Process completed form.
        form = UserCreationForm(data=request.POST)
        
        if form.is_valid():
            new_user = form.save()
            # Log the user in, and then redirect to home page.
            authenticated_user = authenticate(username=new_user.username,
                password=request.POST['password1'])
            login(request, authenticated_user)
            
            return redirect('home')

    context = {'form': form}
    return render(request, 'register.html', context)

def logout_request(request):
    logout(request)
    messages.info(request, "Session est fermée")
    return redirect("home")

def user(request):
    profile = request.user.get_profile()
    i = randint(0,10)
    
    return redirect("/user.html")