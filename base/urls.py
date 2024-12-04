from django.urls import path 
from . import views

urlpatterns = [
    path("", views.home, name = 'home'),
    path("myprojects", views.projects, name = 'projects')
]