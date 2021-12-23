from django.db import models
from django.contrib.auth import get_user_model
from django.db.models.fields import related
from django.urls.base import reverse
from services.models import *


# Create your models here.

User = get_user_model()


class Subscriber(models.Model):
    """
    This is Email accounts
    """
    
    email = models.EmailField(max_length=50)
    is_avtive = models.BooleanField(default=True,blank=True)

    created_at = models.DateTimeField(auto_now=True,blank=True)
    update_at = models.DateTimeField(auto_now_add=True,blank=True)

    def __str__(self):
        return self.email
    
    class Meta:
        verbose_name = "Subscriber"
        verbose_name_plural = "Abunəçi"


class Contact(models.Model):
    name = models.CharField(max_length=40)
    email = models.EmailField(max_length=60)
    subject = models.CharField(max_length=1000)
    message = models.TextField(max_length=1000)

    created_at = models.DateTimeField(auto_now=True,blank=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Contact"
        verbose_name_plural = "Əlaqə"
    


class About(models.Model):
    title = models.CharField(max_length=50)
    about_paragraph1 = models.TextField(max_length=10000,blank=True,null=True)
    about_paragraph2 = models.TextField(max_length=10000,blank=True,null=True)
    about_paragraph4 = models.TextField(max_length=10000,blank=True,null=True)
    
    about_img = models.ImageField(upload_to = 'media/about')

    def __str__(self):
        return self.title

    
    class Meta:
        verbose_name = "About"
        verbose_name_plural = "Haqqımızdada"
        
class About_service_names(models.Model):
    
    xidmet_ad = models.TextField(max_length=1000,blank=True,null=True)
    
    def __str__(self):
        return str(self.xidmet_ad)
    
    class Meta:
        verbose_name = "About_service_names"
        verbose_name_plural = "Haqqimizda_xidmet_adlari"
    
        
        
class Approach(models.Model):
    title = models.CharField(max_length=50)
    our_approach_paragraph1 = models.TextField(max_length=10000,blank=True,null=True)
    our_approach_paragraph2 = models.TextField(max_length=10000,blank=True,null=True)
    our_approach_paragraph3 = models.TextField(max_length=10000,blank=True,null=True)
    our_approach_paragraph4 = models.TextField(max_length=10000,blank=True,null=True)
    
    our_approach_img = models.ImageField(upload_to = 'media/our_approach')

    def __str__(self):
        return self.title
    
    class Meta:
        verbose_name = "Approach"
        verbose_name_plural = "Bizim yanaşmamız"
    


class Address(models.Model):
    location = models.TextField(max_length=1000,default="Nizami rayonu Əlişir Nəvai küç. 11")
    phone = models.CharField(max_length=20,default='(+994 12) 570-00-04')
    email = models.EmailField(default='office@beteko.az',blank=True)

    def __str__(self):
        return self.email
    
    
    class Meta:
        verbose_name = "Address"
        verbose_name_plural = "Ünvan"

class Carusel(models.Model):
    esas_sekil = models.ImageField(upload_to="esas sekil")
    
    def __str__(self):
        return str(self.esas_sekil)
    
    class Meta:
        verbose_name = "Carusel"
        verbose_name_plural = "Əsas şəkil"
    


class Images(models.Model):
    about = models.ForeignKey('About',db_index=True,on_delete=models.CASCADE,blank=True,null=True,related_name='about_image')
    approach = models.ForeignKey('Approach', db_index=True, on_delete=models.CASCADE,blank=True,null=True,related_name='approach_image')
    image = models.ImageField(upload_to= 'about_approach_image') 
    
    def __str__(self):
        return str(self.image)
    
    class Meta:
        verbose_name = "Images"
        verbose_name_plural = "About Approach Şəkil"


# class Team(models.Model):
#     full_name = models.CharField(max_length=40)
#     position = models.CharField(max_length=40)
#     image = models.ImageField(upload_to = 'team_image')

#     def __str__(self):
#         return self.full_name


# class Customer(models.Model):
#     full_name = models.CharField(max_length=30)
#     level = models.CharField(max_length=20)
#     description = models.TextField(max_length=1000)

#     def __str__(self):
#         return self.full_name



class Careers(models.Model):
    title = models.CharField(max_length=50)
    description = models.TextField(max_length=1000)
    image = models.ImageField(upload_to = 'blog_image')
    created_at = models.DateTimeField(auto_now=True,blank=True)

    def __str__(self):
        return self.title
    
    
    class Meta:
        verbose_name = "Careers"
        verbose_name_plural = "İs Elanlari"
        
        
    def get_absolute_url(self):
        return reverse('core:careers_detail',args=[self.pk])
    
    
    
# class SpecialKnowledgeRequired(models.Model):
#     careers = models.ForeignKey('Careers',db_index=True,on_delete=models.CASCADE,blank=True,null=True,related_name="careers_required")
#     tələb_olunan_xüsusi_biliklər = models.TextField(max_length=10000,blank=True,null=True)
#     namizədə_tələblər = models.TextField(max_length=10000,blank=True,null=True)
    
#     class Meta:
#         verbose_name = "SpecialKnowledgeRequired"
#         verbose_name_plural = "Xüsusi Bilik Tələb olunur"
        
        
#     def __str__(self):
#         return str(self.careers)
    
        
class Pdfile(models.Model):
    careers = models.ForeignKey('Careers',db_index=True,on_delete=models.CASCADE,blank=True,null=True,related_name="careers_required")
    pdfile = models.FileField(upload_to='pdf')
    
    def __str__(self):
        return str(self.pdfile)
    

    
class Employees(models.Model):
    işçilər = models.IntegerField(blank=True,null=True);
    musteriler = models.IntegerField(blank=True,null=True);
    bitmis_layiheler = models.IntegerField(blank=True,null=True);
    islenen_proyektler = models.IntegerField(blank=True,null=True);

    
    class Meta:
        verbose_name = "Employees"
        verbose_name_plural = "İsciler"
        
    
    
    
    






