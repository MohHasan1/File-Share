from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

# app name:
app_name = 'user_app'

urlpatterns = [
   path('reg/', views.registration, name="registration"),
   path('login/', auth_views.LoginView.as_view(template_name='user/login.html'), name="login"),
   path('logout/', auth_views.LogoutView.as_view(template_name='user/logout.html'), name="logout"),
   path('profile/', views.profile, name="profile"),

]

