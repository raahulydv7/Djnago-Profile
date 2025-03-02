from django.shortcuts import render,redirect
from .models import UserProfile
from .forms import UserRegisterForm,UserLoginForm,UserProfileForm
from django.contrib import messages
from django.contrib.auth import authenticate,login,logout,update_session_auth_hash
from django.contrib.auth.forms import PasswordChangeForm
from django.contrib.auth.decorators import login_required
from django.conf import settings

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

@login_required
def profile_view(request):
    user_profile, created = UserProfile.objects.get_or_create(user=request.user)
    active_tab = request.GET.get('tab', 'profile')
    
    # Initialize forms
    profile_form = UserProfileForm(instance=request.user)
    password_form = PasswordChangeForm(user=request.user)
    
    if request.method == 'POST':
        if active_tab == 'profile':
            profile_form = UserProfileForm(request.POST, request.FILES, instance=request.user, user=request.user)
            if profile_form.is_valid():
                profile_form.save()
                
                # Handle profile image separately
                if 'profile_image' in request.FILES:
                    user_profile.profile_image = request.FILES['profile_image']
                    user_profile.save()
                
                messages.success(request, 'Profile updated successfully')
                return redirect('profile')
        else:  # password tab
            password_form = PasswordChangeForm(user=request.user, data=request.POST)
            if password_form.is_valid():
                password_form.save()
                # Important: This keeps the user logged in after password change
                update_session_auth_hash(request, request.user)
                messages.success(request, 'Password updated successfully')
                return redirect('profile')
            else:
                messages.error(request, 'Please correct the errors below')
    
    # Prepare the context
    context = {
        'form': profile_form,
        'password_form': password_form,
        'user_profile': user_profile,
        'active_tab': active_tab,
        'MEDIA_URL_setting':settings.MEDIA_URL
    }
    
    return render(request, 'profile.html', context)