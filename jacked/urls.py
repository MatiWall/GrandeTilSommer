from django.urls import path
from . import views


app_name = 'jacked'

urlpatterns = [
    path('home/', views.Home.as_view(), name='home'),
]