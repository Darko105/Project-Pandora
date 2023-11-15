from django.shortcuts import render,redirect
from django.http import HttpResponseRedirect
from django.contrib.auth import login,authenticate
from django.contrib import messages
from .forms import SignUpForm,LoginForm
import requests

siteName = 'Pandora'

def signup(request):
    
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            messages.success(request,f'Welcome to {siteName}! your Account created successfully ')
           # login(request, user)  # Automatically log in the user after registration
            #return redirect('login')  # Redirect to the home page or any other desired page
    else:
        form = SignUpForm()

    return render(request, 'users/signup.html', {'form': form})

"""" 
def getSteamProfile(id):
    rep = requests.get(f'https://steamcommunity.com/profiles/{id}/')
    content = rep.text[280:350]
    char = temp = ''
    i = 0
    while char != '<':
        char = content[i]
        temp += char
        i +=1
    return str(temp[:-1])
    """





def login_view(request):
    if request.method == 'POST':
        form = LoginForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            print(password)
            user = authenticate(request, username=username, password=password)
            if user is not None:
                if user.check_password(password): #check if the password match
                    login(request, user)
                    # Redirect to a success page.
                    return redirect('pandora:index')
    else:
        form = LoginForm()

    return render(request, 'users/login.html', {'form': form})



