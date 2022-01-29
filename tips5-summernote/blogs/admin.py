from django.contrib import admin
from django_summernote.admin import SummernoteModelAdmin

# Register your models here.
from .models import Project

class ProjectAdmin(SummernoteModelAdmin):
    summernote_fields = ('content',)

admin.site.register(Project, ProjectAdmin)
