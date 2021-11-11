from modeltranslation.translator import translator, TranslationOptions
from .models import Blog,About

class BlogTranslationOptions(TranslationOptions):
    fields = ('title', 'description',)

translator.register(Blog, BlogTranslationOptions)


