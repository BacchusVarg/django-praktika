from django.urls import path
from django.contrib.auth import views as auth_views
from authent import views

urlpatterns = [
    path('login/', auth_views.LoginView.as_view(template_name='authent/login.html'), name='login'),
    path('register/', views.register_view, name='register'),
    path('logout/', auth_views.LogoutView.as_view(next_page='login'), name='logout'),
]