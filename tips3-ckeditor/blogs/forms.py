from ckeditor.widgets import CKEditorWidget
from .models import Project
from django import forms

class ProjectForm(forms.ModelForm):
    content = forms.CharField(widget=CKEditorWidget())
    class Meta:
        model = Project
        fields = ('name',)
