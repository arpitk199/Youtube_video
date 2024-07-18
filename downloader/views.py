# views.py
from django.shortcuts import render, redirect
from django.http import HttpResponse, JsonResponse
from django.http import HttpResponseRedirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.decorators import login_required
from django.contrib.messages import success,error
from django.contrib.auth.models import User
from pytube import YouTube
import os

from .forms import DownloadForm

progress = 0  # Global variable to store progress

def home_view(Request):
    return render(Request,"downloader/home.html")

def download_progress(stream, chunk, file_handle, bytes_remaining):
    global progress
    total_size = stream.filesize
    bytes_downloaded = total_size - bytes_remaining
    progress = (bytes_downloaded / total_size) * 100

# @login_required
def download_video(request):
    global progress
    if request.method == 'POST':
        form = DownloadForm(request.POST)
        if form.is_valid():
            url = form.cleaned_data['url']
            folder_path = form.cleaned_data['folder_path']
            if not folder_path:
                folder_path = os.getcwd()
                
            try:
                yt = YouTube(url, on_progress_callback=download_progress)
                video = yt.streams.filter(progressive=True, file_extension='mp4').first()
                video.download(folder_path)
                progress = 100  # Ensure progress is set to 100% when done
                return HttpResponse(f"Downloaded: {yt.title}")
            except Exception as e:
                return HttpResponse(f"Error downloading video: {e}")
    else:
        form = DownloadForm()
    return render(request, 'downloader/download.html', {'form': form})

def download_progress_view(request):
    global progress
    return JsonResponse({'progress': progress})

def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('downloader/download.html')  # Redirect to home page
    else:
        form = AuthenticationForm()
    return render(request, 'downloader/login.html', {'form': form})

def logout_view(request):
    logout(request)
    return redirect('downloader/home.html')  # Redirect to home page

def singup_view(request):
    return render(request,'downloader/singup.html') 


def forgot_password_view(request):
    return render(request,'downloader/forgot_password.html') 