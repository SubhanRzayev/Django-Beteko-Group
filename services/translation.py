from django.db.models import fields
from modeltranslation.translator import translator, TranslationOptions
from .models import CategoryProject, CategoryService, Project,Service


class ProjectTranslationOptions(TranslationOptions):
    fields = ('title', 'description',)

translator.register(Project, ProjectTranslationOptions)


class ServiceTranslationOptions(TranslationOptions):
    fields = ('title', 'description',)

translator.register(Service, ServiceTranslationOptions)


class CategoryServiceTranslationOptions(TranslationOptions):
    fields = ('category',)
    
translator.register(CategoryService,CategoryServiceTranslationOptions)
    


class CategoryProjectTranslationOptions(TranslationOptions):
    fields = ('title',)
    
    
translator.register(CategoryProject,CategoryProjectTranslationOptions)


