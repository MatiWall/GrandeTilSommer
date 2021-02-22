from django.urls import path
from . import views


app_name = 'jacked'

urlpatterns = [
    path('', views.Home.as_view(), name='home'),
    path('macros/<int:user_id>/', views.MacroCyclesView.as_view(), name='macros'),
    path('macro/<int:macro_id>/', views.MacroCycleView.as_view(), name='macro')

]