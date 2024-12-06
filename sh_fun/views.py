from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.db import transaction
from .models import Fun, UserProfile
from .forms import FunForm, UserProfileForm, CustomUserCreationForm
from .utils import send_verification_email
import os
from django.conf import settings
from django.contrib.auth.models import User

# Create your views here.
@login_required
def fun_list(request):
    """Home page view showing all fun posts"""
    funs = Fun.objects.all().order_by('-created_at')
    return render(request, 'fun_list.html', {
        'funs': funs,
        'show_create_button': True
    })

@login_required
def create_fun(request):
    if request.method == 'POST':
        form = FunForm(request.POST, request.FILES)
        if form.is_valid():
            fun = form.save(commit=False)
            fun.user = request.user
            fun.save()
            messages.success(request, 'Your fun moment has been shared!')
            return redirect('fun_list')  # Redirect to home page instead of profile
        else:
            messages.error(request, 'Please correct the errors below.')
    else:
        form = FunForm()
    
    return render(request, 'create_fun.html', {'form': form})

@login_required
def fun_detail(request, fun_id):
    fun = get_object_or_404(Fun, id=fun_id)
    return render(request, 'fun_detail.html', {'fun': fun})

@login_required
def fun_edit(request, fun_id):
    fun = get_object_or_404(Fun, id=fun_id, user=request.user)
    if request.method == 'POST':
        form = FunForm(request.POST, request.FILES, instance=fun)
        if form.is_valid():
            form.save()
            messages.success(request, 'Your fun moment has been updated!')
            return redirect('fun_detail', fun_id=fun.id)
    else:
        form = FunForm(instance=fun)
    return render(request, 'fun_edit.html', {'form': form, 'fun': fun})

@login_required
def fun_delete(request, fun_id):
    fun = get_object_or_404(Fun, id=fun_id, user=request.user)
    if request.method == 'POST':
        fun.delete()
        messages.success(request, 'Your fun moment has been deleted.')
        return redirect('fun_list')
    return render(request, 'fun_delete.html', {'fun': fun})

@login_required
def profile_view(request):
    user_funs = Fun.objects.filter(user=request.user).order_by('-created_at')
    if request.method == 'POST':
        form = UserProfileForm(request.POST, request.FILES, instance=request.user.userprofile)
        if form.is_valid():
            form.save()
            messages.success(request, 'Your profile has been updated!')
            return redirect('profile')
    else:
        form = UserProfileForm(instance=request.user.userprofile)
    
    return render(request, 'profile.html', {
        'form': form,
        'user_funs': user_funs
    })

def profile_detail(request, username):
    user = get_object_or_404(User, username=username)
    user_profile = get_object_or_404(UserProfile, user=user)
    user_funs = Fun.objects.filter(user=user).order_by('-created_at')
    return render(request, 'profile_detail.html', {
        'profile_user': user,
        'user_profile': user_profile,
        'user_funs': user_funs
    })

def verify_email(request, token):
    try:
        profile = UserProfile.objects.get(email_verification_token=token)
        if not profile.email_verified:
            profile.email_verified = True
            profile.email_verification_token = None
            profile.save()
            messages.success(request, 'Your email has been verified successfully! You can now log in.')
        else:
            messages.info(request, 'Your email was already verified.')
    except UserProfile.DoesNotExist:
        messages.error(request, 'Invalid verification link.')
    return redirect('login')

def login_view(request):
    if request.user.is_authenticated:
        return redirect('fun_list')
        
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        
        if user is not None:
            # Check if email is verified
            if user.userprofile.email_verified:
                login(request, user)
                messages.success(request, f'Welcome back, {user.first_name}!')
                return redirect('fun_list')
            else:
                messages.warning(request, 'Please verify your email address before logging in.')
        else:
            messages.error(request, 'Invalid username or password.')
    
    return render(request, 'login.html')

@transaction.atomic
def register_view(request):
    if request.user.is_authenticated:
        return redirect('fun_list')
        
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            # Send verification email
            send_verification_email(user, request)
            messages.success(request, 'Registration successful! Please check your email to verify your account.')
            return redirect('login')
        else:
            for field, errors in form.errors.items():
                for error in errors:
                    messages.error(request, f'{error}')
    else:
        form = CustomUserCreationForm()
    return render(request, 'register.html', {'form': form})

def logout_view(request):
    logout(request)
    messages.info(request, 'You have been logged out.')
    return redirect('login')