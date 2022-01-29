from django_quill.forms import QuillFormField
from django import forms
from .models import Project

class ProjectForm(forms.Form):
    body = QuillFormField()

class ProjectSecondForm(forms.ModelForm):
    class Meta:
        model = Project
        fields = ('name', 'content',)
