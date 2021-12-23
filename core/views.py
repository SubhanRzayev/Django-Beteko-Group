from django.shortcuts import render
from django.urls.base import reverse_lazy
from django.views.generic import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView
from core.forms import ContactForm
from core.models import *
from services.models import *

# Create your views here.

class IndexView(ListView):
    model = About
    template_name = 'index.html'
    success_url =reverse_lazy('core:index')

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
        context['servic'] = Service.get_service_all()[:6]
        context["service_list"] = Service.get_service_all()
        context["about_list"] = About.objects.all()
        context["images_list"] = Images.objects.all()
        context["carusel_list"] = Carusel.objects.all()
        context["employess_list"] = Employees.objects.all()
        
        
        context['about_service_names_list'] = About_service_names.objects.all()
        return context



class ContactView(CreateView):
    model =Contact
    form_class = ContactForm
    template_name = 'contact.html'
    success_url = reverse_lazy('core:contact')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['address_list'] = Address.objects.all()
        

        return context

    def form_valid(self, form):
        context = super().form_valid(form)
        form.save()
        return context



class AboutView(ListView):
    model = About
    template_name = 'about.html'


    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['about_service_names_list'] = About_service_names.objects.all()
        context["employess_list"] = Employees.objects.all()
        

        return context
    
class ApproachView(ListView):
    model = Approach
    template_name = 'approach.html'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["images_list"] = Images.objects.all()  
        context["employess_list"] = Employees.objects.all()
             
        return context

class CareersView(ListView):
    model = Careers
    template_name = 'careers.html'
    

class CareersDetailView(DetailView):
    model = Careers
    template_name = 'careers_detail.html'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["carrers_list"] = Careers.objects.all()
        context["pdfile"] = Pdfile.objects.all()
        context["address_list"] = Address.objects.all()
        return context
    
    


    

    




