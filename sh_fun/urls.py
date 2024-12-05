from django.urls import path
from django.contrib.auth import views as auth_views
from . import views
from django.contrib.auth.views import LogoutView

urlpatterns = [
    # Main pages
    path('', views.fun_list, name='fun_list'),  # Make fun_list the home page
    path('fun/create/', views.create_fun, name='create_fun'),
    path('fun/<int:fun_id>/', views.fun_detail, name='fun_detail'),
    path('fun/<int:fun_id>/edit/', views.fun_edit, name='fun_edit'),
    path('fun/<int:fun_id>/delete/', views.fun_delete, name='fun_delete'),
    
    # Authentication URLs
    path('login/', views.login_view, name='login'),  # Use custom login view
    path('logout/', views.logout_view, name='logout'),  # Use custom logout view
    path('register/', views.register_view, name='register'),  # Rename signup to register for consistency
    path('profile/', views.profile_view, name='profile'),
]