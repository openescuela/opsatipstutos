from django.db import models
from ckeditor.fields import RichTextField

class Project(models.Model):
    name = models.CharField(max_length=50)
    image = models.ImageField()
    content = RichTextField()

    def __str__(self):
        return self.name
