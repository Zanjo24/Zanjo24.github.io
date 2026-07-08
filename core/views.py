from django.shortcuts import render, get_object_or_404
from .models import PersonalInformation, Project

# 1. View that returns all personal information
def personal_info_view(request):
    personal_info = PersonalInformation.objects.first()
    return render(request, 'personal_info.html', {'personal_info': personal_info})

# 2. List view for all projects (titles only rendered in HTML)
def project_list(request):
    projects = Project.objects.all()
    return render(request, 'index.html', {'projects': projects})

# 3. Detail view for a single project
def project_detail(request, project_id):
    project = get_object_or_404(Project, id=project_id)
    return render(project_detail.html', {'project': project})