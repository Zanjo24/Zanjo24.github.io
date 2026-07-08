from django.shortcuts import render
from .models import PersonalInformation, Project

def home(request):
    personal_info = PersonalInformation.objects.first()
    projects = Project.objects.all()
    return render(request, 'index.html', {'personal_info': personal_info, 'projects': projects})