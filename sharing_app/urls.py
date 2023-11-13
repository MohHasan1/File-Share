from django.contrib import admin
from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

# This app name is important as reverse function looks for this to create an url.
app_name = 'sharing_app'

urlpatterns = [
    path('',views.home, name="home"),
    path('upload/', views.upload, name="upload"),
    path('download/<int:file_id>/', views.download, name="download"), # <int:filename>/ gets the file primary id to download.
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
