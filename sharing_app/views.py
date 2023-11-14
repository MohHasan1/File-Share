from django.shortcuts import render
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .forms import UploadFileForm
from .models import File
from django.contrib.auth.models import User
from .encryption import encrypt_file, decrypt_file
from django.http import HttpResponse
import os
from .fileManagement import shareFile, share_file_path, user_directory_path

# Temporary Fernet key:
temp_fernet_key  = b'zdnoc4dAbhI4fZbcSdDMuBPvntPcY7DwHaSsVwAL5js='

@login_required
def home(request):
    #file = File.objects.filter(owner=request.user)
    file = request.user.ownedFiles.all()
    return render(request, 'share/home.html', {'user_files':file})

@login_required
def upload(request):
    if request.method == "POST":

        # User only inputs 2 data: file name and the file.
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

    # Check if the user has permission to download the file
    if request.user == file_inst.owner:

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


@login_required
def share(request, file_id):
    errorMessage = None

    if request.method == 'POST':
        try:

            # Get the user to share with.
            userName = request.POST.get('username')
            user = User.objects.get(username=userName)
            
            # Get the file we want to share:
            file_to_share = File.objects.get(id=file_id)

            # create a new instance in the File table for the reciever (file directory is yet to set)
            shared_File = file_to_share.make_share_file(user)

########################################## if shared file is None ###############################################################
# django buil in u dont have to pass in dict:
            if shared_File is None:
                messages.error(request, "PLease check the username. You are using your username!")
            else:

########################################## Dir for table ###############################################################
                # set the file dir in the File table :

                #original file dir from db:
                og_file_dir = file_to_share.fileDir.path
                og_file_name = os.path.basename(og_file_dir) # This is also the shared file name.
                shared_File.fileDir =  user_directory_path(shared_File, og_file_name)

########################################## Move File (different dir) #########################################################
                # Get the path for the shared file (to save in the table):
                shared_File_Dir = share_file_path(shared_File)

                # move the actual file: #shared_File_Dir
                shareFile(file_to_share.fileDir.path, shared_File_Dir)

########################################## Save ########################################################################
                shared_File.save()

        except User.DoesNotExist:
            errorMessage = "User does not exit, Please put in the correct user name."


    return render(request, 'share/share.html', {'errorMessage':errorMessage})


# @login_required
# def share_file(request):
#     return render(request, 'share/share.html', {})

