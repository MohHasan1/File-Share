from django import forms
from .models import File

class UploadFileForm(forms.ModelForm):
    fileName = forms.CharField(required=True, label="File Name")
    fileDir = forms.FileField(required=True, label="File")

    class Meta:
        model = File
        fields = ['fileName', 'fileDir']
