from django.contrib import admin
from .models import PersonalInformation, TechStack, Project, Testimony, Inquiry

admin.site.register(PersonalInformation)
admin.site.register(TechStack)
admin.site.register(Project)
admin.site.register(Testimony)
admin.site.register(Inquiry)