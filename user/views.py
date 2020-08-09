from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
# Create your views here.

from .forms import LoginForm, RegisterForm



def register_view(request):
    
    if request.method == 'POST':
        form = RegisterForm(request.POST,request.FILES)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            return redirect('login')
    else:
        form = RegisterForm()
    
    data = {
        'form': form
    }
    
    return render(request, 'pages/login/register.html', data)

def login_view(request):
    
    form = LoginForm(request.POST or None)
    if request.method == 'POST':
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user:
                login(request, user)
                return redirect('index')

            #else:
            #    return    

    data = {
        'form': form,
    }
    
    return render(request, 'pages/login/login.html', data)



def logout_view(request):
    logout(request)
    return redirect('login')