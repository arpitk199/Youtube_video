# urls.py
from django.urls import path
from downloader import views

urlpatterns = [
    path('', views.download_video, name='download_video'),
    path('progress/', views.download_progress_view, name='download_progress_view'),
]
