from django.db import models

# Create your models here.

class Project(models.Model):
    name = models.CharField(max_length=50)
    content = models.TextField(default='ici')
