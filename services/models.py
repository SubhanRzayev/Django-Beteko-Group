from django.db import models
from django.urls.base import reverse_lazy
from django.utils import tree
from django.urls import reverse,reverse_lazy

# Create your models here.

class Service(models.Model):
    #relations
    category = models.ForeignKey('CategoryService',db_index=True,blank=True,null=True, related_name='services_category',on_delete=models.CASCADE,)
    
    title = models.CharField(max_length=200)
    description = models.TextField(max_length=1000,blank=True,null=True)
    cover_image = models.ImageField(upload_to = 'service_img',blank = True,null = True)

    def __str__(self):
        return self.title

    @staticmethod
    def get_service_all():
        return Service.objects.all()

    @staticmethod
    def get_all_services_by_categoryid(category_id):
        if category_id:
            return Service.objects.filter(category = category_id)
        else:
            return Service.objects.all()

    def get_absolute_url(self):
        return reverse_lazy("services:service_detail", kwargs={ "pk": self.pk})
            
    
    class Meta:
        verbose_name = "Service"
        verbose_name_plural = "Xidmətlər"
        


class Project(models.Model):
    category = models.ForeignKey('CategoryProject',db_index=True,blank=True,null=True, related_name='projects_category',on_delete=models.CASCADE,)
    title = models.CharField(max_length=50)
    description = models.TextField(max_length=1000,blank=True,null=True)
    image = models.ImageField(upload_to = 'project_img')
    
    def __str__(self):
        return str(self.id)

    
    
    @staticmethod
    def get_projects_all():
        return Project.objects.all()
    

    @staticmethod
    def get_all_projects_by_categoryid(category_id):
        if category_id:
            return Project.objects.filter(category = category_id)
        else:
            return Project.objects.all()


    def get_absolute_url(self):
        return reverse_lazy("services:projects_detail", kwargs={ "pk": self.pk})
    
    
    class Meta:
        verbose_name = "Project"
        verbose_name_plural = "Proyektlər"


    
class CategoryService(models.Model):
    parent_category = models.ForeignKey('self',on_delete=models.CASCADE,blank=True,null=True,related_name="category_subcategories")    
    
    category = models.CharField(max_length=80)

    def __str__(self):
        if self.parent_category:
            return f"{self.parent_category.category} > {self.category}"
        return str(self.category)

    @staticmethod
    def get_all_service_categories():
        return CategoryService.objects.filter(parent_category=None)

    class Meta:
        verbose_name = "CategoryService"
        verbose_name_plural = "KateqoriyaXidmətlər"
    
    

        
    



class CategoryProject(models.Model):
    title = models.CharField(max_length=80)


    def __str__(self):
        return self.title

    @staticmethod
    def get_all_project_categories():
        return CategoryProject.objects.all()


    class Meta:
        verbose_name = "CategoryProject"
        verbose_name_plural = "KateqoriyaProyektlər"

    

class Image(models.Model):
    service = models.ForeignKey('Service',db_index=True,on_delete=models.CASCADE,blank=True,null=True,related_name='service_image')
    projects = models.ForeignKey('Project',db_index=True,on_delete=models.CASCADE,blank=True,null=True,related_name='projects_image')
    image = models.ImageField(upload_to = 'service_image')

    def __str__(self):
        return str(self.image)
    
    
    class Meta:
        verbose_name = "Image"
        verbose_name_plural = "Şəkillər"




    




    




