from django.contrib import admin
from django.urls import path
from core import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('personal-info/', views.personal_info_view, name='personal_info'),
    path('projects/', views.project_list, name='project_list'),
    path('projects/<int:project_id>/', views.project_detail, name='project_detail'),
    path('add-project/', views.add_project, name='add_project'),
    path('contact/', views.contact_view, name='contact'),
    path('add-testimony/', views.add_testimony, name='add_testimony'),
    path('testimonies/', views.TestimonyListView.as_view(), name='testimony_list'),
    path('testimony/<int:pk>/', views.testimony_detail, name='testimony_detail'),
    
]