from django.shortcuts import render
from django.template import Library
from core.models import *
from services.models import *


register = Library()

@register.simple_tag
def header_address():
    return Address.objects.all()

@register.simple_tag
def servic():
    return Service.objects.order_by('title')[:7]


@register.simple_tag
def header_category():
    return CategoryService.get_all_service_categories()
    
