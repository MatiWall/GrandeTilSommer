from django.urls import path
from . import views


app_name = 'user'

urlpatterns = [
    path('register/', views.Register.as_view(), name='register'),
]