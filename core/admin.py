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
    list_display = ('title','description','about_image',)
    list_filter = ('title',)
    search_fields = ('title',)



@admin.register(Subscriber)
class SubscriberAdmin(admin.ModelAdmin):
    list_display = ('email', 'is_avtive','created_at','update_at',)
    list_filter = ('email',)
    search_fields = ('email',)


    

admin.site.register(Customer)
admin.site.register(Images)

