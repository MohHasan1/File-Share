from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

# app name: (user for reverse and routing in html files)
app_name = 'user_app'

urlpatterns = [
   path('reg/', views.registration, name="registration"),
   path('login/', auth_views.LoginView.as_view(template_name='user/loginMub.html'), name="login"),
   #path('login/', auth_views.LogoutView.as_view(template_name='user/loginMub.html'), name="logout"),
   path('', auth_views.LogoutView.as_view(), name="logout"),
   path('profile/', views.profile, name="profile"),

]

