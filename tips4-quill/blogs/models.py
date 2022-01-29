from django.db import models
from django_quill.fields import QuillField

# Create your models here.

class Project(models.Model):
    name = models.CharField(max_length=50)
    content = QuillField(default='ici')
    def __str__(self):
        return self.name
