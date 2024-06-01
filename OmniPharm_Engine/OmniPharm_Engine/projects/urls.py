from django.urls import path
from . import views

app_name = 'projects'

urlpatterns = [
    path('', views.projects_list, name="list"),
    path('new-project/', views.project_new, name="new-project"),
    path('<slug:slug>', views.project_page, name="page"),
]