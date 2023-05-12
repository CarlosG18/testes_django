from django.urls import path
from django.views import View 
from . import views

app_name = "user"
urlpatterns = [
    path('', views.index, name="index"),
    path('create/', views.create, name="create"),
    path('home/', views.home, name="home"),
]