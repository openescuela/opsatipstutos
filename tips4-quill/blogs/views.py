from django.shortcuts import render

# Create your views here.
from .models import Project
from .forms import ProjectForm, ProjectSecondForm
def index(request):
    projects = Project.objects.all()
    form = ProjectForm()
    secondform = ProjectSecondForm
    return render(request, 'blogs/index.html',{'projects':projects,
                                                'form':form,
                                                'secondform':secondform})
