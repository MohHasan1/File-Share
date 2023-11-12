from django.contrib import admin
from django.urls import path
from . import views

# This app name is important as reverse function looks for this to create an url.
app_name = 'sharing_app'

urlpatterns = [
    path('',views.home, name="home"),
]
