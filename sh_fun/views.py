from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.db import transaction
from .models import Fun, UserProfile
from .forms import FunForm, UserProfileForm
import os
from django.conf import settings

# Create your views here.
def index(request):
    # Get all fun posts ordered by creation date
    funs = Fun.objects.all().order_by('-created_at')
    return render(request, 'index.html', {
        'funs': funs,
        'show_create_button': request.user.is_authenticated
    })

def all_fun(request):
    return render(request, 'all_fun.html')

@login_required
def fun_list(request):
    funs = Fun.objects.all().order_by('-created_at')
    return render(request, 'fun_list.html', {'funs': funs})

@login_required
def create_fun(request):
    if request.method == 'POST':
        form = FunForm(request.POST, request.FILES)
        if form.is_valid():
            fun = form.save(commit=False)
            fun.user = request.user
            fun.save()
            messages.success(request, 'Your fun moment has been shared!')
            return redirect('profile')
        else:
            messages.error(request, 'Please correct the errors below.')
            print("Fun form errors:", form.errors)  # Debug print
    else:
        form = FunForm()
    
    return render(request, 'create_fun.html', {'form': form})

@login_required
def delete_fun(request, fun_id):
    fun = get_object_or_404(Fun, id=fun_id, user=request.user)
    fun.delete()
    messages.success(request, 'Your fun moment has been deleted.')
    return redirect('profile')

@login_required
def fun_edit(request, fun_id):
    fun = get_object_or_404(Fun, pk=fun_id, user = request.user)
    if request.method == 'POST':
        form = FunForm(request.POST, request.FILES, instance=fun)
        if form.is_valid():
            fun = form.save(commit=False)
            fun.user = request.user
            fun.save()
            return redirect('fun_list')
    else:
        form = FunForm(instance=fun)
    return render(request, 'create_fun.html', {'form': form})

@login_required
def fun_detail(request, fun_id):
    fun = get_object_or_404(Fun, id=fun_id)
    return render(request, 'fun_detail.html', {
        'fun': fun,
        'is_owner': fun.user == request.user
    })

@login_required
def fun_delete(request, fun_id):
    fun = get_object_or_404(Fun, pk=fun_id, user = request.user)
    if request.method == 'POST':
        fun.delete()
        return redirect('fun_list')
    return render(request, 'fun_delete.html', {'fun': fun})

@login_required
def profile_view(request):
    # Create UserProfile if it doesn't exist
    profile, created = UserProfile.objects.get_or_create(
        user=request.user,
        defaults={
            'bio': '',
            'location': '',
            'website': ''
        }
    )
    
    if request.method == 'POST':
        user_form = UserProfileForm(request.POST, request.FILES, instance=profile)
        if user_form.is_valid():
            try:
                with transaction.atomic():
                    # Handle profile picture
                    if 'profile_picture' in request.FILES:
                        # Delete old profile picture if it exists and is not the default
                        if profile.profile_picture and profile.profile_picture.name != 'profile_pics/default.png':
                            if os.path.isfile(profile.profile_picture.path):
                                os.remove(profile.profile_picture.path)
                    
                    # Update User model fields
                    request.user.first_name = user_form.cleaned_data['first_name']
                    request.user.last_name = user_form.cleaned_data['last_name']
                    request.user.email = user_form.cleaned_data['email']
                    request.user.save()
                    
                    # Update UserProfile model fields
                    profile = user_form.save(commit=False)
                    profile.user = request.user
                    
                    # Ensure bio is not None
                    if profile.bio is None:
                        profile.bio = ""
                    
                    profile.save()
                    
                messages.success(request, 'Your profile was successfully updated!')
                return redirect('profile')
            except Exception as e:
                messages.error(request, f'Error updating profile: {str(e)}')
                print(f"Error updating profile: {str(e)}")  # Debug print
        else:
            messages.error(request, 'Please correct the errors below.')
            print("Form errors:", user_form.errors)  # Debug print
    else:
        initial_data = {
            'first_name': request.user.first_name,
            'last_name': request.user.last_name,
            'email': request.user.email,
        }
        user_form = UserProfileForm(instance=profile, initial=initial_data)

    # Get user's funs
    user_funs = Fun.objects.filter(user=request.user).order_by('-created_at')
    
    # Debug prints
    if settings.DEBUG:
        print("Profile picture:", profile.profile_picture if profile else "No profile")
        print("Profile picture URL:", profile.profile_picture.url if profile and profile.profile_picture else "No URL")
        print("Bio:", profile.bio if profile else "No bio")
        print("Media Root:", settings.MEDIA_ROOT)
        print("Media URL:", settings.MEDIA_URL)
        print("Profile instance:", profile.__dict__)  # Print all profile attributes
    
    # Add debug context
    context = {
        'user': request.user,
        'user_form': user_form,
        'funs': user_funs,
        'debug': settings.DEBUG,
        'profile': profile,
        'media_root': settings.MEDIA_ROOT,
        'media_url': settings.MEDIA_URL,
    }
    
    return render(request, 'profile.html', context)

def register_view(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request, 'Registration successful!')
            return redirect('fun_list')
    else:
        form = UserCreationForm()
    return render(request, 'register.html', {'form': form})

def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                messages.success(request, f'Welcome back, {username}!')
                return redirect('fun_list')
    else:
        form = AuthenticationForm()
    return render(request, 'login.html', {'form': form})

def logout_view(request):
    logout(request)
    messages.success(request, 'You have been successfully logged out.')
    return redirect('login')