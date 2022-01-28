from django.db import models
from tinymce import models as tinymce_models

class Project(models.Model):
    name = models.CharField(max_length=50)
    content = tinymce_models.HTMLField()
