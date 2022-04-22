from django.shortcuts import render, redirect
from .forms import ProjectForm
from .models import Project
from django.contrib import messages


def create_project(request):
    form = ProjectForm()
    data = request.POST
    if request.method == 'POST':
        form = ProjectForm(data=data)
        title = data.get('title')
        if form.is_valid() and data.get('technology') != "person":
            form.save()
            form = ProjectForm
            messages.success(request, f"{title} just got created")
            return redirect("view_all_projects")
        else:
            messages.error(request, "person as a technology is not valid")
    return render(request, "projects/create_project.html", {"form": form})


def get_projects(request):
    data = request.POST
    if data:
        key = data.get('filter')
        projects = {} if key is None else Project.objects.filter(title__contains=key)
    else:
        projects = Project.objects.all()
        # .order_by("-date_created")
    return render(request, "projects/project_list.html", {"projects": projects})


def filter_projects(request):
    data = request.POST
    key = data.get('filter')
    projects = {} if key is None else Project.objects.filter(title__contains=key)
    return render(request, "projects/filtered_projects.html", {'projects': projects})


def retrieve_project(request, id):
    if Project.objects.filter(id=id).exists():
        project = Project.objects.get(id=id)
    else:
        project = {}
    return render(request, "projects/project_detail.html", {'project': project})


def update_project(request, id):
    project = Project.objects.get(id=id)
    form = ProjectForm(instance=project)
    data = request.POST
    print(data)
    if request.method == 'POST':
        form = ProjectForm(instance=project, data=data)
        if form.is_valid() and data.get('technology') != "person":
            form.save()
            return redirect('project_detail', id)
        else:
            print('This object will not save')
            print('The technology should not be person')
            print(form.errors)
    return render(request, "projects/update_profile.html", {'project': project, 'form': form})


def delete_project(request, id):
    if Project.objects.filter(id=id).exists():
        Project.objects.get(id=id).delete()
        return redirect('view_all_projects')
