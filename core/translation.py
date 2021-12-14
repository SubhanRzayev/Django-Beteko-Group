from django.db.models import fields
from modeltranslation.translator import translator, TranslationOptions
from .models import Blog,About

class BlogTranslationOptions(TranslationOptions):
    fields = ('title', 'description',)

translator.register(Blog, BlogTranslationOptions)

class AboutTranslationOptions(TranslationOptions):
    fields = ('title','description',)
    
translator.register(About,AboutTranslationOptions)
