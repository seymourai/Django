from django.shortcuts import render, redirect
from .models import Project
from django.contrib.auth.decorators import login_required
from . import forms 
# Create your views here.


def projects_list(request):
    projects = Project.objects.all().order_by('-date')
    return render(request, 'projects/projects_list.html', {'projects': projects})


def project_page(request, slug):
    project = Project.objects.get(slug=slug)
    return render(request, 'projects/project_page.html', {'project': project})

@login_required(login_url="/users/login/")
def project_new(request):
    if request.method == 'POST': 
        form = forms.CreateProject(request.POST, request.FILES) 
        if form.is_valid():
            newproject = form.save(commit=False) 
            newproject.author = request.user 
            newproject.save()
            return redirect('projects:list')
    else:
        form = forms.CreateProject()
    return render(request, 'projects/project_new.html', { 'form': form })

