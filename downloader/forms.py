# forms.py
from django import forms

class DownloadForm(forms.Form):
    url = forms.URLField(label='Video URL', required=True)
    folder_path = forms.CharField(label='Download Folder Path', required=False)
