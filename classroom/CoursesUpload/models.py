from django.db import models
from django.core.files.storage import FileSystemStorage


# Créez une instance de FileSystemStorage
fs = FileSystemStorage(location='CoursesUpload/pdfs/')

#infos sur le cours
class SupportCours(models.Model):
    TYPES_CHOICES = [
        ('leçon', 'Leçon'),
        ('devoir', 'Devoir'),
    ]
    title = models.CharField(max_length=100)
    teacher_name = models.CharField(max_length=100)
    module_du_cours = models.CharField(max_length=50)
    document_type = models.CharField(
        max_length=100,
        choices=TYPES_CHOICES,
        default='leçon',
    )
    #pdf_file = models.FileField(path='CoursesUpload/pdfs/', blank=True, null=True)

#uploader les fichiers
class UploadPDF(models.Model):
    titre = models.CharField(max_length=255)
    document = models.FileField(upload_to='pdfs/', storage=fs)

# Create your models here.
