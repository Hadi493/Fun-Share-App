from django.urls import path
from . import views

urlpatterns = [
    path('', views.all_fun, name='all_fun'),
]