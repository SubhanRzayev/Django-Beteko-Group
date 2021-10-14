from django.shortcuts import render
from django.urls.base import reverse_lazy
from django.views.generic import ListView
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
        return context



class ContactView(CreateView):
    model =Contact
    form_class = ContactForm
    template_name = 'contact.html'
    success_url = reverse_lazy('core:contact')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['address_list'] = Address.objects.all()
        context['customer_list'] = Customer.objects.all()

        return context

    def form_valid(self, form):
        context = super().form_valid(form)
        form.save()
        return context



class AboutView(ListView):
    model = About
    template_name = 'about.html'






    

    




