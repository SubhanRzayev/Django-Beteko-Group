from django.db import models
from django.views.generic import ListView,DetailView
from django.shortcuts import get_object_or_404, render
from django.urls.base import reverse
from services.models import *
from .urls import *

# Create your views here.

class ServiceView(ListView):
    model = Service
    template_name = 'service.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        service = None
        categoryId = self.request.GET.get('category')
        if categoryId:
            service = Service.get_all_services_by_categoryid(categoryId)
        else:
            service = Service.get_service_all()

        context["categories_list"] = CategoryService.get_all_service_categories()
        context['service_list'] =service
        context['servic'] = Service.get_service_all()
        return context

class ServiceDetailView(DetailView):
    model = Service
    template_name = 'service_details.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        service = None
        categoryId = self.request.GET.get('category')
        if categoryId:
            service = Service.get_all_services_by_categoryid(categoryId)
        else:
            service = Service.get_service_all()

        context["categories_list"] = CategoryService.get_all_service_categories()
        context['service_list'] =service
        context['servic'] = Service.get_service_all()
        return context
    



    


class ProjectView(ListView):
    model = Project
    template_name = 'portfolio.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        project = None
        categoryId = self.request.GET.get('category')
        if categoryId:
            project = Project.get_all_projects_by_categoryid(categoryId)
        else:
            project = Project.get_projects_all()

        context["categories_list"] = CategoryProject.get_all_project_categories()
        context['project_list'] =project
        context['project'] = Project.get_projects_all()
        return context


class ProjectDetailView(DetailView):
    model = Project
    template_name = 'projects-detail.html'


    def get_success_url(self):
        return reverse('services:projects_detail', kwargs={'pk', self.object.pk})

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['projects'] = get_object_or_404(Project, pk = self.kwargs['pk'])
        return context
    

    

    

    




