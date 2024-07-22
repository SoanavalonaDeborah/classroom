# myapp/forms.py

from django import forms
from . import models

class SupportCoursForm(forms.ModelForm):
    class Meta:
        model = models.SupportCours
        fields = ['title', 'teacher_name', 'module_du_cours', 'document_type']