from modeltranslation.translator import translator, TranslationOptions
from .models import Project,Service


class ProjectTranslationOptions(TranslationOptions):
    fields = ('title', 'description',)

translator.register(Project, ProjectTranslationOptions)


class ServiceTranslationOptions(TranslationOptions):
    fields = ('title', 'description',)

translator.register(Service, ServiceTranslationOptions)