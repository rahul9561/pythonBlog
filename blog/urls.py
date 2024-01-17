from django.urls import path
from . import views
from .views import delete_post

urlpatterns = [
    path('', views.index, name='index'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('signup/', views.signup, name='signup'),
     path('login/', views.user_login, name='login'),
     path('dashboard/delete/<int:post_id>/', delete_post, name='delete_post'),
    
]
