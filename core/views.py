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
from .forms import ProjectForm, TestimonyForm

def add_project(request):
    if request.method == 'POST':
        form = ProjectForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = ProjectForm()
    return render(request, 'core/add_project.html', {'form': form})

from .models import Project, Testimony, Inquiry, PersonalInformation 

def contact_view(request):
    if request.method == 'POST':
        Inquiry.objects.create(
            first_name=request.POST.get('first_name'),
            last_name=request.POST.get('last_name'),
            contact_number=request.POST.get('contact_number'),
            email=request.POST.get('email'),
            address=request.POST.get('address'),
            message=request.POST.get('message')
        )
        return redirect('contact')
    return render(request, 'core/contact.html')

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

from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import user_passes_test
from .forms import ProjectForm, TestimonyForm, TechStackForm
from .models import Project, TechStack, Testimony, Inquiry, PersonalInformation

def admin_login_view(request):
    error_message = None
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        
        if user is not None:
            if user.is_superuser:
                login(request, user)
                return redirect('dashboard')
            else:
                error_message = "Access denied. Admin/superuser credentials required."
        else:
            error_message = "Invalid username or password."
            
    return render(request, 'core/admin_login.html', {'error_message': error_message})


@user_passes_test(lambda u: u.is_superuser, login_url='admin_login')
def dashboard_view(request):
    projects = Project.objects.all()
    tech_stacks = TechStack.objects.all()
    return render(request, 'core/dashboard.html', {
        'projects': projects,
        'tech_stacks': tech_stacks,
    })


@user_passes_test(lambda u: u.is_superuser, login_url='admin_login')
def add_tech_stack(request):
    if request.method == 'POST':
        form = TechStackForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('dashboard')
    else:
        form = TechStackForm()
    return render(request, 'core/add_tech_stack.html', {'form': form})
from django.contrib.auth import logout
from django.shortcuts import redirect

def admin_logout_view(request):
    logout(request)
    return redirect('home')