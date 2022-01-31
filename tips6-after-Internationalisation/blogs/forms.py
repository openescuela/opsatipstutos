from django import forms
from .models import ContactMe

class ContactMe(forms.ModelForm):
    class Meta:
        model = ContactMe
        fields = ('name','email','message')
