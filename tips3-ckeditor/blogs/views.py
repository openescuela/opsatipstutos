from django.shortcuts import render

# Create your views here.
from .models import Project
from .forms import ProjectForm

def index(request):
    projects = Project.objects.all()
    form = ProjectForm()
    return render(request, 'blogs/index.html',{'projects':projects, 'form':form})
