from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    path('funs/', views.fun_list, name='fun_list'),
    path('funs/create/', views.create_fun, name='create_fun'),
    path('funs/<int:fun_id>/', views.fun_detail, name='fun_detail'),
    path('funs/<int:fun_id>/edit/', views.fun_edit, name='fun_edit'),
    path('funs/<int:fun_id>/delete/', views.fun_delete, name='fun_delete'),
    
    # Authentication URLs
    path('login/', auth_views.LoginView.as_view(template_name='login.html'), name='login'),
    path('logout/', views.logout_view, name='logout'),  # Using our custom logout view
    path('signup/', views.register_view, name='signup'),  # Changed from register to signup
    path('profile/', views.profile_view, name='profile'),  # New profile URL
]