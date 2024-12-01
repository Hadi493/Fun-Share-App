from django.urls import path
from . import views

urlpatterns = [
    path('', views.fun_list, name='all_fun'),
    path('create/', views.create_fun, name='create_fun'),
    path('<int:fun_id>/', views.fun_detail, name='fun_detail'),
    path('<int:fun_id>/edit/', views.fun_edit, name='fun_edit'),
    path('<int:fun_id>/delete/', views.fun_delete, name='fun_delete'),
]