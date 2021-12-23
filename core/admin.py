from django.contrib import admin
from modeltranslation.admin import TranslationAdmin
from core.models import *
# Register your models here.

@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    list_display = ('name','email','subject','message')
    list_filter = ('name',)
    search_fields = ('name',)

@admin.register(Address)
class AddressAdmin(admin.ModelAdmin):
    list_display = ('location','phone','email',)
    list_filter = ('email',)
    search_fields = ('email',)

@admin.register(About)
class AboutAdmin(TranslationAdmin):
    list_display = ('title','about_paragraph1','about_paragraph2','about_paragraph4','about_img',)
    list_filter = ('title',)                                                
    search_fields = ('title',)



@admin.register(Subscriber)
class SubscriberAdmin(admin.ModelAdmin):
    list_display = ('email', 'is_avtive','created_at','update_at',)
    list_filter = ('email',)
    search_fields = ('email',)


@admin.register(About_service_names)
class About_service_namesAdmin(TranslationAdmin):
    list_display = ('xidmet_ad',)
    
    
@admin.register(Approach)
class ApproachAdmin(TranslationAdmin):
    list_display = ('title','our_approach_paragraph1','our_approach_paragraph2','our_approach_paragraph3','our_approach_paragraph4','our_approach_img',) 
    list_filter = ('title',)
    search_fields = ('title',)
    
    
@admin.register(Careers)
class CareersAdmin(TranslationAdmin):
    list_display = ('title','description','image','created_at',)       
    

# @admin.register(SpecialKnowledgeRequired)
# class SpecialKnowledgeRequiredAdmin(TranslationAdmin):
#     list_display = ('tələb_olunan_xüsusi_biliklər','namizədə_tələblər',)      
    
    
admin.site.register(Carusel)
admin.site.register(Images)
admin.site.register(Employees)
admin.site.register(Pdfile)







