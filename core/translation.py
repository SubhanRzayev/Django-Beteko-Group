from django.db.models import fields
from modeltranslation.translator import translator, TranslationOptions
from .models import About, About_service_names, Approach, Careers

# class BlogTranslationOptions(TranslationOptions):
#     fields = ('title', 'description',)

# translator.register(Blog, BlogTranslationOptions)

class AboutTranslationOptions(TranslationOptions):
    fields = ('title','about_paragraph1','about_paragraph2','about_paragraph4')
    
translator.register(About,AboutTranslationOptions)

class About_service_namesTranslationOptions(TranslationOptions):
    fields = ('xidmet_ad',)

translator.register(About_service_names,About_service_namesTranslationOptions)

class ApproachTranslationOptions(TranslationOptions):
    fields = ('title','our_approach_paragraph1','our_approach_paragraph2','our_approach_paragraph3','our_approach_paragraph4',)

translator.register(Approach,ApproachTranslationOptions)

class CareersTranslationOptions(TranslationOptions):
    fields = ('title','description',)
    
translator.register(Careers,CareersTranslationOptions)

# class SpecialKnowledgeRequiredOptions(TranslationOptions):
#     fields = ('tələb_olunan_xüsusi_biliklər','namizədə_tələblər',)
    
# translator.register(SpecialKnowledgeRequired,SpecialKnowledgeRequiredOptions)
