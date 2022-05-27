from django.shortcuts import render
from django.http import Http404
from .models import Editor, Project

# Create your views here.
def index(request):
    return render(request,'pages/index.html')

def add_project(request):
    try:
        project = Project.objects.all()
    except Project.DoesNotExist:
        raise Http404()
    return render(request,"pages/project.html", {"projects":project})

def add_editor(request):
    try:
        editor = Editor.objects.all()
    except Editor.DoesNotExist:
        raise Http404()
    project = Project.objects.all()
    return render(request,"pages/index.html", {"editors":editor,"projects":project})
    