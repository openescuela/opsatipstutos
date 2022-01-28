from django.shortcuts import render

# Create your views here.
from .models import Project

def index(request):
    projects = Project.objects.all()
    return render(request, 'blogs/index.html',{'projects':projects})
