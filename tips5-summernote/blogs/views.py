from django.shortcuts import render

# Create your views here.
from .models import Project
from .forms import ProjectForm, SecondForm

def index(request):
    projects = Project.objects.all()
    firstform = ProjectForm()
    secondform = SecondForm()
    return render(request, 'blogs/index.html',{'projects':projects,
                                                'firstform':firstform,
                                                'secondform':secondform})
