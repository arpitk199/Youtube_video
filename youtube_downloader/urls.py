# urls.py
from django.urls import path
from downloader import views 
from django.contrib.auth.views import LogoutView

urlpatterns = [
    path('', views.download_video, name='home'),  # Assuming download_video is your home view
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('progress/', views.download_progress_view, name='download_progress_view'),
]
