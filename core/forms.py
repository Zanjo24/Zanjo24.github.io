from django import forms
from .models import Project, TechStack, Testimony, Inquiry

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

class InquiryForm(forms.ModelForm):
    class Meta:
        model = Inquiry
        fields = ['first_name', 'last_name', 'contact_number', 'email', 'address', 'message']
        widgets = {
            'address': forms.Textarea(attrs={'rows': 2}),
            'message': forms.Textarea(attrs={'rows': 4}),
        }