from django.urls import path
from . import views


app_name = 'jacked'

urlpatterns = [
    path('', views.Home.as_view(), name='home'),
    path('user/<int:user_id>/macros/', views.MacroCyclesView.as_view(), name='macros'),
    path('user/<int:user_id>/macro/<int:macro_id>/', views.MacroCycleView.as_view(), name='macro'),
    path('macro/delete/<int:user_id>/<int:macro_id>/', views.delete_macro, name='macro_delete')

]