from django.urls import path
from . import views


app_name = 'jacked'

urlpatterns = [
    path('', views.Home.as_view(), name='home'),
    path('macros/<int:user_id>/', views.macro_cycle, name='macros'),

]