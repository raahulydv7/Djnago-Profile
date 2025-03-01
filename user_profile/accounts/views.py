from django.shortcuts import render,redirect
from .forms import UserRegisterForm,UserLoginForm
from django.contrib import messages
from django.contrib.auth import authenticate,login,logout

# Create your views here.
def homepage_view(request):
    return render(request, 'home.html')

def register_view(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request, 'Account created successfully')
            return redirect('home')
        else:
            messages.error(request, 'Invalid form')
    else:
        form = UserRegisterForm()
    return render(request, 'register.html',{'form':form})

def login_view(request):
    if request.user.is_authenticated:
        messages.info(request, "You are already logged in.")
        return redirect('home')
    
    if request.method == 'POST':
        form = UserLoginForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            messages.success(request, 'LogedIn successfully')
            return redirect('home')
        else:
            messages.error(request, 'Invalid Credentials')
    
    else:
        form = UserLoginForm()
    return render(request, 'login.html',{'form':form})

def logout_view(request):
    logout(request)
    return redirect('home')