from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

# When user upload a file a unique directory is created. (this fun is not used when sharing is done)
def user_directory_path(File, filename):
    return f'user_{File.owner.id}/file/{filename}'

class File(models.Model):
    fileName = models.CharField(max_length=255)
    fileSize = models.FloatField()
    fileDir = models.FileField(null=True, upload_to=user_directory_path)
    owner = models.ForeignKey(User, null=False, on_delete=models.CASCADE, related_name='ownedFiles')
    shared = models.BooleanField()
    sender = models.ForeignKey(User, null=True, on_delete=models.SET_NULL, related_name='sharedFiles')
    created_shared_at = models.DateTimeField(default=timezone.now)

    def share_file(self, sender):
        if  not self.shared:
            self.shared = True
            self.sender = sender
            #might need to a filedir
            self.save()
    
    def __str__(self):
        return self.fileName
    
    class Meta:
        constraints = [
            models.CheckConstraint(check=models.Q(fileSize__gte=0.0), name='file_size_non_negative_check'),
        ]

        

