from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .forms import UploadFileForm
from .models import File
from .encryption import encrypt_file, decrypt_file
from django.http import HttpResponse
import os

# Temporary Fernet key:
temp_fernet_key  = b'zdnoc4dAbhI4fZbcSdDMuBPvntPcY7DwHaSsVwAL5js='

@login_required
def home(request):
    file = File.objects.filter(owner=request.user)
    return render(request, 'share/home.html', {'user_files':file})

@login_required
def upload(request):
    if request.method == "POST":

        # User onlu inputs 2 data: file name and the file.
        form = UploadFileForm(request.POST, request.FILES)
        
        # Remaining columns will be filled here.
        if form.is_valid():
            #file_name = form.cleaned_data['fileName']

            # Save the form data without committing to the database.(similar to add in git!)
            File = form.save(commit=False)

            File.fileSize = round(request.FILES['fileDir'].size / (1024 ** 2), 2)
            File.owner = request.user
            File.shared = False  
            File.sender = None  

            File.save()

            # Encryption (we first save the file and then encrypt)
            key = temp_fernet_key
            encrypt_file(File.fileDir.path, key) # .path gives the actual route of the file

    else:
        form = UploadFileForm()

    form = UploadFileForm()
    return render(request, 'share/upload.html', {'form':form})

@login_required
# Instead of using the build in download funtion we will make a custom one.
def download(request, file_id):

    #find the file:(one file so no need to use filter)
    file_inst = File.objects.get(id=file_id)

    # File path:(fileDir.path)
    file_path = file_inst.fileDir.path

    #decrypt:
    decrypt_file(file_path, temp_fernet_key)

    # Extract the file extension using os.path.splitext() on the full path
    _, file_extension = os.path.splitext(file_path)

    #download:
    #if os.path.exists(file_path):
    with open(file_path, 'rb') as file:
        response = HttpResponse(file.read(), content_type='application/octet-stream')
        response['Content-Disposition'] = f'attachment; filename="{file_inst.fileName}.{file_extension}"'

    #encrypt file again:
    encrypt_file(file_path, temp_fernet_key)

    # return the response
    return response


