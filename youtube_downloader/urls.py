# urls.py
from django.contrib import admin
from django.urls import path
from downloader import views 
from django.contrib.auth.views import LogoutView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home_view,name="home"),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    # path('singup/', views.singup_view, name='singup'),

    path('progress/', views.download_progress_view, name='download_progress_view'),
]
