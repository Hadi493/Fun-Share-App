from django.urls import path
from django.contrib.auth import views as auth_views
from . import views
from django.contrib.auth.views import LogoutView

urlpatterns = [
    path('', views.index, name='index'),
    path('funs/', views.fun_list, name='fun_list'),
    path('fun/create/', views.create_fun, name='create_fun'),
    path('fun/<int:fun_id>/', views.fun_detail, name='fun_detail'),
    path('fun/<int:fun_id>/edit/', views.fun_edit, name='fun_edit'),
    path('fun/<int:fun_id>/delete/', views.fun_delete, name='delete_fun'),
    
    # Authentication URLs
    path('login/', auth_views.LoginView.as_view(template_name='login.html'), name='login'),
    path('logout/', LogoutView.as_view(next_page='login'), name='logout'),  
    path('signup/', views.register_view, name='signup'),  
    path('profile/', views.profile_view, name='profile'),  
]