from django.shortcuts import render, get_object_or_404
from .models import PersonalInformation, Project

def personal_info_view(request):
    personal_info = PersonalInformation.objects.first()
    return render(request, 'personal_info.html', {'personal_info': personal_info})

def project_list(request):
    projects = Project.objects.all()
    return render(request, 'index.html', {'projects': projects})

def project_detail(request, project_id):
    project = get_object_or_404(Project, id=project_id)
    return render(request, 'project_detail.html', {'project': project})

from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import ListView
from .models import Project, Testimony, Inquiry
from .forms import ProjectForm, InquiryForm, TestimonyForm

def add_project(request):
    if request.method == 'POST':
        form = ProjectForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')
    else:
        form = ProjectForm()
    return render(request, 'core/add_project.html', {'form': form})

def contact_view(request):
    if request.method == 'POST':
        form = InquiryForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('contact')
    else:
        form = InquiryForm()
    return render(request, 'core/contact.html', {'form': form})

def add_testimony(request):
    if request.method == 'POST':
        form = TestimonyForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('testimony_list')
    else:
        form = TestimonyForm()
    return render(request, 'core/add_testimony.html', {'form': form})

class TestimonyListView(ListView):
    model = Testimony
    template_name = 'core/testimony_list.html'
    context_object_name = 'testimonies'

def testimony_detail(request, pk):
    testimony = get_object_or_404(Testimony, pk=pk)
    return render(request, 'core/testimony_detail.html', {'testimony': testimony})