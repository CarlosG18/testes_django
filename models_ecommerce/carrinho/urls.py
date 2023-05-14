from django.urls import path
from . import views

app_name = "carrinho"
urlpatterns = [
    path('create/<int:pk>/', views.create, name="create"),
]