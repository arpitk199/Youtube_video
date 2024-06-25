# views.py
from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from pytube import YouTube
import os

progress = 0  # Global variable to store progress

def download_progress(stream, chunk, file_handle, bytes_remaining):
    global progress
    total_size = stream.filesize
    bytes_downloaded = total_size - bytes_remaining
    progress = (bytes_downloaded / total_size) * 100

def download_video(request):
    global progress
    if request.method == 'POST':
        url = request.POST.get('url')
        folder_path = request.POST.get('folder_path')
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
    return render(request, 'downloader/download.html')

def download_progress_view(request):
    global progress
    return JsonResponse({'progress': progress})
