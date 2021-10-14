from modeltranslation.admin import TranslationAdmin
from django.contrib import admin
from services.models import *


# Register your models here.

@admin.register(Service)
class ServiceAdmin(TranslationAdmin):
    list_display = ('title','description','cover_image','category',)
    list_filter = ('title',)
    search_fields = ('title',)

@admin.register(Project)
class ProjectsAdmin(TranslationAdmin):
    list_display = ('id', 'title','description','image','category',)
    list_filter = ('id',)
    search_fields = ('title',)

@admin.register(Image)
class ImageAdmin(admin.ModelAdmin):
    list_display = ('id','image')
    list_filter = ('id',)

admin.site.register(CategoryService)
admin.site.register(CategoryProject)

