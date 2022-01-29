from django_summernote.widgets import SummernoteWidget
from django import forms
from .models import Project

# Form as Form
class ProjectForm(forms.Form):
    content = forms.CharField(widget=SummernoteWidget())

# Form as ModelForm
class SecondForm(forms.ModelForm):
    content = forms.CharField(widget=SummernoteWidget())
    class Meta :
        model = Project
        fields = ('name', 'content',)
