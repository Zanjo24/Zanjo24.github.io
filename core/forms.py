from django import forms
from .models import Project, TechStack, Testimony

class ProjectForm(forms.ModelForm):
    class Meta:
        model = Project
        fields = ['project_name', 'description', 'tech_stacks', 'link']
        widgets = {
            'description': forms.Textarea(attrs={'rows': 4}),
            'tech_stacks': forms.CheckboxSelectMultiple(),
        }

class TechStackForm(forms.ModelForm):
    class Meta:
        model = TechStack
        fields = ['name']

class TestimonyForm(forms.ModelForm):
    class Meta:
        model = Testimony
        fields = ['full_name', 'content']
        widgets = {
            'content': forms.Textarea(attrs={'rows': 3}),
        }